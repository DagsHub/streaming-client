import errno
import logging
import os
import platform
import sys
from argparse import ArgumentParser
from os import PathLike
from pathlib import Path
from threading import Lock
from typing import Optional
from dagshub.common import rich_console

from .filesystem import SPECIAL_FILE, DagsHubFilesystem

logger = logging.getLogger(__name__)

SPECIAL_FILE_FH = (1 << 64) - 1

fuse_enabled_systems = ["Linux"]
system = platform.system()
if system not in fuse_enabled_systems:
    err_str = f"FUSE mounting isn't supported on {system}.\n" \
              f"Please use install_hooks to access DagsHub hosted files from a python script"
    raise ImportError(err_str)
from fuse import FUSE, FuseOSError, LoggingMixIn, Operations  # noqa


class DagsHubFUSE(LoggingMixIn, Operations):
    def __init__(self,
                 project_root: Optional[PathLike] = None,
                 repo_url: Optional[str] = None,
                 branch: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None,
                 token: Optional[str] = None):
        # FIXME TODO move autoconfiguration out of FUSE object constructor and to main method
        self.fs = DagsHubFilesystem(project_root=project_root, repo_url=repo_url, branch=branch, username=username,
                                    password=password, token=token)
        logger.debug("__init__")
        self.rwlock = Lock()

    def __call__(self, op, path, *args):
        return super(DagsHubFUSE, self).__call__(op, self.fs.project_root / path[1:], *args)

    def access(self, path, mode):
        """
        Check file accessibility based on the given path and mode.

        Args:
            path (_type_): The path to check accessibility.
            mode (_type_): The access mode to check.

        Returns: True if the file is accessible; otherwise, False.
        """
        logger.debug(f"access - path: {path}, mode:{mode}")
        try:
            self.fs.stat(path)
        except FileNotFoundError:
            return False

    def open(self, path, flags):
        """
        Open a file for reading or writing.

        Args:
            path (_type_): The path of the file to open.
            flags (_type_): The flags for opening the file.

        Raises:
            FuseOSError: If an error occurs while opening the file, a FuseOSError is raised.

        Returns: The file descriptor for the opened file.
        """
        logger.debug(f"open - path: {path}, flags: {flags}")
        if path == Path(self.fs.project_root / SPECIAL_FILE):
            return SPECIAL_FILE_FH
        try:
            self.fs.open(path).close()
        except FileNotFoundError:
            raise FuseOSError(errno.ENOENT)
        logger.debug("finished fs.open")
        return os.open(self.fs._relative_path(path), flags, dir_fd=self.fs.project_root_fd)

    def getattr(self, path, fd=None):
        """
        Get the attributes of a file or directory.

        Args:
            path (_type_): The path to the file or directory.
            fd (_type_, optional): An optional file descriptor. Defaults to None.

        Raises:
            FuseOSError: If the file or directory does not exist, a FuseOSError is raised.

        Returns:
            _type_: A dictionary containing file attributes such as size, mode, and more.
        """
        logger.debug(f"getattr - path:{str(path)}, fd:{fd}")
        try:
            if fd:
                logger.debug("with __stat")
                st = self.fs._DagsHubFilesystem__stat(fd)
            else:
                logger.debug("with fs.stat")
                st = self.fs.stat(path)

            logger.debug(f"st: {st}")
            return {
                key: getattr(st, key)
                for key in (
                    'st_atime',
                    'st_ctime',
                    'st_gid',
                    'st_mode',
                    'st_mtime',
                    # 'st_nlink',
                    'st_size',
                    'st_uid',
                )
            }
        except FileNotFoundError:
            logger.debug("FileNotFound")
            raise FuseOSError(errno.ENOENT)

    def read(self, path, size, offset, fh):
        """
        Read data from a file.

        Args:
            path (_type_): The path of the file to read.
            size (_type_): The size of data to read.
            offset (_type_): The offset in the file.
            fh (_type_): The file descriptor.

        Returns: The data read from the file.
        """
        logger.debug(f"read - path: {path}, offset: {offset}, fh: {fh}")
        if fh == SPECIAL_FILE_FH:
            return self.fs._special_file()[offset:offset + size]
        with self.rwlock:
            os.lseek(fh, offset, 0)
            return os.read(fh, size)

    def readdir(self, path, fh):
        """
        List the contents of a directory.

        Args:
            path (_type_): The path of the directory.
            fh (_type_): The file descriptor.

        Returns: A list of directory contents.
        """
        logger.debug(f"readdir - path: {path}, fh: {fh}")
        return ['.', '..'] + self.fs.listdir(path)

    def release(self, path, fh):
        logger.debug(f"release - path: {path}, fh: {fh}")
        if fh != SPECIAL_FILE_FH:
            return os.close(fh)


def mount(debug=False,
          project_root: Optional[PathLike] = None,
          repo_url: Optional[str] = None,
          branch: Optional[str] = None,
          username: Optional[str] = None,
          password: Optional[str] = None,
          token: Optional[str] = None):
    """_summary_

    Args:
        debug (bool, optional): _description_. Defaults to False.
        project_root (Optional[PathLike], optional): _description_. Defaults to None.
        repo_url (Optional[str], optional): _description_. Defaults to None.
        branch (Optional[str], optional): _description_. Defaults to None.
        username (Optional[str], optional): _description_. Defaults to None.
        password (Optional[str], optional): _description_. Defaults to None.
        token (Optional[str], optional): _description_. Defaults to None.
    """
    logging.basicConfig(level=logging.DEBUG)
    fuse = DagsHubFUSE(project_root=project_root, repo_url=repo_url, branch=branch, username=username,
                       password=password, token=token)
    rich_console.print(
        f'Mounting DagsHubFUSE filesystem at {fuse.fs.project_root}\n'
        f'Run `cd .` in any existing terminals to utilize mounted FS.')
    FUSE(fuse, str(fuse.fs.project_root), foreground=debug, nonempty=True)
    if not debug:
        os.chdir(os.path.realpath(os.curdir))
    # TODO: Clean unmounting procedure


def main():
    parser = ArgumentParser()
    parser.add_argument('project_root', nargs='?')
    parser.add_argument('--repo_url')
    parser.add_argument('--branch')
    parser.add_argument('--username')
    parser.add_argument('--password')
    parser.add_argument('--debug', action='store_true', default=False)  # default=False, nargs=0)

    args = parser.parse_args()

    if not args.debug:
        # Hide tracebacks of errors, display only error message
        sys.tracebacklimit = 0

    mount(**vars(args))


if __name__ == '__main__':
    main()
