#!/usr/bin/python3
"""Define the class Rectangle"""


class Rectangle:
    """Represents a rectangle
    Attributes:
        _width (int): width of the new rectangle
        _height (int): The height of the new rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an integer of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __init__(self, width=0, height=0):
        """Initializing the rectangle
        Args:
           width (int): width of a side of the new rectangle
           height (int): height of a side of the new rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Prints a string when an instance has been deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Return the current width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """Return printable string representative of the rectangle"""
        string = ""
        if self.__width != 0 and self.height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.height))
        return string

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
