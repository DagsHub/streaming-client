import builtins
import io
import os
import re
import subprocess
import sys
from configparser import ConfigParser
from contextlib import contextmanager
from functools import partial, wraps
from multiprocessing import AuthenticationError
from os import PathLike
from pathlib import Path
from typing import Optional, TypeVar, Union, Dict, Set, Tuple, List
from urllib.parse import urlparse
import dacite

from dagshub.common import config, helpers
import logging
from dagshub.common.helpers import http_request, get_project_root
from dagshub.streaming.dataclasses import StorageAPIEntry, ContentAPIEntry, DagshubPath

# Pre 3.11 - need to patch _NormalAccessor for _pathlib, because it pre-caches open and other functions.
# In 3.11 _NormalAccessor was removed
PRE_PYTHON3_11 = sys.version_info.major == 3 and sys.version_info.minor < 11
if PRE_PYTHON3_11:
    from pathlib import _NormalAccessor as _pathlib  # noqa: E402

try:
    from functools import cached_property
except ImportError:
    from cached_property import cached_property

T = TypeVar('T')
logger = logging.getLogger(__name__)


def wrapreturn(wrappertype):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return wrappertype(func(*args, **kwargs))

        return wrapper

    return decorator


class dagshub_ScandirIterator:
    def __init__(self, iterator):
        self._iterator = iterator

    def __iter__(self):
        return self._iterator

    def __next__(self):
        return self._iterator.__next__()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return self


SPECIAL_FILE = Path(".dagshub-streaming")


