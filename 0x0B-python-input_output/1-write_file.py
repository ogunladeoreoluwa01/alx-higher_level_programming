#!/usr/bin/python3
"""This file writes to a file or creates it if it is not there"""


def write_file(filename="", text=""):
    """It writes info into a file"""
    with open(filename, 'w', encoding='utf -8') as file_obj:
        return file_obj.write(text)
