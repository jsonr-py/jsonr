import pickle
import copyreg
import shelve
import marshal
import dbm
import sqlite3

class Data:
    def __init__(self):
        self.pickle: object = pickle
        self.copyreg: object = copyreg
        self.shelve: object = shelve
        self.marshal: object = marshal
        self.dbm: object = dbm
        self.sqlite3: object = sqlite3
