#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """A class that defines a private instance attribute size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
    
    def area(self):
        """a public instance method that returns the current area"""
        return self.__size * self.__size

