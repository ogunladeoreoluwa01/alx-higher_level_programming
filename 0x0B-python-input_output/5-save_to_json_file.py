#!/usr/bin/python3
"""This module brings us to saving information in json format"""
import json


def save_to_json_file(my_obj, filename):
    """This savess an object in json format"""
    with open(filename, 'w') as ft:
        json.dump(my_obj, ft)
