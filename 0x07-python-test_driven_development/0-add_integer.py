#!/usr/bin/python3
"""

This is a python code that adds up two integers


"""


def add_integer(a, b=98):
    """
    Returns the sum of two integers or float as intergers

    Args:
        a: first argument
        b: second argument

    Returns: sum of the two integers

    Raises:
        TypeError: If any of the argument is not an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
