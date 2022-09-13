#!/usr/bin/python3
import math

class MagicClass:
    """This representing a circle"""
    def __init__(self, radius=0):
        """Initializing the Magic Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius
    def area(self):
        """Calculates the area of the circle"""
        return (self.__radius **2) * math.pi
    def circum(self):
        """Calculates the circum of the circle"""
        return 2 * math.pi * self.__radius
