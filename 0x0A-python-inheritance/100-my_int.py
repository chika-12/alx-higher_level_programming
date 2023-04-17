#!/usr/bin/python3
"""A class instance"""


class MyInt(int):
    """A class"""

    def __eq__(self, other):
        """swaps eq for ne"""
        return super().__ne__(other)

    def __ne__(self, other):
        """swaps ne for eq"""
        return super().__eq__(other)
