#!/usr/bin/python3
"""A python code"""


def append_write(filename="", text=""):
    """Appends a text to a file"""

    with open(filename, "a", encoding="UTF-8") as file:
        return (file.write(text))
