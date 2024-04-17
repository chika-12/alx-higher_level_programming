#!/usr/bin/python3
"""A python code written by chika"""
import json


def load_from_json_file(filename):
    """Creating an object from a json code"""

    with open(filename) as file:
        return json.load(file)
