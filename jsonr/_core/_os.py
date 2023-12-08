import os
import io
import time
import argparse
import getopt
import logging
import logging.config
import logging.handlers
import getpass
import curses
import curses.textpad
import curses.ascii
import curses.panel
import platform
import errno
import ctypes

class OperatingSystem:
    def __init__(self):
        self.os: object = os
        self.io: object = io
        self.time: object = time
        self.argparse: object = argparse
        self.getopt: object = getopt
        self.logging: object = logging
        self.logging_config: object = logging.config
        self.logging_handlers: object = logging.handlers
        self.getpass: object = getpass
        self.curses: object = curses
        self.curses_textpad: object = curses.textpad
        self.curses_ascii: object = curses.ascii
        self.curses_panel: object = curses.panel
        self.platform: object = platform
        self.errno: object = errno
        self.ctypes: object = ctypes
