#!/usr/bin/python3
"""Base class"""


class MyList(list):
    """Prints a list"""

    def print_sorted(self):
        sorted_self = sorted(self)
        print(sorted_self)
