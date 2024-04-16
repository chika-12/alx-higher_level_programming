#!/usr/bin/python3
"""A python code that inherit from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Instatiation of subclass"""

    def __init__(self, width, height):
        """Initializes a class"""

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
