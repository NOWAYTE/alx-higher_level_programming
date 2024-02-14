#!/usr/bin/python3

"""Defines function that checks for an object."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns:
        return True if an obj is an instance of a_class and
        False if not.
    """
    if type(obj) == a_class:
        return True
    return False