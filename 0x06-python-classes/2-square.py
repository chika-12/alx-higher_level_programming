#!/usr/bin/python3
# 0-square.py by Chika Mark
"""Defines a square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):

        """Initializing the square
        Args:
             size: defines the size of the square

        Raise:
              ValueError: If the size is less than 0
              TypeError: If the size is not an interger
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")

        self.__size = size
