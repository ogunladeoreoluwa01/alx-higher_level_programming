#!/usr/bin/python3
"""This returns a serializable description o f a class"""


def class_to_json(obj):
    """This returns a serializable description o f a class"""
    return obj.__dict__
