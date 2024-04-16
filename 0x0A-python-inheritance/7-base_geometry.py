#!/usr/bin/python3
"""A python code"""


class BaseGeometry:
    """Empty class"""

    def area(self):
        """raises an exception if area is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validetes value"""

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
