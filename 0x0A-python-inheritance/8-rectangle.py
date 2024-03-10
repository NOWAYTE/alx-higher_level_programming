#!/usr/bin/python3

"""Defines a class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a class rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width: The width of the  Rectangle.
            height: The height of the new Rectangle.
        """
        self._width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
