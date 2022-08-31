#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i, l in sorted(a_dictionary.items()):
        print("{}: {}".format(i, l))
