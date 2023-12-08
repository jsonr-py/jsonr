'''
jsonr._utils

jsor.utils backend
'''

import sys
import warnings

def py_checker(PYTHON_MINIMUM_MAJOR, PYTHON_MINIMUM_MINOR, PYTHON_MINIMUM_MICRO):
    if sys.version_info < (PYTHON_MINIMUM_MAJOR, PYTHON_MINIMUM_MINOR, PYTHON_MINIMUM_MICRO):
        alert: str = f'\n\nPython {PYTHON_MINIMUM_MAJOR}.{PYTHON_MINIMUM_MINOR}.{PYTHON_MINIMUM_MICRO} or higher is required for jsonr.\n\nCurrent Version: {str(sys.version).split("(")[0]}\n\n>>> Error Below:'
        warnings.warn(alert, stacklevel=2, category=RuntimeWarning)
    return (PYTHON_MINIMUM_MAJOR, PYTHON_MINIMUM_MINOR, PYTHON_MINIMUM_MICRO)
