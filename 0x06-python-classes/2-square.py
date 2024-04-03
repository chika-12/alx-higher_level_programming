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
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
