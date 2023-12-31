'''
jsonr.utils

jsonr frontend

__all__: tuple = (
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
)
'''

from .._utils import (
    py_checker,
)
from .._utils._bond import (
    Bond,
)
from .._utils._convertions import (
    as_bytes,
    as_unicode,
)
from .._utils._infinity import (
    Infinity,
    NegativeInfinity,
)
from .._utils._inspect import (
    is_method,
    is_function,
    is_code,
    get_argspec,
)

__all__: tuple = (
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
)
