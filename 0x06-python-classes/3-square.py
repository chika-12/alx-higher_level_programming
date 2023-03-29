#!/usr/bin/python3
# 0-square.py by Chika Mark
"""A module that defines a square"""


class Square:
    """A class tha represents a square"""

    def __init__(self, size):

        """Initializes asquare
        Args:
            size: Defines the size of the square
        Raise:
            TypeError: If the the size is not an integer
            ValueError: if the size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >0")

        self.__size = size

    def area(self):
        """Defines the area of a square"""
        return(self.__size ** 2)
