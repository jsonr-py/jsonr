import bdb
import faulthandler
import pdb
import timeit
import trace
import tracemalloc

class Debug:
    def __init__(self):
        self.bdb: object = bdb
        self.faulthandler: object = faulthandler
        self.pdb: object = pdb
        self.timeit: object = timeit
        self.trace: object = trace
        self.tracemalloc: object = tracemalloc
