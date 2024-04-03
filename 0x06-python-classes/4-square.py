#!/usr/bin/python3
"""This is a python script"""


class Square:

    """This script does more computations on the square class"""

    def __init__(self, size=0):

        """Defines the size of a square
        raises: an error message if size is not an int
        an also when it less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):

        """To retrive size"""
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        return self.__size * self.__size
