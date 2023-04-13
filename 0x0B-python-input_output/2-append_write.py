#!/usr/bin/python3
"""A beautiful function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a string"""

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
