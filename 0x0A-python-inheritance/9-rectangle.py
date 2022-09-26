#!/usr/bin/python3
"""Import the Base Geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """Initializing the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return (self.__height * self.__width)

    def __str__(self):
        """Return printable string representative of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
