#!/usr/bin/python3
"""Defines a function that checks an objct"""


def is_kind_of_class(obj, a_class):
    """Function that checks if an object is an instance or an instance of inherited class
    
    Args:
        obj: Object to check 
        a_class: class to be compared with

    Returns:
        returns True is object is is an instance or an instance 
        of inherited class

    
    """

    if isinstance(obj, a_class):
        return True
    return False
