#!/usr/bin/python3
"""Defines a Rectangle class"""


from model.base import Base

class Rectangle(Base):
    """Inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value 

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")

        self.__height = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("X must be an integer")
        
        if value < 0:
            raise ValueError("X must be >=  0")

        self.__x

    @property 
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if not isinstance(self, value):
            raise TypeError("Y must be an integer")

        if value < 0:
            raise ValueError("Y must be >= 0")

        self.__y = value

