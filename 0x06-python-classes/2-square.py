#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """A class that defines a square and a private instance attribute size"""
    def __init__(self, size=0):
        self.__size = size
        try:
            if isinstance(size, int):
                pass
            if not size < 0 :
                pass
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
