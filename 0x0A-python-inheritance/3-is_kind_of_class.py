#!/usr/bin/python3
"""
Contains the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
