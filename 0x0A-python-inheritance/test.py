#!/usr/bin/python3

"""Defines a Square class """


class Square:
    """Represents a Square class that inherits from BaseRectangle"""

    def __init__(self, size):
        """Instance of a square

        Args:
            size(int): Represents the size of the square

        """

        self.__size = size
        super().__init__(size, size)
        super().integer_validator("size", size)

    def area(self):
        """Returns the area of the square"""

        return self.__size * self.__size

    def __str__(self):
        """Returns the string representation of the square"""

        return f"{[self.__class__.__name__}] {self.__width}/{self.__height}"
