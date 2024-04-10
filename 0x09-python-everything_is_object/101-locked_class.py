#!/usr/bin/python3
"""
A python script
"""


class LockedClass:
    """
    A locked class attribute
    """

    def __setattr__(self, attr, value):
        if not hasattr(self, attr) and attr != 'first_name':
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attr}'")
        super().__setattr__(attr, value)
