#!/usr/bin/python3
"""function"""


def inherits_from(obj, a_class):
    """checks if obj is an instance of a_class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
