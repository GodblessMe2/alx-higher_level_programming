#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of 10 and 5."""
    from calculator_1 import *
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))

    """Print the sub of 10 and 5."""
    print("{} - {} = {}".format(a, b, sub(a, b)))

    """Print the mul of 10 and 5."""
    print("{} + {} = {}".format(a, b, mul(a, b)))

    """Print the div of 10 and 5."""
    print("{} + {} = {}".format(a, b, div(a, b)))
