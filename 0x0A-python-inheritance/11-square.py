#!/usr/bin/python3


"""Defines a Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initialize a square

        Args:
            size(int): The size of the sqaure

        """

        self.integer_validator("size", size)
        super().__init__(size, size)

        self.___size = size
