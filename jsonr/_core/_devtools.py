import typing
import pydoc
import doctest
import unittest
import unittest.mock
import test
import test.support
import test.support.socket_helper
import test.support.script_helper
import test.support.bytecode_helper
import test.support.threading_helper
import test.support.os_helper
import test.support.import_helper
import test.support.warnings_helper

class DevTools:
    def __init__(self):
        self.typing: object = typing
        self.pydoc: object = pydoc
        self.doctest: object = doctest
        self.unittest: object = unittest
        self.unittest_mock: object = unittest.mock
        self.test: object = test
        self.test_support: object = test.support
        self.test_support_socket_helper: object = test.support.socket_helper
        self.test_support_script_helper: object = test.support.script_helper
        self.test_support_bytecode_helper: object = test.support.bytecode_helper
        self.test_support_threading_helper: object = test.support.threading_helper
        self.test_support_os_helper: object = test.support.os_helper
        self.test_support_import_helper: object = test.support.import_helper
        self.test_support_warnings_helper: object = test.support.warnings_helper