# TODO: Singleton metaclass that lets us keep a "main" DvcFilesystem instance
class DagsHubFilesystem:
    """
    A DagsHub-repo aware filesystem class

    :param project_root: Path to the git repository with the repo.
        If None, we look up the filesystem from the current dir until we find a git repo
    :param repo_url: URL to the DagsHub repository.
        If None, URL is received from the git configuration
    :param branch: Explicitly sets a branch/commit revision to work with
        If None, branch is received from the git configuration
    :param username: DagsHub username
    :param password: DagsHub password
    :param token: DagsHub API token (as an alternative login variant to username/password)
    :param timeout: Timeout in seconds for HTTP requests.
        Influences all requests except for file download, which has no timeout
    """

    def __init__(self,
                 project_root: Optional[PathLike] = None,
                 repo_url: Optional[str] = None,
                 branch: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None,
                 token: Optional[str] = None,
                 timeout: Optional[int] = None,
                 _project_root_fd: Optional[int] = None):

        # Find root directory of Git project
        if not project_root:
            self.project_root = get_project_root(Path(os.path.abspath('.')))
        else:
            self.project_root = Path(os.path.abspath(project_root))
        del project_root
        # TODO: if no Git project found, search for .dvc project?

        if _project_root_fd:
            self.project_root_fd = _project_root_fd
        else:
            self.project_root_fd = os.open(self.project_root, os.O_DIRECTORY)

        self.dagshub_remotes = []
        self.parse_git_config()

        if not repo_url:
            if len(self.dagshub_remotes) > 0:
                repo_url = self.dagshub_remotes[0]
            else:
                raise ValueError('No DagsHub git remote detected, please specify repo_url= argument or --repo_url flag')

        self.user_specified_branch = branch
        self.parsed_repo_url = urlparse(repo_url)
        self.dvc_remote_url = f'{repo_url}.dvc/cache'
        # Key: path, value: dict of {name, type} on that path (in remote)
        self.remote_tree: Dict[str, Dict[str, str]] = {}

        # Determine if any authentication is needed
        self.username = username or config.username
        self.password = password or config.password
        self.token = token or config.token
        self.timeout = timeout or config.http_timeout

        self._listdir_cache: Dict[str, Optional[Tuple[List[ContentAPIEntry], bool]]] = {}

        # Check that the repo is accessible by accessing the content root
        response = self._api_listdir(DagshubPath(self, self.project_root, Path()))
        if response is None:
            # TODO: Check .dvc/config{,.local} for credentials
            raise AuthenticationError('DagsHub credentials required, however none provided or discovered')

        self._storages = self._api_storages()

    @cached_property
    def _current_revision(self) -> str:
        """
        Gets current revision on repo:
        - If User specified a branch, returns HEAD of that brunch on the remote
        - If branch wasn't detected, returns HEAD of default branch in the speficied remote.
        - If HEAD is a branch, tries to find a dagshub remote associated with it and get its HEAD
        - If HEAD is a commit revision, checks that the commit exists on DagsHub
        """

        if self.user_specified_branch:
            branch = self.user_specified_branch
        else:
            try:
                with open(self.project_root / ".git/HEAD") as head_file:
                    head = head_file.readline().strip()
                if head.startswith("ref"):
                    branch = head.split("/")[-1]
                else:
                    # contents of HEAD is the revision - check that this commit exists on remote
                    if self.is_commit_on_remote(head):
                        return head
                    else:
                        raise RuntimeError(f"Current HEAD ({head}) doesn't exist on the remote. "
                                           f"Please push your changes to the remote or checkout a tracked branch.")

            except FileNotFoundError:
                logger.debug("Couldn't get branch info from local git repository, " +
                             "fetching default branch from the remote...")
                owner, reponame = self.parsed_repo_url.path.split("/")[1:]
                branch = helpers.get_default_branch(owner, reponame, self.auth)
                logger.debug(f'Set default branch: "{branch}"')
        return self.get_remote_branch_head(branch)

    @property
    def content_api_url(self):
        return self.get_api_url(f"/api/v1/repos{self.parsed_repo_url.path}/content/{self._current_revision}")

    @property
    def raw_api_url(self):
        return self.get_api_url(f"/api/v1/repos{self.parsed_repo_url.path}/raw/{self._current_revision}")

    @property
    def storage_api_url(self):
        return self.get_api_url(f"/api/v1/repos{self.parsed_repo_url.path}/storage")

    @property
    def storage_content_api_url(self):
        return f"{self.storage_api_url}/content"

    @property
    def storage_raw_api_url(self):
        return f"{self.storage_api_url}/raw"

    def is_commit_on_remote(self, sha1):
        url = self.get_api_url(f"/api/v1/repos{self.parsed_repo_url.path}/commits/{sha1}")
        resp = self.http_get(url)
        return resp.status_code == 200

    def get_remote_branch_head(self, branch):
        url = self.get_api_url(f"/api/v1/repos{self.parsed_repo_url.path}/branches/{branch}")
        resp = self.http_get(url)
        if resp.status_code != 200:
            raise RuntimeError(f"Got status {resp.status_code} while trying to get head of branch {branch}. \r\n"
                               f"Response body: {resp.content}")
        return resp.json()["commit"]["id"]

    def get_api_url(self, path):
        return str(self.parsed_repo_url._replace(path=path).geturl())

    @property
    def auth(self):
        import dagshub.auth
        from dagshub.auth.token_auth import HTTPBearerAuth

        if self.username is not None and self.password is not None:
            return self.username, self.password

        try:
            token = self.token or dagshub.auth.get_token()
        except dagshub.auth.OauthNonInteractiveShellException:
            logger.debug("Failed to perform OAuth in a non interactive shell")
        if token is not None:
            return HTTPBearerAuth(token)

        # Try to fetch credentials from the git credential file
        proc = subprocess.run(['git', 'credential', 'fill'],
                              input=f'url={self.repo_url}'.encode(),
                              capture_output=True)
        answer = {line[:line.index('=')]: line[line.index('=') + 1:]
                  for line in proc.stdout.decode().splitlines()}
        if 'username' in answer and 'password' in answer:
            return answer['username'], answer['password']

    def parse_git_config(self):
        # Get URLs of dagshub remotes
        git_config = ConfigParser()
        git_config.read(Path(self.project_root) / '.git/config')
        git_remotes = [urlparse(git_config[remote]['url'])
                       for remote in git_config
                       if remote.startswith('remote ')]
        for remote in git_remotes:
            if remote.hostname != config.hostname:
                continue
            remote = remote._replace(netloc=remote.hostname)
            remote = remote._replace(path=re.compile(r'(\.git)?/?$').sub('', remote.path))
            self.dagshub_remotes.append(remote.geturl())

    def __del__(self):
        os.close(self.project_root_fd)

    def _parse_path(self, file: Union[str, PathLike, int]) -> DagshubPath:
        if isinstance(file, int):
            return DagshubPath(self, None, None)
        if file == "":
            return DagshubPath(self, None, None)
        abspath = Path(os.path.abspath(file))
        try:
            relpath = abspath.relative_to(os.path.abspath(self.project_root))
            if str(relpath).startswith("<"):
                return DagshubPath(self, abspath, None)
            return DagshubPath(self, abspath, relpath)
        except ValueError:
            return DagshubPath(self, abspath, None)

    def _special_file(self):
        # TODO Include more information in this file
        return b'v0\n'

    def open(self, file, mode='r', buffering=-1, encoding=None,
             errors=None, newline=None, closefd=True, opener=None):
        if type(file) is bytes:
            file = os.fsdecode(file)
        path = self._parse_path(file)
        if path.is_in_repo:
            if opener is not None:
                raise NotImplementedError('DagsHub\'s patched open() does not support custom openers')
            project_root_opener = partial(os.open, dir_fd=self.project_root_fd)
            if path.is_passthrough_path:
                return self.__open(path.relative_path, mode, buffering, encoding, errors, newline,
                                   closefd, opener=project_root_opener)
            elif path.relative_path == SPECIAL_FILE:
                return io.BytesIO(self._special_file())
            else:
                try:
                    return self.__open(path.relative_path, mode, buffering, encoding, errors, newline,
                                       closefd, opener=project_root_opener)
                except FileNotFoundError as err:
                    # Open for reading - try to download the file
                    if "r" in mode:
                        resp = self._api_download_file_git(path)
                        if resp.status_code < 400:
                            self._mkdirs(path.relative_path.parent, dir_fd=self.project_root_fd)
                            # TODO: Handle symlinks
                            with self.__open(path.relative_path, 'wb', opener=project_root_opener) as output:
                                output.write(resp.content)
                            return self.__open(path.relative_path, mode, buffering, encoding, errors, newline,
                                               closefd, opener=project_root_opener)
                        else:
                            # TODO: After API no longer 500s on FileNotFounds
                            #       check status code and only return FileNotFound on 404s
                            raise FileNotFoundError(f'Error finding {path.relative_path} in repo or on DagsHub')
                    # Write modes - make sure that the folder is a tracked folder (create if doesn't exist on disk),
                    # and then let the user write to file
                    else:
                        try:
                            # Using the fact that stat creates tracked dirs (but still throws on nonexistent dirs)
                            _ = self.stat(self.project_root / path.relative_path.parent)
                        except FileNotFoundError:
                            raise err
                        # Try to download the file if we're in append modes
                        if "a" in mode or "+" in mode:
                            resp = self._api_download_file_git(path.relative_path.as_posix())
                            if resp.status_code < 400:
                                with self.__open(path.relative_path, 'wb', opener=project_root_opener) as output:
                                    output.write(resp.content)
                        return self.__open(path.relative_path, mode, buffering, encoding, errors, newline,
                                           closefd, opener=project_root_opener)

        else:
            return self.__open(file, mode, buffering, encoding, errors, newline,
                               closefd, opener)

    def os_open(self, path, flags, mode=0o777, *, dir_fd=None):
        """
        os.open is supposed to be lower level, but it's still being used by e.g. Pathlib
        We're trying to wrap around it here, by parsing flags and calling the higher-level open
        Caveats: list of flags being handled is not exhaustive + mode doesn't work
                 (because we lose them when passing to builtin open)
        WARNING: DO NOT patch actual os.open with it, because the builtin uses os.open.
                 This is only for the purposes of patching pathlib.open in Python 3.9 and below.
                 Since Python 3.10 pathlib uses io.open, and in Python 3.11 they removed the accessor completely
        """
        if dir_fd is not None:  # If dir_fd supplied, path is relative to that dir's fd, will handle in the future
            logger.debug("fs.os_open - NotImplemented")
            raise NotImplementedError('DagsHub\'s patched os.open() (for pathlib only) does not support dir_fd')
        path = self._parse_path(path)
        if path.is_in_repo:
            try:
                open_mode = "r"
                # Write modes - calling in append mode,
                # This way we create the intermediate folders if file doesn't exist, but the folder it's in does
                # Append so we don't truncate the file
                if not (flags & os.O_RDONLY):
                    open_mode = "a"
                logger.debug("fs.os_open - trying to materialize path")
                self.open(path.relative_path, mode=open_mode).close()
                logger.debug("fs.os_open - successfully materialized path")
            except FileNotFoundError:
                logger.debug("fs.os_open - failed to materialize path, os.open will throw")
        return os.open(path.relative_path, flags, mode, dir_fd=dir_fd)

    def stat(self, path, *, dir_fd=None, follow_symlinks=True):
        if type(path) is bytes:
            path = os.fsdecode(path)
        if dir_fd is not None or not follow_symlinks:
            logger.debug("fs.stat - NotImplemented")
            raise NotImplementedError('DagsHub\'s patched stat() does not support dir_fd or follow_symlinks')
        parsed_path = self._parse_path(path)
        # todo: remove False
        if parsed_path.is_in_repo:
            logger.debug("fs.stat - is relative path")
            if parsed_path.is_passthrough_path:
                return self.__stat(parsed_path.relative_path, dir_fd=self.project_root_fd)
            elif parsed_path.relative_path == SPECIAL_FILE:
                return dagshub_stat_result(self, path, is_directory=False, custom_size=len(self._special_file()))
            else:
                try:
                    logger.debug(f"fs.stat - calling __stat - relative_path: {path}, dir_fd: {self.project_root_fd}")
                    return self.__stat(parsed_path.relative_path, dir_fd=self.project_root_fd)
                except FileNotFoundError as err:
                    logger.debug("fs.stat - FileNotFoundError")
                    logger.debug(f"remote_tree: {self.remote_tree}")
                    parent_path = parsed_path.relative_path.parent
                    if str(parent_path) not in self.remote_tree:
                        try:
                            # Run listdir to update cache
                            self.listdir(self.project_root / parent_path)
                        except FileNotFoundError:
                            raise err

                    cached_remote_parent_tree = self.remote_tree.get(str(parent_path))
                    logger.debug(f"cached_remote_parent_tree: {cached_remote_parent_tree}")

                    if cached_remote_parent_tree is None:
                        raise err

                    filetype = cached_remote_parent_tree.get(parsed_path.name)
                    if filetype is None:
                        raise err

                    if filetype == "file":
                        return dagshub_stat_result(self, path, is_directory=False)
                    elif filetype == "dir":
                        self._mkdirs(parsed_path.relative_path, dir_fd=self.project_root_fd)
                        return self.__stat(parsed_path.relative_path, dir_fd=self.project_root_fd)
                    else:
                        raise RuntimeError(f"Unknown file type {filetype} for path {str(parsed_path)}")

        else:
            return self.__stat(path, follow_symlinks=follow_symlinks)

    def chdir(self, path):
        if type(path) is bytes:
            path = os.fsdecode(path)
        parsed_path = self._parse_path(path)
        if parsed_path.is_in_repo:
            try:
                self.__chdir(parsed_path.absolute_path)
            except FileNotFoundError:
                resp = self._api_listdir(parsed_path)
                # FIXME: if path is file, return FileNotFound instead of the listdir error
                if resp is not None:
                    self._mkdirs(parsed_path.relative_path, dir_fd=self.project_root_fd)
                    self.__chdir(parsed_path.absolute_path)
                else:
                    raise
        else:
            self.__chdir(path)

    def listdir(self, path='.'):
        # listdir needs to return results for bytes path arg also in bytes
        is_bytes_path_arg = type(path) is bytes
        if is_bytes_path_arg:
            str_path = os.fsdecode(path)
        else:
            str_path = path
        parsed_path = self._parse_path(str_path)
        if parsed_path.is_in_repo:
            if parsed_path.is_passthrough_path:
                with self._open_fd(parsed_path.relative_path) as fd:
                    return self.__listdir(fd)
            else:
                dircontents: Set[str] = set()
                error = None
                try:
                    with self._open_fd(parsed_path.relative_path) as fd:
                        dircontents.update(self.__listdir(fd))
                except FileNotFoundError as e:
                    error = e
                dircontents.update(
                    special.name for special in self._get_special_paths(parsed_path, Path(), is_bytes_path_arg))
                resp = self._api_listdir(parsed_path)
                if resp is not None:
                    dircontents.update(Path(f.path).name for f in resp)
                    self.remote_tree[str(parsed_path.relative_path)] = {
                        Path(f.path).name: f.type
                        for f in resp
                    }
                    res = list(dircontents)
                    if is_bytes_path_arg:
                        res = [os.fsencode(p) for p in res]
                    return res
                else:
                    if error is not None:
                        raise error
                    else:
                        res = list(dircontents)
                        if is_bytes_path_arg:
                            res = [os.fsencode(p) for p in res]
                        return res
        else:
            return self.__listdir(path)

    @wrapreturn(dagshub_ScandirIterator)
    def scandir(self, path='.'):
        # scandir needs to return name and path as bytes, if entry arg is bytes
        is_bytes_path_arg = type(path) is bytes
        if is_bytes_path_arg:
            str_path = os.fsdecode(path)
        else:
            str_path = path
        parsed_path = self._parse_path(str_path)
        if parsed_path.is_in_repo and not parsed_path.is_passthrough_path:
            path = Path(str_path)
            local_filenames = set()
            try:
                for direntry in self.__scandir(path):
                    local_filenames.add(direntry.name)
                    yield direntry
            except FileNotFoundError:
                pass
            for special_entry in self._get_special_paths(parsed_path, path, is_bytes_path_arg):
                if special_entry.path not in local_filenames:
                    yield special_entry
            # Mix in the results from the API
            resp = self._api_listdir(parsed_path)
            if resp is not None:
                for f in resp:
                    name = Path(f.path).name
                    if name not in local_filenames:
                        yield dagshub_DirEntry(self, path / name, f.type == 'dir', is_binary=is_bytes_path_arg)
        else:
            for entry in self.__scandir(path):
                yield entry

    def _get_special_paths(
        self, dh_path: DagshubPath, relative_to: PathLike, is_binary: bool
    ) -> Set["dagshub_DirEntry"]:
        def generate_entry(path, is_directory):
            if isinstance(path, str):
                path = Path(path)
            return dagshub_DirEntry(self, relative_to / path,
                                    is_directory=is_directory, is_binary=is_binary)

        has_storages = len(self._storages) > 0
        res = set()
        str_path = dh_path.relative_path.as_posix()
        if str_path == ".":
            res.add(generate_entry(SPECIAL_FILE, False))
            if has_storages:
                res.add(generate_entry(".dagshub", True))
        elif str_path.startswith(".dagshub") and has_storages:
            storage_paths = [s.path_in_mount for s in self._storages]
            for sp in storage_paths:
                try:
                    relpath = sp.relative_to(dh_path.relative_path)
                    if relpath != Path():
                        res.add(generate_entry(relpath.parts[0], True))
                except ValueError:
                    continue
        return res

    def _api_listdir(self, path: DagshubPath, include_size: bool = False) -> Optional[List[ContentAPIEntry]]:
        response, hit = self._check_listdir_cache(path.relative_path.as_posix(), include_size)
        if hit:
            return response
        response = self.http_get(self._content_url_for_path(path),
                                 params={'include_size': 'true'} if include_size else {},
                                 headers=config.requests_headers)
        if response.status_code >= 400:
            logger.debug(f"Got HTTP code {response.status_code} while listing {path}, no results will be returned")
            return None
        res = []
        for entry_raw in response.json():
            entry = dacite.from_dict(ContentAPIEntry, entry_raw)
            # Ignore storage root entries, we handle them separately in a different place
            if entry.type == "storage":
                continue
            res.append(entry)
        self._listdir_cache[path.relative_path.as_posix()] = (res, include_size)
        return res

    def _api_storages(self) -> List[StorageAPIEntry]:
        response = self.http_get(self.storage_api_url)
        if response.status_code >= 400:
            logger.warning(f"Got HTTP code {response.status_code} while getting storages. Content: {response.content}")
            logger.warning("Storages are unavailable")
            return []
        return [dacite.from_dict(StorageAPIEntry, storage_entry) for storage_entry in response.json()]

    def _check_listdir_cache(self, path: str, include_size: bool) -> Tuple[Optional[List[ContentAPIEntry]], bool]:
        # Checks that path has a pre-cached response
        # If include_size is True, but only a response without size is cached, that's a cache miss
        if path in self._listdir_cache:
            cache_val, with_size = self._listdir_cache[path]
            if not include_size or (include_size and with_size):
                return cache_val, True
        return None, False

    def _content_url_for_path(self, path: DagshubPath):
        if not path.is_in_repo:
            raise RuntimeError(f"Can't access path {path.absolute_path} outside of repo")
        str_path = path.relative_path.as_posix()
        if path.is_storage_path:
            path_to_access = str_path[len(".dagshub/storage/"):]
            return f"{self.storage_content_api_url}/{path_to_access}"
        return f"{self.content_api_url}/{str_path}"

    def _raw_url_for_path(self, path: DagshubPath):
        if not path.is_in_repo:
            raise RuntimeError(f"Can't access path {path.absolute_path} outside of repo")
        str_path = path.relative_path.as_posix()
        if path.is_storage_path:
            path_to_access = str_path[len(".dagshub/storage/"):]
            return f"{self.storage_raw_api_url}/{path_to_access}"
        return f"{self.raw_api_url}/{str_path}"

    def _api_download_file_git(self, path: DagshubPath):
        return self.http_get(self._raw_url_for_path(path), headers=config.requests_headers, timeout=None)

    def http_get(self, path: str, **kwargs):
        timeout = self.timeout
        if "timeout" in kwargs:
            timeout = kwargs["timeout"]
            del kwargs["timeout"]
        return http_request("GET", path, auth=self.auth, timeout=timeout, **kwargs)

    def install_hooks(self):
        if not hasattr(self.__class__, f'_{self.__class__.__name__}__unpatched'):
            # TODO: DRY this dictionary. i.e. __open() links cls.__open
            #  and io.open even though this dictionary links them
            #  Cannot use a dict as the source of truth because type hints rely on
            #  __get_unpatched inferring the right type
            self.__class__.__unpatched = {
                'open': io.open,
                'stat': os.stat,
                'listdir': os.listdir,
                'scandir': os.scandir,
                'chdir': os.chdir,
            }
            if PRE_PYTHON3_11:
                self.__class__.__unpatched["pathlib_open"] = _pathlib.open
        io.open = builtins.open = self.open
        os.stat = self.stat
        os.listdir = self.listdir
        os.scandir = self.scandir
        os.chdir = self.chdir
        if PRE_PYTHON3_11:
            if sys.version_info.minor == 10:
                # Python 3.10 - pathlib uses io.open
                _pathlib.open = self.open
            else:
                # Python <=3.9 - pathlib uses os.open
                _pathlib.open = self.os_open
            _pathlib.stat = self.stat
            _pathlib.listdir = self.listdir
            _pathlib.scandir = self.scandir

        self.__class__.hooked_instance = self

    @classmethod
    def uninstall_hooks(cls):
        if hasattr(cls, f'_{cls.__name__}__unpatched'):
            io.open = builtins.open = cls.__unpatched['open']
            os.stat = cls.__unpatched['stat']
            os.listdir = cls.__unpatched['listdir']
            os.scandir = cls.__unpatched['scandir']
            os.chdir = cls.__unpatched['chdir']
            if PRE_PYTHON3_11:
                _pathlib.open = cls.__unpatched['pathlib_open']
                _pathlib.stat = cls.__unpatched['stat']
                _pathlib.listdir = cls.__unpatched['listdir']
                _pathlib.scandir = cls.__unpatched['scandir']

    def _mkdirs(self, relative_path: PathLike, dir_fd: Optional[int] = None):
        for parent in list(relative_path.parents)[::-1]:
            try:
                self.__stat(parent, dir_fd=dir_fd)
            except (OSError, ValueError):
                os.mkdir(parent, dir_fd=dir_fd)
        try:
            self.__stat(relative_path, dir_fd=dir_fd)
        except (OSError, ValueError):
            os.mkdir(relative_path, dir_fd=dir_fd)

    @contextmanager
    def _open_fd(self, relative_path):
        fd = None
        try:
            fd = os.open(relative_path, os.O_DIRECTORY, dir_fd=self.project_root_fd)
            yield fd
        finally:
            if fd is not None:
                os.close(fd)

    @classmethod
    def __get_unpatched(cls, key, alt: T) -> T:
        if hasattr(cls, f'_{cls.__name__}__unpatched'):
            return cls.__unpatched[key]
        else:
            return alt

    @property
    def __open(self):
        return self.__get_unpatched('open', io.open)

    @property
    def __stat(self):
        return self.__get_unpatched('stat', os.stat)

    @property
    def __listdir(self):
        return self.__get_unpatched('listdir', os.listdir)

    @property
    def __scandir(self):
        return self.__get_unpatched('scandir', os.scandir)

    @property
    def __chdir(self):
        return self.__get_unpatched("chdir", os.chdir)


