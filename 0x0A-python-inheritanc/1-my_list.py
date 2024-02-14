#!/usr/bin/python3

"""Defines a function that inherits"""


class MyList(list):
    """Sorted list"""


    def print_sorted(self):
        print(sorted(self))