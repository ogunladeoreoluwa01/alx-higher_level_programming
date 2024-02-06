#!/usr/bin/python3
"""A class that inherits from the list"""


class MyList(list):
    """A class that inherits from the

    Args:
        list (list): the base class
    """
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints out a sorted list
        """
        print(sorted(self))
