#!/usr/bin/python3
"""THis creates a class that can be serialized"""


class Student:
    """A class that can be encoded into json"""
    def __init__(self, first_name, last_name, age):
        """Initializes the attributes of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a serializable representation of the class"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return  {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Initialize a class' attributes from a dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
