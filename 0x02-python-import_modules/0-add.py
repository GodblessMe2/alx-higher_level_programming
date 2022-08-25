#!/usr/bin/python3
import imp


if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    from add_0 import add

    print("{} + {} = {}".format(1, 2, add(1, 2)))
