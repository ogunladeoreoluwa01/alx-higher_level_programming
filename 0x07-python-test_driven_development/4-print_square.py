#!/usr/bin/python3
"""The function in this module prints
the dimensions of a square
"""


def print_square(size):
    """print_square prints out a square using "#"

    Args:
        size (int): THe size of the square

    Raises:
        TypeError: size must be an integeer
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for num in range(size):
        for num in range(size):
            print("#", end="")
        print("")
