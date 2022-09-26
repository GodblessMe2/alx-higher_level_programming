#!/usr/bin/python3
"""print the list of available attribute"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
