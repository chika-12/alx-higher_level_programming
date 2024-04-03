#!/usr/bin/python3
"""This is a python script"""


class Square:

    """This script does more computations on the square class"""

    def __init__(self, size=0):
        self.__size = int(size)

        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size must be >= 0")
