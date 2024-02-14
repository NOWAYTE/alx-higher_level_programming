#!/usr//bin/python3
"""Defines a function that checks an object """


def is_same_class(obj, a_class):
    """Function return true if an obejct is an instance of a class


    Args:
        obj: Object to check
        a_class: The class in which the object belongs to

    Return:
        returns true if the object is an instance of a_class
    
    """

    if type(obj) == a_class:
        return True
    return False
