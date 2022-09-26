#!/usr/bin/python3
"""
This module contains the function inherits_from
"""


def inherits_from(obj, a_class):
    """Return True if the object is an instance of the class
       that is been inherit(directly or indirectly)
    """
    return (type(obj) is not a_class)
