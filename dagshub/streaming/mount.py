from argparse import ArgumentParser
import argparse
import logging
import atexit
import errno
import os
from os import PathLike
from pathlib import Path
from threading import Lock
import threading
from time import sleep
from typing import Optional

from fuse import FUSE, FuseOSError, Operations, LoggingMixIn, fuse_exit

from .filesystem import SPECIAL_FILE, DagsHubFilesystem

SPECIAL_FILE_FH = (1<<64)-1

class DagsHubFUSE(LoggingMixIn, Operations):
    def __init__(self,
                 project_root: Optional[PathLike] = None,
                 repo_url: Optional[str] = None,
                 branch: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None):
        # FIXME TODO move autoconfiguration out of FUSE object constructor and to main method
        self.fs = DagsHubFilesystem(project_root=project_root, repo_url=repo_url, branch=branch, username=username, password=password)
        self.rwlock = Lock()
        self.mounted = False

    def init(self, path):
        self.mounted = True

    def destroy(self, path):
        self.mounted = False
        del self.fs

    def __call__(self, op, path, *args):
        return super(DagsHubFUSE, self).__call__(op, self.fs.project_root / path[1:], *args)

    def access(self, path, mode):
        try:
            self.fs.stat(path)
        except FileNotFoundError:
            return False

    def open(self, path, flags):
        if path == Path(self.fs.project_root / SPECIAL_FILE):
            return SPECIAL_FILE_FH
        self.fs.open(path).close()
        return os.open(path, flags, dir_fd=self.fs.project_root_fd)

    def getattr(self, path, fd=None):
        try:
            if fd:
                st = self.fs._DagsHubFilesystem__stat(fd)
            else:
                st = self.fs.stat(path)
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
            raise FuseOSError(errno.ENOENT)

    def read(self, path, size, offset, fh):
        if fh == SPECIAL_FILE_FH:
            return self.fs._special_file()[offset:offset+size]
        with self.rwlock:
            os.lseek(fh, offset, 0)
            return os.read(fh, size)

    def readdir(self, path, fh):
        return ['.', '..'] + self.fs.listdir(path)

    def release(self, path, fh):
        if fh != SPECIAL_FILE_FH: 
            return os.close(fh)

def mount(background: bool = True,
          project_root: Optional[PathLike] = None,
          repo_url: Optional[str] = None,
          branch: Optional[str] = None,
          username: Optional[str] = None,
          password: Optional[str] = None,
          _fuse: DagsHubFUSE = None,
          _register_exit_hook: bool = False):
    if _fuse is None:
        _fuse = DagsHubFUSE(project_root=project_root, repo_url=repo_url, branch=branch, username=username, password=password)
    if background:
        threading.Thread(target=mount, name="DagsHub FUSE daemon", daemon=True, kwargs={
                            "background": False,
                            "_fuse": _fuse,
                            "_register_exit_hook": True
                        }
                ).start()
        while not _fuse.mounted:
            sleep(0.1)
        os.chdir(Path().absolute())
    else:
        print(f'\n\nMounting DagsHubFUSE filesystem at {_fuse.fs.project_root}\nRun `cd .` in any existing terminals to utilize mounted FS.\n\n')
        if _register_exit_hook:
            atexit.register(fuse_exit)
        FUSE(_fuse, str(_fuse.fs.project_root), foreground=True, nonempty=True)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('project_root', nargs='?')
    parser.add_argument('--repo_url')
    parser.add_argument('--branch')
    parser.add_argument('--username')
    parser.add_argument('--password')

    args = parser.parse_args()
    mount(background=False, **vars(args))