#!/usr/bin/python3
"""Defines an function that checks for an object"""


def inherits_from(obj, a_class):
    """Function that checks if an object is an instance
      or an instance of inherited class

    Args:
        obj: Object to check
        a_class: class to be compared with

    Returns:
        returns True is object is is an instance or an instance
        of inherited class


    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
