#!/usr/bin/python3
"""THis creates a class that can be serialized"""


class Student:
    """A class that can be encoded into json"""
    def __init__(self, first_name, last_name, age):
        """Initializes the attributes of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a serializable representation of the class"""
        return self.__dict__