def install_hooks(project_root: Optional[PathLike] = None,
                  repo_url: Optional[str] = None,
                  branch: Optional[str] = None,
                  username: Optional[str] = None,
                  password: Optional[str] = None,
                  token: Optional[str] = None,
                  timeout: Optional[int] = None):
    """
    Monkey patches builtin Python functions to make them DagsHub-repo aware.
    Patched functions are: `open()`, `os.listdir()`, `os.scandir()`, `os.stat()` + pathlib's functions that use them

    This is equivalent to creating a `DagsHubFilesystem` object and calling its `install_hooks()` method

    :param project_root: Path to the git repository with the repo.
        If None, we look up the filesystem from the current dir until we find a git repo
    :param repo_url: URL to the DagsHub repository.
        If None, URL is received from the git configuration
    :param branch: Explicitly sets a branch/commit revision to work with
        If None, branch is received from the git configuration
    :param username: DagsHub username
    :param password: DagsHub password
    :param token: DagsHub API token (as an alternative login variant to username/password)
    :param timeout: Timeout in seconds for HTTP requests.
        Influences all requests except for file download, which has no timeout
    """
    fs = DagsHubFilesystem(project_root=project_root, repo_url=repo_url, branch=branch, username=username,
                           password=password, token=token, timeout=timeout)
    fs.install_hooks()


