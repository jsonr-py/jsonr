'''
from .jsonr_typing_json import (
    JSON,
    JSONArray,
    JSONObject,
    JSONValue
)
'''

class JSONArray(list):
    def __class_getitem__(cls, item: str) -> str:
        return item

class JSONObject(object):
    def __class_getitem__(cls, item: str) -> str:
        return item

class JSONValue(object):
    def __class_getitem__(cls, item: str) -> str:
        return item
