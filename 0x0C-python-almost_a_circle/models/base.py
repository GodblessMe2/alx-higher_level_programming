#!/usr/bin/python3
"""Define the class Base"""
import csv
import json
import turtle


class Base:
    """Represents a base
       Attributes:
       __self (int): size of a size of the base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the base
        Args:
            size(int): size of a side of the base
            Return: None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
