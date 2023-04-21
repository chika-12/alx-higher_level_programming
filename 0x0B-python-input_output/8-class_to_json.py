#!/usr/bin/python3
"""Converts class to json"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure"""
    return obj.__dict__
