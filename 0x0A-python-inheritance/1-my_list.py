#!/usr/bin/python3
"""creates a class"""


class MyList(list):
    """Initializes class"""
    def print_sorted(self):
        print(sorted(self))
