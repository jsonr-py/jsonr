'''
Create highly customizable JSON objects.

    - jsonr.New(auto=False, limit=None, *args, **kwargs)

Run `help(jsonr.New)` or `help(jsonr.JSON)` for more information.
'''

from .core import New

JSON: New = New

PYTHON_MINIMUM_MAJOR: int = 3
PYTHON_MINIMUM_MINOR: int = 7
PYTHON_MINIMUM_MICRO: int = 0

import sys

if sys.version_info < (PYTHON_MINIMUM_MAJOR, PYTHON_MINIMUM_MINOR, PYTHON_MINIMUM_MICRO):
    alert: str = f'\n\nPython {PYTHON_MINIMUM_MAJOR}.{PYTHON_MINIMUM_MINOR}.{PYTHON_MINIMUM_MICRO} or higher is required for {__name__}.\n\nCurrent Version: {str(sys.version).split("(")[0]}\n\n>>> Error Below:'
    import warnings
    warnings.warn(alert, stacklevel=2, category=RuntimeWarning)
