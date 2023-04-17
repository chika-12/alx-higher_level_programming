#!/usr/bin/python3
"""A function"""


def add_attribute(obj, attr_name, value):
    """Checks if object is an instance of certain class"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
