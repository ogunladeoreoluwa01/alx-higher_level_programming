#!/usr/bin/python3
"""This module contains a function that loads from a json file"""
import json


def load_from_json_file(filename):
    """"This loads from a json file"""
    with open(filename, 'r') as ft:
        return json.load(ft)
