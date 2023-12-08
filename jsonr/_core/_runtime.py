import sys
import sys.monitoring
import sysconfig
import builtins
import __main__
import warnings
import dataclasses
import contextlib
import abc
import atexit
import traceback
import __future__
import gc
import inspect
import site

class Runtime:
    def __init__(self):
        self.sys: object = sys
        self.sys_monitoring: object = sys.monitoring
        self.sysconfig: object = sysconfig
        self.builtins: object = builtins
        self.__main__: object = __main__
        self.warnings: object = warnings
        self.dataclasses: object = dataclasses
        self.contextlib: object = contextlib
        self.abc: object = abc
        self.atexit: object = atexit
        self.traceback: object = traceback
        self.__future__: object = __future__
        self.gc: object = gc
        self.inspect: object = inspect
        self.site: object = site
