#!/usr/bin/python3
"""A class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a class of instances"""

    def __init__(self, size):
        """Initiates a class"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        