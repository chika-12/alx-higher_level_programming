#!/usr/bin/python3
"""A beutiful function"""
import json


def save_to_json_file(my_obj, filename):
    """write a json object to a text file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
