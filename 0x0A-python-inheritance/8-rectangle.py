#!/usr/bin/python3

"""Defines a Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialises a Rectangle

        Args:
            width: width of the rectangle
            Height: height of the reactangle

        """
        self.integer_validator("height", height)
        self.__heigth = height
        self.integer_validator("width", width)
        self.width = width