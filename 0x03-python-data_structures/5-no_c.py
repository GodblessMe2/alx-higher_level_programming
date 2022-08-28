#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for c in my_string:
        if chr(99) != c and chr(67) != c:
            new_string += c
    return new_string
