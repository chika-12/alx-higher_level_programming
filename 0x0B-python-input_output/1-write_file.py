#!/usr/bin/python3
"""A function that returns the number of strings"""


def write_file(filename="", text=""):
    """creates a file and returns the number of characters"""

    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
