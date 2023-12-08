import zlib
import gzip
import bz2
import lzma
import zipfile
import tarfile

class dCompression:
    def __init__(self):
        self.zib: object = zlib
        self.gzip: object = gzip
        self.bz2: object = bz2
        self.lzma: object = lzma
        self.zipfile: object = zipfile
        self.tarfile: object = tarfile
