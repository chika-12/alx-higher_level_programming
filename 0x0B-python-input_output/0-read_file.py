#!/usr/bin/python3
"""A function for opening"""


def read_file(filename=""):
    """OPens a file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
