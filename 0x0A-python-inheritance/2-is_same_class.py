#!/usr/bin/python3
"""creates a class"""


def is_same_class(obj, a_class):
    """checking if object is the instance of the specified class"""
    if not isinstance(obj, a_class):
        return True
    else:
        return False
