#!/usr/bin/python3
"""A function """
import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename, 'r') as file:
        return json.load(file)
