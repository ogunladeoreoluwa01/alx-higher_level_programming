#!/usr/bin/python3
"""The module teaches us about subclass methods and how to look for them"""


def inherits_from(obj, a_class):
    """It checks if a class inherited from another class

    Args:
        obj (object): the object ot be checked
        a_class (object): the criteria

    Returns:
        bool: True or false depending on outcome
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
