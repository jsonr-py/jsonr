import pathlib
import os.path
import fileinput
import stat
import filecmp
import tempfile
import glob
import fnmatch
import linecache
import shutil

class File:
    def __init__(self):
        self.pathlib: object = pathlib
        self.os_path: object = os.path
        self.fileinput: object = fileinput
        self.stat: object = stat
        self.filecmp: object = filecmp
        self.tempfile: object = tempfile
        self.glob: object = glob
        self.fnmatch: object = fnmatch
        self.linecache: object = linecache
        self.shutil: object = shutil
