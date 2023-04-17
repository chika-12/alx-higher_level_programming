#!/usr/bin/python3
"""A class instance"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a class square"""

    def __init__(self, size):
        """Initialises a class"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        super().__str__()
        return "[Square] {}/{}".format(self.__size, self.__size)
