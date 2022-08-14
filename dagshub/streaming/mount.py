#!/usr/bin/env python
from __future__ import print_function, absolute_import, division

import logging
import os
from os import PathLike

from errno import EACCES
from threading import Lock

from fuse import FUSE, FuseOSError, Operations, LoggingMixIn
from typing import Optional, TypeVar 
from pathlib import Path
import requests
import json

T = TypeVar('T')

class Loopback(LoggingMixIn, Operations):
    def __init__(self, url: str, 
            mount: Optional[str] = None,
            username: Optional[str] = None,
            password: Optional[str] = None):
        self.url = url
        self.rwlock = Lock()
        self.auth = (username, password) if username or password else None
        del username, password

        # setup mountpoint
        if mount:
            self.mount = mount
        else:
            self.mount = os.path.join(str(Path.home()), '.dagshub', url.split('/')[4].split('.')[0])

    def __call__(self, op, path, *args):
        return super(Loopback, self).__call__(op, self.url + path, *args)

    def access(self, path, mode):
        if not os.access(path, mode):
            raise FuseOSError(EACCES)

    chmod = os.chmod
    chown = os.chown

    def create(self, path, mode):
        return os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, mode)

    def flush(self, path, fh):
        return os.fsync(fh)

    def fsync(self, path, datasync, fh):
        if datasync != 0:
            return os.fdatasync(fh)
        else:
            return os.fsync(fh)

    def getattr(self, path, fh=None):
        st = self.stat(path)
        return dict((key, getattr(st, key)) for key in (
            'st_atime', 'st_ctime', 'st_gid', 'st_mode', 'st_mtime',
            'st_nlink', 'st_size', 'st_uid'))

    getxattr = None

    def link(self, target, source):
        return os.link(self.url + source, target)

    def _list_files(self, url):
        return [file['path'] for file in requests.get(url).json()]

    listxattr = None
    mkdir = os.mkdir
    mknod = os.mknod
    # open = os.open

    @classmethod
    def __get_unpatched(cls, key, alt: T) -> T:
        if hasattr(cls, f'_{cls.__name__}__unpatched'):
            return cls.__unpatched[key]
        else:
            return alt

    @classmethod
    @property
    def __stat(cls):
        return cls.__get_unpatched('stat', os.stat)

    def open(self, file: PathLike, mode: str = 'r', *args, **kwargs):
        try:
            return self.__open(file, mode, *args, **kwargs)
        except FileNotFoundError as e:
            print('JINEN DEBUG:: OPEN')
            relative_path = self._relative_path(file)
            if relative_path:
                resp = requests.get(f'{self.raw_api_url}/{relative_path}', auth=self.auth)
                if resp.ok:
                    Path(file).absolute().parent.mkdir(parents=True, exist_ok=True)
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

    def _relative_path(self, file: PathLike):
        print("DEBUG JINEN", file)
        path = Path(file).absolute()
        print("DEBUG JINEN", path)
        if path.is_relative_to(self.project_root.absolute()):
            return path.relative_to(self.project_root.absolute())
        else:
            return None

    def stat(self, path: PathLike, *, dir_fd=None, follow_symlinks=True):
        if dir_fd is not None or not follow_symlinks:
            raise NotImplementedError('DagsHub\'s patched stat() does not support additional arguments')
        try:
            return self.__stat(path)
        except FileNotFoundError as e:
            print('JINEN DEBUG:: STAT')
            relative_path = self._relative_path(path)
            if relative_path:
                # TODO: check single file content API instead of directory when it becomes available
                # TODO: use DVC remote cache to download file now that we have the directory json
                resp = requests.get(f'{self.content_api_url}/{relative_path.parent}', auth=self.auth)
                if resp.ok:
                    json = resp.json()
                    matches = [info for info in json if Path(info['path']) == relative_path]
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

    def read(self, path, size, offset, fh):
        with self.rwlock:
            os.lseek(fh, offset, 0)
            return os.read(fh, size)

    def readdir(self, path, fh):
        print(path, fh)
        return ['.', '..'] + self._list_files('https://dagshub.com/api/v1/repos/nirbarazida/chexnet/content/master/') # path

    readlink = os.readlink

    def release(self, path, fh):
        return os.close(fh)

    def rename(self, old, new):
        return os.rename(old, self.url + new)

    rmdir = os.rmdir

    def statfs(self, path):
        stv = os.statvfs(path)
        return dict((key, getattr(stv, key)) for key in (
            'f_bavail', 'f_bfree', 'f_blocks', 'f_bsize', 'f_favail',
            'f_ffree', 'f_files', 'f_flag', 'f_frsize', 'f_namemax'))

    def symlink(self, target, source):
        return os.symlink(source, target)

    def truncate(self, path, length, fh=None):
        with open(path, 'r+') as f:
            f.truncate(length)

    unlink = os.unlink
    utimens = os.utime

    def write(self, path, data, offset, fh):
        with self.rwlock:
            os.lseek(fh, offset, 0)
            return os.write(fh, data)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('root')
    parser.add_argument('mount')
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)
    fuse = FUSE(
        Loopback(args.root), args.mount, foreground=True, allow_other=True)
