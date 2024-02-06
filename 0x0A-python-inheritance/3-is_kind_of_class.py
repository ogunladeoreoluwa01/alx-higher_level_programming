#!/usr/bin/python3
"""This module contains a function to check if an object
is an instance o f a specified class or it's subclass"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of the specified class

    Args:
        obj (object): the object to be checked
        a_class (object): the criteria

    Returns:
        bool: True or false depending on outcome
    """
    return isinstance(obj, a_class)
