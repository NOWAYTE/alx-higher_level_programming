#!/usr/bin/python3

"""Defines a Rectangle class """

BaseGeometry = __import__('7-base_geometry').BaeGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """instaniate rectangle

        Args:
            width(int): Width of the new rectangle
            Height(int): Height of th new rectangle

        """

        def area(self):
            """Defines the area of a rectangle"""

            return self.__width * self.__heigth

        def __str__(self):
            """Returns string representation of the object"""

            return f"[Rectangle] {self.__width}/self__height}"
