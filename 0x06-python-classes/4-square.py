#!/usr/bin/python3
"""A class Square that defines a square"""


def __init__(self, size=0):
    self.__size = size

@property
def size(self):
    return slef.__size

@size.setter
def size(self, value):
    if not isinstance(size, int):
        raise TypeError("size must me and integer")
    if size< 0:
        raise ValueError("size must be >= 0")

def size(self):
    return self.__size