def uninstall_hooks():
    DagsHubFilesystem.uninstall_hooks()


class dagshub_stat_result:
    def __init__(self, fs: 'DagsHubFilesystem', path: PathLike, is_directory: bool, custom_size: int = None):
        self._fs = fs
        self._path = path
        self._is_directory = is_directory
        self._custom_size = custom_size
        assert not self._is_directory  # TODO make folder stats lazy?

    def __getattr__(self, name: str):
        if not name.startswith('st_'):
            raise AttributeError
        if hasattr(self, '_true_stat'):
            return os.stat_result.__getattribute__(self._true_stat, name)
        if name == 'st_uid':
            return os.getuid()
        elif name == 'st_gid':
            return os.getgid()
        elif name == 'st_atime' or name == 'st_mtime' or name == 'st_ctime':
            return 0
        elif name == 'st_mode':
            return 0o100644
        elif name == 'st_size':
            if self._custom_size:
                return self._custom_size
            return 1100  # hardcoded size because size requests take a disproportionate amount of time
        self._fs.open(self._path)
        self._true_stat = self._fs._DagsHubFilesystem__stat(self._fs._relative_path(self._path),
                                                            dir_fd=self._fs.project_root_fd)
        return os.stat_result.__getattribute__(self._true_stat, name)

    def __repr__(self):
        inner = repr(self._true_stat) if hasattr(self, '_true_stat') else 'pending...'
        return f'dagshub_stat_result({inner}, path={self._path})'


