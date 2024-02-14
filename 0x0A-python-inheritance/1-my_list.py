#!/usr/bin/python3

"""Defines a class that inherits a class"""


class MyList(list):
    """MyList inherits list"""

    def print_sorted(self):
        """Function that returns sorted list"""

        print(sorted(self))