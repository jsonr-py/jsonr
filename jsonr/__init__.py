'''
Highly customizable JSON objects and dataframes, and your python toolkit all in one.

__all__:          tuple = (
                        'New',
                        'Frame',
                        'load',
                        'dump',
                        'py_checker',
                        'as_bytes',
                        'as_unicode',
                        'is_method',
                        'is_function',
                        'is_code',
                        'get_argspec',
                        'Bond',
                        'Infinity',
                        'NegativeInfinity',
                        'PYTHON_MINIMUM_MAJOR',
                        'PYTHON_MINIMUM_MINOR',
                        'PYTHON_MINIMUM_MICRO',
                        'JSON',
                        'JSONArray',
                        'JSONObject',
                        'JSONValue',
                        'Flowa',
                        'FlowaArray',
                        'FlowaObject',
                        'FlowaValue',
                        'Image',
                        'ImageStr',
                        'ImageObject',
                        'ImageUrl',
                        'Text',
                        'TextArray',
                        'TextObject',
                        'TextValue',
                        'Any',
                        'Callable',
                        'Dict',
                        'List',
                        'Optional',
                        'Tuple',
                        'Type',
                        'Union',
                        'cast',
                        'overload',
                        'String',
                        'StringBuffer',
)
'''

import json
import pickle

from . import core
from .core import New, Frame

from . import utils
from .utils import (
    py_checker,
    as_bytes,
    as_unicode,
    is_method,
    is_function,
    is_code,
    get_argspec,
    Bond,
    Infinity,
    NegativeInfinity,
)

from . import typing
from .typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple,
    Type,
    Union,
    cast,
    overload,
    String,
    StringBuffer,
    JSONArray,
    JSONObject,
    JSONValue,
    Flowa,
    FlowaArray,
    FlowaObject,
    FlowaValue,
    Image,
    ImageStr,
    ImageObject,
    ImageUrl,
    Text,
    TextArray,
    TextObject,
    TextValue
)

JSON: New = New

PYTHON_MINIMUM_MAJOR: int = 3
PYTHON_MINIMUM_MINOR: int = 7
PYTHON_MINIMUM_MICRO: int = 0

load:             object = pickle.load
dump:             object = pickle.dump

py_checker(PYTHON_MINIMUM_MAJOR, PYTHON_MINIMUM_MINOR, PYTHON_MINIMUM_MICRO)

__all__:          tuple = (
                        'New',
                        'Frame',
                        'load',
                        'dump',
                        'py_checker',
                        'as_bytes',
                        'as_unicode',
                        'is_method',
                        'is_function',
                        'is_code',
                        'get_argspec',
                        'Infinity',
                        'NegativeInfinity',
                        'PYTHON_MINIMUM_MAJOR',
                        'PYTHON_MINIMUM_MINOR',
                        'PYTHON_MINIMUM_MICRO',
                        'JSON',
                        'JSONArray',
                        'JSONObject',
                        'JSONValue',
                        'Flowa',
                        'FlowaArray',
                        'FlowaObject',
                        'FlowaValue',
                        'Image',
                        'ImageStr',
                        'ImageObject',
                        'ImageUrl',
                        'Text',
                        'TextArray',
                        'TextObject',
                        'TextValue',
                        'Any',
                        'Callable',
                        'Dict',
                        'List',
                        'Optional',
                        'Tuple',
                        'Type',
                        'Union',
                        'cast',
                        'overload',
                        'String',
                        'StringBuffer',
)

__version__:      str = '8.6.2'
__description__:  str = 'Highly customizable JSON objects and dataframes, and your python toolkit all in one.'
__desc__:         str = 'Highly customizable JSON objects and dataframes, and your python toolkit all in one.'
__author__:       str = 'jsonr'
__author_email__: str = 'jsonr.py@gmail.com'
__license__:      str = 'MIT'
__copyright__:    str = 'Copyright (c) 2023 jsonr'
__credits__:      str = 'jsonr'
__maintainer__:   str = 'jsonr'
__email__:        str = 'jsonr.py@gmail.com'
__status__:       str = 'Development Status :: 5 - Production/Stable'
__topic__:        str = 'Topic :: Software Development :: Build Tools'
__license_type__: str = 'License :: OSI Approved :: MIT License'
__url__:          str = 'https://github.com/jsonr-py/jsonr'
__github__:       str = 'https://github.com/jsonr-py'
__repo__ :        str = 'https://github.com/jsonr-py/jsonr'
__keywords__:     str = 'jsonr json jsonr-py jsonr-python, python'
