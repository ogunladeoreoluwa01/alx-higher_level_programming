#!/usr/bin/python3
"""This module contains a function to check if an object
is an instance o f a specified class"""


def is_same_class(obj, a_class):
    """Checks if an object is the same as the specified class

    Args:
        obj (object) the object to be checked
        a_class (object): the criteria

    Returns:
        _type_: _description_
    """
    if type(obj) == a_class:
        return True
    return False
