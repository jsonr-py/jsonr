import json
from ..bases import NewBase


class New(NewBase):
    """
    Create highly customizable JSON objects.

    Parameters:
        auto (bool): Whether to automatically save all json keys to class variables.
        limit (int): The maximum number of keys to save to the json object.
        **kwargs: Additional keyword arguments to pass to the json object.

    Methods:
        __init__ (auto=True, *args, limit=None, **kwargs): Initialize the json object.

        save (file, indent=0): Save json object to file.
        load (file): Load json object from file.

        auto (enabled=True): Change whether to automatically save all json keys to class variables.

        copy (): Copy json object.
        to (copy): Copy json object from another json object.

        add (key, value): Add new key to json object.
        remove (key): Remove key from json object. # Also delete()
        update (**kwargs): All keys and values in kwargs will be added or updated to json object.

        wipe (): Wipe all keys from json object.
        new (): Create a new json object.

        search (key, value): Search for a key in json object.
        get (key, default=None): Get value of key in json object.

    """
    def __init__(self, auto: bool=False, *args, limit: int=None, **kwargs) -> None:
        """Initialize the json object."""
        super().__init__(auto=auto, limit=limit, *args, **kwargs)

    def save(self, file: str, indent: int = 0, *args, **kwargs) -> NewBase:
        """Save json object to file."""
        with open(file, "w") as f:
            json.dump(self._NewBase_json_secret_var_jsonr_python, f, indent=indent, *args, **kwargs)
        return self

    def load(self, file: str, *args, **kwargs) -> NewBase:
        """Load json object from file."""
        with open(file, "r") as f:
            self._NewBase_json_secret_var_jsonr_python = json.load(f, *args, **kwargs)
            self._trim()


        if self._NewBase_auto_unique_secret_var_jsonr_python:
            for key, value in self._NewBase_json_secret_var_jsonr_python.items():
                setattr(self, key, value)
        return self

    def copy(self, *args, **kwargs) -> NewBase[dict]:
        """Copy json object."""
        return self._NewBase_json_secret_var_jsonr_python.copy()

    def to(self, copy: dict, *args, **kwargs) -> NewBase:
        """Copy json object from another json object."""
        self._NewBase_json_secret_var_jsonr_python = copy
        self._trim()

        if self._NewBase_auto_unique_secret_var_jsonr_python:
            for key, value in self._NewBase_json_secret_var_jsonr_python.items():
                setattr(self, key, value)
        return self

    def add(self, keyword: str, value: object, *args, unique: str = None, **kwargs) -> NewBase:
        """Add new key to json object."""
        if unique:
            setattr(self, unique, value)
        if self._NewBase_auto_unique_secret_var_jsonr_python:
            setattr(self, keyword, value)

        self._NewBase_json_secret_var_jsonr_python[keyword] = value
        return self

    def remove(self, keyword: str, *args, **kwargs) -> NewBase:
        """Remove key from json object."""
        self.delete(keyword)
        return self

    def wipe(self, *args, **kwargs) -> NewBase:
        """Wipe all keys from json object."""
        self._NewBase_json_secret_var_jsonr_python = {}
        return self

    def new(self, auto: bool=False, limit: int=None, *args, **kwargs) -> NewBase[None]:
        return super().__init__(auto=auto, limit=limit, *args, **kwargs)

    def search(self, *args, keyword: str = None, value: str = None, **kwargs) -> NewBase[object]:
        """Search for a key in json object."""
        if keyword and value:
            return self._NewBase_json_secret_var_jsonr_python[keyword] == value
        elif keyword:
            return self._NewBase_json_secret_var_jsonr_python[keyword]
        elif value:
            return value in self._NewBase_json_secret_var_jsonr_python.values()
        else:
            return self._NewBase_json_secret_var_jsonr_python

    def get(self, keyword: str, *args, default: object=None, **kwargs) -> NewBase[object]:
        """Get value of key in json object."""
        return self._NewBase_json_secret_var_jsonr_python.get(keyword, default)

    def delete(self, keyword: str, *args, **kwargs) -> NewBase:
        """Delete key from json object."""
        try:
            delattr(self, keyword)
            del self._NewBase_json_secret_var_jsonr_python[keyword]
        except:
            pass
        return self

    def update(self, **kwargs) -> NewBase:
        """All keys and values in kwargs will be added or updated to json object."""
        for keyword, value in kwargs.items():
            self._NewBase_json_secret_var_jsonr_python[keyword] = value
            if self._NewBase_auto_unique_secret_var_jsonr_python: setattr(self, keyword, value)
        return self

