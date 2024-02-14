#!/usr/bin/python3

"""Defines a function that inherits"""


class MyList(list):
    """Sorted list"""


    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        
        print(sorted(self))
