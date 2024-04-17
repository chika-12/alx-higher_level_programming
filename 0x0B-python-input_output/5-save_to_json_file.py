#!/usr/bin/python3
"""A python code written by chika"""
import json


def save_to_json_file(my_obj, filename):
    """Saving a json object to a file"""

    with open(filename, "w", encoding="UTF-8") as file:
        j_file = json.dumps(my_obj)
        file.write(j_file)
