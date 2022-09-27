#!/usr/bin/python3
"""Append a string at the end of a text file"""


def append_write(filename="", text=""):
    """Return a string that was appended to a file"""
    with open(filename, mode= "a", encoding="utf-8") as f:
        return (f.write(text))
