#!/usr/bin/python3
"""Contains the "append_after" function"""


def append_after(filename="", search_string="", new_string=""):
    """Returns a list of lists of integers representing the Pascal’s triangle of n"""
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
