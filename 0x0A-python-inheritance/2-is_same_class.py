#!/usr/bin/python3
"""A python code"""


def is_same_class(obj, a_class):
    """Checks isinstance of an object"""

    if isinstance(type(obj), a_class):
        return True
    else:
        return False
