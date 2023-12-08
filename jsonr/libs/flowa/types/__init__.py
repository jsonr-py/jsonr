"""
flowa.types

Classes:
  - Node: Represents a Node in a Decision Tree.
  - Map: Represents a Map in an Encoder.
  - Image: Represents an Image Object.
"""


class Node(object):
    """
    A Node class for the Flowa Decision Tree.

    Attributes:
      value: The value of the node.
      feature: The feature used to split the node.
      threshold: The threshold used to split the node.
      left: The left child of the node.
      right: The right child of the node.

    Methods:
      __init__: Constructs a Node object.
      __repr__: Returns the string representation of the node.
      __str__: Returns the string representation of the node.
      __call__: Returns the value of the node.

    Functions:
      is_leaf_node: Returns True if the node is a leaf node.
      children: Returns the children of the node.
    """

    def __init__(
        self,
        feature: int = None,
        threshold: float = None,
        left: object = None,
        right: object = None,
        *,
        value: float = None,
        **kwargs,
    ) -> None:
        """Constructs a Node object."""
        self.feature: int = feature
        self.threshold: float = threshold
        self.left: object = left
        self.right: object = right
        self.value: float = value

    def is_leaf_node(self, *args, **kwargs) -> bool:
        """Determines if node is a leaf node or not."""
        return self.value is not None

    def children(self, *args, **kwargs) -> tuple:
        """Returns left and right children of the node."""
        return (self.left, self.right)

    def __repr__(self, *args, **kwargs) -> str:
        """Returns the string representation of the node.""" ""
        return f"Node(feature={self.feature}, threshold={self.threshold}, left={self.left}, right={self.right}, value={self.value})"

    def __call__(self, *args, **kwargs) -> float:
        """Returns the value of the node.""" ""
        return self.value

    def __str__(self, *args, **kwargs) -> str:
        """Returns the string representation of the node."""
        return self.__repr__()


class Map(object):
    """
    A Map class for the Flowa Decision Tree.

    Attributes:
      labels: The map of the label encoder.

    Methods:
      __init__: Constructs a Map object.
      __repr__: Returns the string representation of the map.
      __str__: Returns the string representation of the map.
      __call__: Returns the value of the map.
    """

    def __init__(self, map: dict, *args, **kwargs) -> None:
        """Constructs a Map object."""
        self.labels: dict = map
        for label, value in map.items():
            setattr(self, label, value)

    def __repr__(self, *args, **kwargs) -> str:
        """Returns the string representation of the map."""
        return f"Map(maplen={len(self.labels)})"

    def __str__(self, *args, **kwargs) -> str:
        """Returns the string representation of the map."""
        return self.__repr__()

    def __call__(self, *args, **kwargs) -> dict:
        """Returns the value of the map."""
        return self.labels


class Image:
    """
    A class for storing image data.

    Attibutes:
      prompt: The prompt used to generate the image.
      url: The URL of the image.
      model: The model used to generate the image.
      width: The width of the image.
      height: The height of the image.
      seed: The seed used to generate the image.
      logo: Whether or not to include the logo in the image.
      content: The content of the image.

    Methods:
      __init__: Constructs an Image object.
      __repr__: Returns the string representation of the image.
      save(path): Saves the image to a file.
    """

    def __init__(
        self,
        prompt: str,
        url: str,
        model: str,
        height: str,
        width: str,
        seed: str,
        logo: str,
        content: str,
    ):
        """Constructs an Image object."""
        self.prompt: str = prompt
        self.url: str = url
        self.model: str = model
        self.height: int = height
        self.width: int = width
        self.seed: int = seed
        self.logo: bool = logo
        self.content: str = content

    def __repr__(self, *args, **kwargs) -> str:
        """Returns the string representation of the image."""
        return f"Image(prompt={self.prompt}, model={self.model}, height={self.height}, width={self.width}, seed={self.seed}, logo={self.logo}, url={self.url}, content={self.content[:10]}...)"

    def save(self, path: str, *args, **kwargs) -> None:
        """Saves the image to a file."""
        with open(path, "wb") as file:
            file.write(self.content)
        return self
