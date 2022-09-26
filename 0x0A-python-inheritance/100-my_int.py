#!/usr/bin/python3
"""Define the class MyInt"""
from distutils.dir_util import remove_tree


class MyInt(int):
    """This method gets called when using != on the object"""
    def __eq__(self, other):
        """Return != is now"""
        return int(self) != other

    """This method gets called when using == on the object"""
    def __ne__(self, other):
        """Return == is now"""
        return int(self) == other
