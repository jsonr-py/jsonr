'''
from .jsonr_typing_flowa import (
    Flowa,
    FlowaArray,
    FlowaObject,
    FlowaValue
)
'''

class Flowa(str):
    def __class_getitem__(cls, item: str) -> str:
        return item

class FlowaArray(list):
    def __class_getitem__(cls, item: str) -> str:
        return item

class FlowaObject(object):
    def __class_getitem__(cls, item: str) -> str:
        return item

class FlowaValue(object):
    def __class_getitem__(cls, item: str) -> str:
        return item
