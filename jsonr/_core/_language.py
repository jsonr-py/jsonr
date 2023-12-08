import ast
import symtable
import token
import keyword
import tokenize
import tabnanny
import pyclbr
import py_compile
import compileall
import dis
import pickletools

class Language:
    def __init__(self):
        self.ast: object = ast
        self.symtable: object = symtable
        self.token: object = token
        self.keyword: object = keyword
        self.tokenize: object = tokenize
        self.tabnanny: object = tabnanny
        self.pyclbr: object = pyclbr
        self.py_compile: object = py_compile
        self.compileall: object = compileall
        self.dis: object = dis
        self.pickletools: object = pickletools
