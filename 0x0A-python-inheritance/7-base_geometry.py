#!/usr/bin/python3
"""Creates a class """


class BaseGeometry:
    """creates a class called geometry"""
    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raise TypeError and ValueError"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
