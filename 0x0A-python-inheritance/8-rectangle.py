#!/usr/bin/python3

"""Defines a Rectangle class"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialises a Rectangle

        Args:
            width: width of the rectangle
            Height: height of the reactangle

        """
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        self.integer_validator("width", width)
