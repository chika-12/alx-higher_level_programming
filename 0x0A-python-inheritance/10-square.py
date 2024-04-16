#!/usr/bin/python3
"""A python code """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass of Rectangle"""

    def __init__(self, size):
        """Validates size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
