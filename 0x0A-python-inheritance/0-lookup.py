#!/usr/bin/python3
"""This module contains a function that eturns all class attributes"""


def lookup(obj):
    """_summary_

    Args:
        obj (object): an object

    Returns:
        list: all attributes of the object
    """
    return dir(obj)
