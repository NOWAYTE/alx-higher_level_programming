#!/usr//bin/python3
"""Defines a function that checks an object """


def is_same_class(obj, a_class):
    """Function return true if an obejct is an instance of a class"""

    if type(obj) == a_class:
        return True
    return False
    