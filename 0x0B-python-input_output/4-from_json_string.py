#!/usr/bin/python3
"""This brings us to deserialization in json"""
import json


def from_json_string(my_str):
    """This function deserializes a json object"""
    return json.loads(my_str)
