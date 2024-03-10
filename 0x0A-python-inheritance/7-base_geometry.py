#!/usr/bin/python3

"""Defines a BaseGeomtry class"""


class BaseGeometry:

    """Represents a base Geometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a parameter as an integer


        Args:
            name(str): the name of the parameter
            value(int): Parameter to be validated

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0

        """
        if type(value) is not int:
            raise Exception("<name> must be an integer")

        if value <= 0:
            raise Exception("<name> must be greater than 0")
