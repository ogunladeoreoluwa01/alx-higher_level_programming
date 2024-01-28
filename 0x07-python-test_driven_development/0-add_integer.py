#!/usr/bin/python3
"""The function in this module adds up two integers
"""


def add_integer(a, b=98):
    """The function adds two integers or floats together

    Args:
        a (int, float): first parameter
        b (int, optional): second parameter. Defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: the sum of int a and int b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
