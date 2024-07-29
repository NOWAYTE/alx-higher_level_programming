#!/usr/bin/python3
"""Contains a base class"""


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes an instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