class dagshub_DirEntry:
    def __init__(self, fs: 'DagsHubFilesystem', path: PathLike, is_directory: bool = False, is_binary: bool = False):
        self._fs = fs
        self._path = path
        self._is_directory = is_directory
        self._is_binary = is_binary

    @property
    def name(self):
        # TODO: create decorator for delegation
        if hasattr(self, '_true_direntry'):
            name = self._true_direntry.name
        else:
            name = self._path.name
        return os.fsencode(name) if self._is_binary else name

    @property
    def path(self):
        if hasattr(self, '_true_direntry'):
            path = self._true_direntry.path
        else:
            path = str(self._path)
        return os.fsencode(path) if self._is_binary else path

    def is_dir(self):
        if hasattr(self, '_true_direntry'):
            return self._true_direntry.is_dir()
        else:
            return self._is_directory

    def is_file(self):
        if hasattr(self, '_true_direntry'):
            return self._true_direntry.is_file()
        else:
            # TODO: Symlinks should return false
            return not self._is_directory

    def stat(self):
        if hasattr(self, '_true_direntry'):
            return self._true_direntry.stat()
        else:
            return self._fs.stat(self._path)

    def __getattr__(self, name: str):
        if name == '_true_direntry':
            raise AttributeError
        if hasattr(self, '_true_direntry'):
            return os.DirEntry.__getattribute__(self._true_direntry, name)
        if self._is_directory:
            self._fs._mkdirs(self._fs._relative_path(self._path), dir_fd=self._fs.project_root_fd)
        else:
            self._fs.open(self._path)
        with self._open_fd(self._fs._relative_path(self._path).parent) as fd:
            for direntry in self._fs._DagsHubFilesystem__scandir(fd):
                if direntry.name == self._path.name:
                    self._true_direntry = direntry
                    return os.DirEntry.__getattribute__(self._true_direntry, name)
            else:
                raise FileNotFoundError

    def __repr__(self):
        cached = ' (cached)' if hasattr(self, '_true_direntry') else ''
        return f'<dagshub_DirEntry \'{self.name}\'{cached}>'


# Used for testing purposes only
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    fs = DagsHubFilesystem()
    fs.install_hooks()

__all__ = [DagsHubFilesystem.__name__, install_hooks.__name__]
