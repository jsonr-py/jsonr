'''
Create highly customizable JSON objects.

    - jsonr.New(auto=False, limit=None, *args, **kwargs)

Create a dataframe.
    - jsonr.Frame(columns=[], rows=[])

Run `help(jsonr.New)` or `help(jsonr.JSON)` for more information on json objects.


Run `help(jsonr.Frame)` for more information on dataframe objects.

Methods:
    - jsonr.load(file): Load binary file.
    - jsonr.dump(file): Dump binary file.
'''

from .core import New, Frame

JSON: New = New

PYTHON_MINIMUM_MAJOR: int = 3
PYTHON_MINIMUM_MINOR: int = 7
PYTHON_MINIMUM_MICRO: int = 0

import sys
import pickle

load:             object = pickle.load
dump:             object = pickle.dump

if sys.version_info < (PYTHON_MINIMUM_MAJOR, PYTHON_MINIMUM_MINOR, PYTHON_MINIMUM_MICRO):
    alert: str = f'\n\nPython {PYTHON_MINIMUM_MAJOR}.{PYTHON_MINIMUM_MINOR}.{PYTHON_MINIMUM_MICRO} or higher is required for {__name__}.\n\nCurrent Version: {str(sys.version).split("(")[0]}\n\n>>> Error Below:'
    import warnings
    warnings.warn(alert, stacklevel=2, category=RuntimeWarning)

__all__:          tuple = (
                        'load',
                        'dump',
                        'New',
                        'Frame',
                        'JSON',
                        'PYTHON_MINIMUM_MAJOR',
                        'PYTHON_MINIMUM_MINOR',
                        'PYTHON_MINIMUM_MICRO'
)

__version__:      str = '8.5.3'
__author__:       str = 'jsonr'
__author_email__: str = 'jsonr.py@gmail.com'
__license__:      str = 'MIT'
__copyright__:    str = 'Copyright (c) 2023 jsonr'
__credits__:      str = 'jsonr'
__maintainer__:   str = 'jsonr'
__email__:        str = 'jsonr.py@gmail.com'
__status__:       str = 'Development Status :: 3 - Alpha'
__topic__:        str = 'Topic :: Software Development :: Build Tools'
__license_type__: str = 'License :: OSI Approved :: MIT License'
__url__:          str = 'https://github.com/jsonr-py/jsonr'
__github__:       str = 'https://github.com/jsonr-py'
__repo__ :        str = 'https://github.com/jsonr-py/jsonr'
__keywords__:     str = 'jsonr json jsonr-py jsonr-python'
