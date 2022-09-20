#!/usr/bin/python3
"""Define the class LockedClass"""


class LockedClass:
    """LockedClass that let the user dynamically
    create a new instance attribute
    """
    __slots__ = ["first_name"]
