import builtins
import io
import os
import subprocess
from configparser import ConfigParser
from functools import wraps
from multiprocessing import AuthenticationError
from os import PathLike
from os.path import ismount
from pathlib import Path
from pathlib import _NormalAccessor as _pathlib
from typing import Optional, TypeVar
from urllib.parse import urlparse

import requests

T = TypeVar('T')

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
        def __enter__(self):
            return self
        def __exit__(self, *args):
            return self

# TODO: Singleton metaclass that lets us keep a "main" DvcFilesystem instance
class DagsHubFilesystem:

    __slots__ = 'project_root', 'content_api_url', 'raw_api_url', 'dvc_remote_url', 'auth'

    def __init__(self,
                 project_root: Optional[PathLike] = None,
                 repo_url: Optional[str] = None,
                 branch: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None):

        # Find root directory of Git project
        if not project_root:
            self.project_root = Path('.').absolute()
            while not (self.project_root / '.git').is_dir():
                if ismount(self.project_root):
                    raise ValueError('No git project found! (stopped at mountpoint {self.project_root})')
                self.project_root = self.project_root.parent
        else:
            self.project_root = Path(project_root)
        del project_root
        # TODO: if no Git project found, search for .dvc project?

        # Find Git remote URL
        git_config = ConfigParser()
        git_config.read(self.project_root / '.git/config')
        git_remotes = [git_config[remote]['url']
                        for remote in git_config
                        if remote.startswith('remote ')]
        dagshub_remotes = next(remote.removesuffix('/').removesuffix('.git')
                                for remote in git_remotes
                                if remote.startswith("https://dagshub.com/"))
        # TODO: if no DagsHub remote found, check DVC remotes (i.e. using GitHub Connect)

        if not repo_url:
            if len(dagshub_remotes) > 0:
                repo_url = dagshub_remotes
            else:
                raise ValueError('No DagsHub git remote detected, please specify repo_url')

        if not branch:
            branch = (self.__open(self.project_root / '.git/HEAD')
                          .readline()
                          .strip()
                          .split('/')[-1]) or 'main'
            # TODO: check DagsHub for default branch if no branch/commit checked out

        parsed_repo_url = urlparse(repo_url)
        content_api_path = f'/api/v1/repos{parsed_repo_url.path}/content/{branch}'

        self.content_api_url = parsed_repo_url._replace(path=content_api_path).geturl()
        self.raw_api_url = f'{repo_url}/raw/{branch}'
        self.dvc_remote_url = f'{repo_url}.dvc/cache'

        del repo_url, branch, parsed_repo_url, content_api_path

        # Determine if any authentication is needed
        self.auth = (username, password) if username or password else None
        del username, password
        response = requests.get(self.content_api_url, auth=self.auth)
        if response.ok:
            # No authentication needed
            pass
        else:
            # Check Git credential stores
            proc = subprocess.run(['git', 'credential', 'fill'],
                                input=f'url={repo_url}'.encode(),
                                capture_output=True)
            answer = {line[:line.index('=')]: line[line.index('=')+1:]
                        for line in proc.stdout.decode().splitlines()}
            if 'username' in answer and 'password' in answer:
                self.auth = (answer['username'], answer['password'])
            else:
                # TODO: Check .dvc/config{,.local} for credentials
                raise AuthenticationError('DagsHub credentials required, however none provided or discovered')

    def _relative_path(self, file: PathLike):
        path = Path(file).absolute()
        if path.is_relative_to(self.project_root.absolute()):
            return path.relative_to(self.project_root.absolute())
        else:
            return None

    def open(self, file: PathLike, mode: str = 'r', *args, **kwargs):
        try:
            return self.__open(file, mode, *args, **kwargs)
        except FileNotFoundError as e:
            relative_path = self._relative_path(file)
            if relative_path:
                resp = requests.get(f'{self.raw_api_url}/{relative_path}', auth=self.auth)
                if resp.ok:
                    Path(file).absolute().parent.mkdir(parents=True, exist_ok=True)
                    # TODO: Handle symlinks
                    with self.__open(file, 'wb') as output:
                        output.write(resp.content)
                    return self.__open(file, mode)
                else:
                    # TODO: After API no longer 500s on FileNotFounds
                    #       check status code and only return FileNotFound on 404s
                    raise FileNotFoundError(f'Error finding {relative_path} in repo or on DagsHub')
            else:
                # Outside of repository
                raise e

    def stat(self, path: PathLike, *, dir_fd=None, follow_symlinks=True):
        if dir_fd is not None or not follow_symlinks:
            raise NotImplementedError('DagsHub\'s patched stat() does not support additional arguments')
        try:
            return self.__stat(path)
        except FileNotFoundError as e:
            relative_path = self._relative_path(path)
            if relative_path:
                # TODO: check single file content API instead of directory when it becomes available
                # TODO: use DVC remote cache to download file now that we have the directory json
                resp = requests.get(f'{self.content_api_url}/{relative_path.parent}', auth=self.auth)
                if resp.ok:
                    matches = [info for info in resp.json() if Path(info['path']) == relative_path]
                    assert len(matches) <= 1
                    if matches:
                        if matches[0]['type'] == 'dir':
                            Path(path).mkdir(parents=True, exist_ok=True)
                            return self.__stat(path)
                        else:
                            return dagshub_stat_result(self, path)
                    else:
                        raise FileNotFoundError
                else:
                    raise FileNotFoundError
            else:
                raise e

    def listdir(self, path='.'):
        relative_path = self._relative_path(path)
        if relative_path:
            dircontents: set[str] = set()
            error = None
            try:
                dircontents.update(self.__listdir(path))
            except FileNotFoundError as e:
                error = e
            resp = requests.get(f'{self.content_api_url}/{relative_path}')
            if resp.ok:
                dircontents.update(Path(f['path']).name for f in resp.json())
                return list(dircontents)
            else:
                if error is not None:
                    raise error
                else:
                    return list(dircontents)
        else:
            return self.__listdir(path)

    @wrapreturn(dagshub_ScandirIterator)
    def scandir(self, path='.'):
        path = Path(path)
        relative_path = self._relative_path(path)
        if relative_path:
            local_filenames = set()
            for direntry in self.__scandir(path):
                local_filenames.add(direntry.name)
                yield direntry
            resp = requests.get(f'{self.content_api_url}/{relative_path}')
            if resp.ok:
                for f in resp.json():
                    name = Path(f['path']).name
                    if name not in local_filenames:
                        yield dagshub_DirEntry(self, path / name, f['type'] == 'dir')
        else:
            return self.__scandir(path)

    def install_hooks(self):
        if not hasattr(self.__class__, f'_{self.__class__.__name__}__unpatched'):
            # TODO: DRY this dictionary. i.e. __open() links cls.__open and io.open even though this dictionary links them
            #       Cannot use a dict as the source of truth because type hints rely on __get_unpatched inferring the right type
            self.__class__.__unpatched = {
                'open': io.open,
                'stat': os.stat,
                'listdir': os.listdir,
                'scandir': os.scandir
            }
        io.open = builtins.open = _pathlib.open = self.open
        os.stat = _pathlib.stat = self.stat
        os.listdir = _pathlib.listdir = self.listdir
        os.scandir = _pathlib.scandir = self.scandir
        self.__class__.hooked_instance = self

    @classmethod
    def __get_unpatched(cls, key, alt: T) -> T:
        if hasattr(cls, f'_{cls.__name__}__unpatched'):
            return cls.__unpatched[key]
        else:
            return alt

    @classmethod
    @property
    def __open(cls):
        return cls.__get_unpatched('open', io.open)

    @classmethod
    @property
    def __stat(cls):
        return cls.__get_unpatched('stat', os.stat)

    @classmethod
    @property
    def __listdir(cls):
        return cls.__get_unpatched('listdir', os.listdir)

    @classmethod
    @property
    def __scandir(cls):
        return cls.__get_unpatched('scandir', os.scandir)

