#!/usr/bin/python3
"""This is a python script"""


class Square:

    """This script does more computations on the square class"""

    def __init__(self, size=0, position=(0, 0)):

        """Defines the size of a square
        raises: an error message if size is not an int
        an also when it less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        #if not isinstance(position, tuple):
        #raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = position
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

    def position(self):
        
        """To retrieve postion"""
        return self.__position

    def position(self, value):
        """Sets the value of position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):

        return self.__size * self.__size

    def my_print(self):

        if self.__size != 0:
            for num in range(self.__size):
                for val in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
