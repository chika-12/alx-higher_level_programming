#!/usr/bin/python3
"""A python code"""


def read_file(filename=""):
    """opening file for reading"""

    with open(filename, "r", encoding="UTF-8") as file:
        line = file.read()

        print(line, end="")
