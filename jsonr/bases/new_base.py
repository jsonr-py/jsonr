_NewBase_banned_keywords_secret_var_jsonr_python: list = [
    "_NewBase_json_secret_var_jsonr_python",
    "_NewBase_args_secret_var_jsonr_python",
    "_NewBase_kwargs_secret_var_jsonr_python",
    "_NewBase_auto_unique_secret_var_jsonr_python",
    "_NewBase_limit_secret_var_jsonr_python",
]


class NewBase(object):
    def __init__(self, auto: bool = False, limit: int = None, *args, **kwargs) -> None:
        if auto: (setattr(self, key, value) for key, value in kwargs.items() if key not in _NewBase_banned_keywords_secret_var_)

        self._NewBase_json_secret_var_jsonr_python: dict = {**kwargs}
        self._NewBase_args_secret_var_jsonr_python: tuple = args
        self._NewBase_kwargs_secret_var_jsonr_python: tuple = kwargs

        self._NewBase_auto_unique_secret_var_jsonr_python: bool = auto
        self._NewBase_limit_secret_var_jsonr_python: int = limit

    def _trim(self) -> dict:
        if self._NewBase_limit_secret_var_jsonr_python is not None:
            self._NewBase_json_secret_var_jsonr_python: dict = dict(
                list(self._NewBase_json_secret_var_jsonr_python.items())[
                    : self._NewBase_limit_secret_var_jsonr_python
                ]
            )
        return self._NewBase_json_secret_var_jsonr_python

    def __setattr__(self, name, value) -> None:
        super().__setattr__(name, value)
        if name not in _NewBase_banned_keywords_secret_var_jsonr_python:
            self._NewBase_json_secret_var_jsonr_python[name] = value

    def __delattr__(self, name) -> None:
        super().__delattr__(name)
        if name not in _NewBase_banned_keywords_secret_var_jsonr_python:
            del self._NewBase_json_secret_var_jsonr_python[name]

    def __getattr__(self, name) -> object:
        return super().__getattr__(name)

    def __class_getitem__(cls, item) -> object:
        return item

    def __repr__(self) -> object:
        return self._NewBase_json_secret_var_jsonr_python

    def __len__(self) -> int:
        return len(self._NewBase_json_secret_var_jsonr_python)

    def __getitem__(self, key) -> object:
        return self._NewBase_json_secret_var_jsonr_python[key]

    def __setitem__(self, key, value) -> None:
        self._NewBase_json_secret_var_jsonr_python[key] = value
        if self._NewBase_auto_unique_secret_var_jsonr_python:
            setattr(self, key, value)

        self._trim()

    def __delitem__(self, key) -> None:
        del self._NewBase_json_secret_var_jsonr_python[key]

    def __contains__(self, key) -> object:
        return key in self._NewBase_json_secret_var_jsonr_python

    def __iter__(self) -> object:
        return iter(self._NewBase_json_secret_var_jsonr_python)

    def __reversed__(self) -> object:
        return reversed(self._NewBase_json_secret_var_jsonr_python)

    def __eq__(self, other) -> bool:
        return self._NewBase_json_secret_var_jsonr_python == other

    def __ne__(self, other) -> bool:
        return self._NewBase_json_secret_var_jsonr_python != other

    def __lt__(self, other) -> bool:
        return len(self._NewBase_json_secret_var_jsonr_python) < other

    def __le__(self, other) -> bool:
        return len(self._NewBase_json_secret_var_jsonr_python) <= other

    def __gt__(self, other) -> bool:
        return len(self._NewBase_json_secret_var_jsonr_python) > other

    def __ge__(self, other) -> bool:
        return len(self._NewBase_json_secret_var_jsonr_python) >= other

    def __add__(self, other) -> object:
        if self._NewBase_auto_unique_secret_var_jsonr_python:
            try:
                self._NewBase_json_secret_var_jsonr_python: dict = {
                    **self._NewBase_json_secret_var_jsonr_python,
                    **other,
                }
                self._trim()

                for key, value in other.items():
                    setattr(self, key, value)
            except:
                return self.__len__() + other
        return self._NewBase_json_secret_var_jsonr_python

    def __iadd__(self, other) -> object:
        return self.__add__()

    def __sub__(self, other) -> object:
        try:
            for key in other:
                del self._NewBase_json_secret_var_jsonr_python[key]
        except:
            return self.__len__() - other
        return self._NewBase_json_secret_var_jsonr_python

    def __isub__(self, other) -> object:
        return self.__sub__()

    def __mul__(self, other) -> object:
        try:
            self._NewBase_json_secret_var_jsonr_python: dict = {
                **self._NewBase_json_secret_var_jsonr_python,
                **other,
            }
            self._trim()

            for key, value in other.items():
                setattr(self, key, value)
        except:
            return self.__len__() * other
        return self._NewBase_json_secret_var_jsonr_python

    def __imul__(self, other) -> object:
        return self.__mul__()

    def __truediv__(self, other) -> object:
        try:
            for key, value in other.items():
                del (self, key, value)
        except:
            return self.__len__() / other
        return self._NewBase_json_secret_var_jsonr_python

    def __itruediv__(self, other) -> object:
        return self.__truediv__()

    def __floordiv__(self, other) -> object:
        try:
            self._NewBase_json_secret_var_jsonr_python: dict = {
                **self._NewBase_json_secret_var_jsonr_python,
                **other,
            }
            self._trim()

            for key, value in other.items():
                delattr(self, key, value)
        except:
            return self.__len__() // other
        return self._NewBase_json_secret_var_jsonr_python

    def __ifloordiv__(self, other) -> object:
        return self.__floordiv__()

    def __mod__(self, other) -> object:
        try:
            self._NewBase_json_secret_var_jsonr_python: dict = {
                **self._NewBase_json_secret_var_jsonr_python,
                **other,
            }
            self._trim()

            for key, value in other.items():
                delattr(self, key, value)
        except:
            return self.__len__() % int(other)
        return self._NewBase_json_secret_var_jsonr_python

    def __imod__(self, other) -> object:
        return self.__mod__()

    def __pow__(self, other) -> object:
        try:
            self._NewBase_json_secret_var_jsonr_python: dict = {
                **self._NewBase_json_secret_var_jsonr_python,
                **other,
            }
            self._trim()

            for key, value in other.items():
                setattr(self, key, value)
        except:
            return self.__len__() ** int(other)
        return self._NewBase_json_secret_var_jsonr_python

    def __ipow__(self, other) -> object:
        return self.__pow__()

    def __lshift__(self, other) -> int:
        return self.__len__() << other

    def __ilshift__(self, other) -> int:
        return self.__len__() << other

    def __rshift__(self, other) -> int:
        return self.__len__() >> other

    def __irshift__(self, other) -> int:
        return self.__len__() >> other

    def __and__(self, other) -> int:
        return self.__len__() & other

    def __iand__(self, other) -> int:
        return self.__len__() & other

    def __xor__(self, other) -> int:
        return self.__len__() ^ other

    def __ixor__(self, other) -> int:
        return self.__len__() ^ other

    def __or__(self, other) -> object:
        return self.__len__() | other

    def __ior__(self, other) -> object:
        return self.__len__() | other

    def __neg__(self) -> int:
        return -self.__len__()

    def __pos__(self) -> int:
        return +self.__len__()

    def __abs__(self) -> int:
        return abs(self.__len__())

    def __invert__(self) -> int:
        return ~self.__len__()

    def __str__(self) -> str:
        return str(self.__repr__())

    def __int__(self) -> int:
        return int(self.__len__())

    def __float__(self) -> float:
        return float(self.__len__())

    def __complex__(self) -> complex:
        return complex(self.__len__())

    def __round__(self) -> int:
        return round(self.__len__())

    def __trunc__(self) -> object:
        return trunc(self.__len__())

    def __floor__(self) -> object:
        return floor(self.__len__())

    def __ceil__(self) -> object:
        return ceil(self.__len__())

    def __call__(self, *args, **kwargs) -> object:
        return self

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> str:
        return f"jsonr.exit <exc_type: {exc_type}, exc_value: {exc_value}, traceback: {traceback}>"
