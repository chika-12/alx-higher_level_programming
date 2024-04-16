#!/usr/bin/python3
"""A python code"""


def write_file(filename="", text=""):
    """Writing into a file"""

    with open(filename, "w", encoding="UTF-8") as file:
        return (file.write(text))
