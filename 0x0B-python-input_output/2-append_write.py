#!/usr/bin/python3
"""This module contains an appending function"""


def append_write(filename="", text=""):
    """It appends to a text file"""
    with open(filename, 'a', encoding='utf -8') as file_obj:
        c = file_obj.write(text)
    return c
