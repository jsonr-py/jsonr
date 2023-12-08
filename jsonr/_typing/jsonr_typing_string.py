'''
from .jsonr_typing_string import (
    String,
    StringBuffer
)
'''

class String(str):
    def __class_getitem__(cls, item: str) -> str:
        return item

class StringBuffer:
    def __init__(self, size: int = 0) -> None:
        self.size: int = size
        self.buffer: str = ''

    def __str__(self) -> str:
        return self.__repr__()

    def __int__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "".join(self.buffer)

    def __call__(self, value: str) -> object:
        if isinstance(value, int):
            self.remove(value)
        else:
            self.add(value)

        return self

    def add(self, value: str) -> object:
        self.buffer: str = f'{self.buffer}{value}'[:self.size]
        return self

    def remove(self, value: str) -> object:
        self.buffer: str = f'{self.buffer[:value]}'
        return self
