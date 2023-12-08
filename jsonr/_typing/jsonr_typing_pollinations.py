'''
from .jsonr_typing_pollinations import (
    Image,
    ImageStr,
    ImageObject,
    ImageUrl,
    Text,
    TextArray,
    TextObject,
    TextValue
)
'''

class Image(object):
    def __class_getitem__(cls, item: str) -> str:
        return item

class ImageStr(str):
    def __class_getitem__(cls, item: str) -> str:
        return item

class ImageObject(object):
    def __class_getitem__(cls, item: str) -> str:
        return item

class ImageUrl(str):
    def __class_getitem__(cls, item: str) -> str:
        return item

class Text(str):
    def __class_getitem__(cls, item: str) -> str:
        return item

class TextArray(list):
    def __class_getitem__(cls, item: str) -> str:
        return item

class TextObject(object):
    def __class_getitem__(cls, item: str) -> str:
        return item

class TextValue(object):
    def __class_getitem__(cls, item: str) -> str:
        return item
