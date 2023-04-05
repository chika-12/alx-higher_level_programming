#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """A rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a rectangle
        Arg:
            Width: A property of a rectangle
            Height: Also a property of a rectangle
        Exceptions:
            TypeError: Occurs if width or height is not an interger
            ValueError: Occurs if with or height is less than zero
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retives the property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Assigns value to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrives property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Assigns value to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height))

    def __str__(self) -> str:
        """Returns a string"""
        if self.width == 0 or self.height == 0:
            return("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        """Returns a triangle"""
        return "Rectangle {:d}, {:d}".format(self.__width, self.__height)

    def __del__(self):
        """Prints message for every object that is deleted"""
        print("Bye rectangle...")
