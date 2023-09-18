#!/usr/bin/python3
"""A module containing a function that prints a square"""


def print_square(size):
    """ Prints a square with character '#'
        Arguments:
            @size: is the length of the square
    """


    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    columns = size
    if columns:
        for i in range(size):
            for x in range(size):
                print("#".format(), end="")
            print()
