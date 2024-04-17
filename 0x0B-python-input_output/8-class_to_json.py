#!/usr/bin/python3
"""A python code written by chika mark"""


def class_to_json(obj):
    """Creating a dictionary from a class instance for json serialization"""

    return obj.__dict__
