#!/usr/bin/python3
"""Define the class Rectangle"""


class Rectangle:
    """Represents a rectangle
    Attributes:
        _width (int): width of the new rectangle
        _height (int): The height of the new rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializing the rectangle
        Args:
           width (int): width of a side of the new rectangle
           height (int): height of a side of the new rectangle
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Return the current width of the rectangle"""
        return (self.__width)
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the current height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Return the area of the rectangle"""
        return (self.height * self.width)
    
    def perimeter(self):
        return (self.height + self.width + self.height + self.width)
    def __str__(self):
        """Return printable string representative of the rectangle"""
        string = ""
        if self.__width != 0 and self.height != 0:
            string += "\n".join('#' * self.__width
                                for j in range(self.height))
        return string