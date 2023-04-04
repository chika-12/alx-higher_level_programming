#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """This is a triangle"""

    def __init__(self, width=0, height=0):
        """Initialization of a triangle
        Args:
            width: one of the properties of a triangle
            height: also a property of a triangle
        Exceptions:
            TypeErrror: checks if argument is an integer value
            ValueError: checks if argument is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """raise type and value exceptions"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """raise type and value exeption"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height ==0:
            return 0
        return ((self.__width * self.height) + (self.__width * self.__height))