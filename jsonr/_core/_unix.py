import sys
import pwd
import grp
import termios
import tty
import pty
import fcntl
import resource
import syslog

class Unix:
    def __init__(self):
        self.posix: object = posix
        self.pwd: object = pwd
        self.grp: object = grp
        self.termios: object = termios
        self.tty: object = tty
        self.pty: object = pty
        self.fcntl: object = fcntl
        self.resource: object = resource
        self.syslog: object = syslog
