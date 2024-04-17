#!/usr/bin/python3
"""A python code written by chika mark"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        value = load_from_json_file("add_item.json")
    except FileNotFoundError:
        value = []
    value.extend(sys.argv[1:])
    save_to_json_file(value, "add_item.json")
