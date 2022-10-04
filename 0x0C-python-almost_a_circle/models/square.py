#!/usr/bin/python3
"""Define the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A representation of a class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialise a class Square
        Args:
            side (int): The side of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the current size size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return printable string representative of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs):
            for k, m in kwargs.items():
                if k == "id":
                    if m is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = m
                elif k == "size":
                    self.size = m
                elif k == "x":
                    self.x = m
                elif k == "y":
                    self.y = m

    def to_dictionary(self):
        """Return the dictionary representation of a square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
