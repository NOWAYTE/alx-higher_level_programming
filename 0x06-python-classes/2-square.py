#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """A class that defines a square and a private instance attribute size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
