#!/usr/bin/python3


"""Define the list class"""


class MyList(list):
    """A subclass of the derived class"""
    
    def print_sorted(self):
        """Print out the ascending sort list"""
        print(sorted(self))
