#!/usr/bin/python3
"""Define the a function that attributes to object"""


def add_attribute(obj, att, value):
    """Add a new attributes to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
