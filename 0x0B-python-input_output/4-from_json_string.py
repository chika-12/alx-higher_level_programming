#!/usr/bin/python3
"""A function"""
import json


def from_json_string(my_str):
    """Converts a json string to python object"""

    return json.loads(my_str)
