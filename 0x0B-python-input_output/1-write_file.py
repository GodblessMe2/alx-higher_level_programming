#!/usr/bin/python3
"""Writes a string to a text file"""


def write_file(filename="", text=""):
    """Returns the numbers of characters written to the file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
