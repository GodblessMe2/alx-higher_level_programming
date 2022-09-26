#!/usr/bin/python3
"""Import the Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a rectangle"""
    def __init__(self, size):
        """Initializing the rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the rectangle"""
        return (self.__size ** 2)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
