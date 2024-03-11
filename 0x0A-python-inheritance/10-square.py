#!/usr/bin/python3

"""Defines a Square class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """Represents a Square class"""

    def __init__(self, size):
        """Instantiating sqaure
        Args:
            size(int): represents the size of the sqaure

        """

        self.__size = size
        super().__init__()
        super().integer_validator("size", size)
        self.__width = size
        self.__height = height

        def area(self):
            """Return the area of the rectangle"""

            return self.__width * self.__height
