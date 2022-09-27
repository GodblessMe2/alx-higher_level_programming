#!/usr/bin/python3
"""Read the text file [UTF8]"""


def read_file(filename=""):
    """Read the string in the file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
