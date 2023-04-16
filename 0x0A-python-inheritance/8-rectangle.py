#!/usr/bin/python3
"""Creates a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates aclass called rectangle"""
    def __init__(self, width, height):
        """Initializes a class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
