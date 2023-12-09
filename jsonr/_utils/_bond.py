class Bond(object):
    '''
    Tie, untie, group, and filter bonds and pairs.

    Parameters:
        size (int): The maximum size of the bond. If None, the bond will not be limited.

    Attributes:
        size (int): The maximum size of the bond. If None, the bond will not be limited.
        memory (list): A list of tuples that represent the bond.
        unique_pairs (set): A set of tuples that represent the unique pairs in the bond.

    Methods:
        tie(object_1, object_2): Tie two objects together.
        untie(object_1, object_2): Untie two objects from each other.
        filter(object): Filter the bond by the given object.
        groups(): Return the bond.
        is_same(object_1, object_2): Check if two objects are the tied.

    '''
    def __init__(self, size=None, *args, **kwargs) -> None:
        self.size:         int  = size
        self.memory:       list = []
        self.unique_pairs: set  = set()

    def __repr__(self, *args, **kwargs) -> str:
        return str(self.memory)

    def __str__(self, *args, **kwargs) -> str:
        return str(self.memory)

    def __class_getitem__(self, item: object, *args, **kwargs) -> object:
        return object

    def filter(self, object_1, *args, **kwargs) -> list:
        filtered = [entry for entry in self.memory if object_1 in entry]
        return filtered

    def tie(self, object_1, object_2, *args, **kwargs) -> list:
        new_entry = (object_1, object_2)
        if self.size is not None and len(self.memory) >= self.size:
            oldest_entry: tuple = self.memory.pop(0)
            self.unique_pairs.discard(oldest_entry)
        self.memory.append(new_entry)
        self.unique_pairs.add(new_entry)
        return self.memory

    def untie(self, object_1, object_2, *args, **kwargs) -> list:
        self.memory: list = [entry for entry in self.memory if entry != (object_1, object_2) and entry != (object_2, object_1)]
        self.unique_pairs.discard((object_1, object_2))
        self.unique_pairs.discard((object_2, object_1))
        return self.memory

    def is_same(self, object_1, object_2, *args, **kwargs) -> bool:
        return (object_1, object_2) in self.unique_pairs or (object_2, object_1) in self.unique_pairs

    def groups(self, *args, **kwargs) -> list:
        return self.memory