def install_hooks(project_root: Optional[PathLike] = None,
                  repo_url: Optional[str] = None,
                  branch: Optional[str] = None,
                  username: Optional[str] = None,
                  password: Optional[str] = None):
    fs = DagsHubFilesystem(project_root=project_root, repo_url=repo_url, branch=branch, username=username, password=password)
    fs.install_hooks()

class dagshub_stat_result:
    def __init__(self, fs: 'DagsHubFilesystem', path: PathLike):
        self._fs = fs
        self._path = path

    def __getattr__(self, name: str):
        if not name.startswith('st_'):
            raise AttributeError
        if hasattr(self, '_true_stat'):
            return os.stat_result.__getattribute__(self._true_stat, name)
        self._fs.open(self._path)
        self._true_stat = self._fs._DagsHubFilesystem__stat(self._path)
        return os.stat_result.__getattribute__(self._true_stat, name)

    def __repr__(self):
        inner = repr(self._true_stat) if hasattr(self, '_true_stat') else 'pending...'
        return f'dagshub_stat_result({inner}, path={self._path})'

class dagshub_DirEntry:
    def __init__(self, fs: 'DagsHubFilesystem', path: PathLike, is_directory=False):
        self._fs = fs
        self._path = path
        self._is_directory = is_directory
    
    @property
    def name(self):
        # TODO: create decorator for delegation
        if hasattr(self, '_true_direntry'):
            return self._true_direntry.name
        else:
            return self._path.name

    @property
    def path(self):
        if hasattr(self, '_true_direntry'):
            return self._true_direntry.path
        else:
            return str(self._path)

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
            self._path.mkdir(parents=True, exist_ok=True)
        else:
            self._fs.open(self._path)
        for direntry in self._fs._DagsHubFilesystem__scandir(self._path.parent):
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
    install_hooks()

__all__ = [DagsHubFilesystem.__name__, install_hooks.__name__]