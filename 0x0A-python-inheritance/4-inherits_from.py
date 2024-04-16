#!/usr/bin/python3
"""A python code"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a_class"""

    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
