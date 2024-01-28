#!/usr/bin/python3
"""The function in this module prints out the person's name
as formatted output
"""


def say_my_name(first_name, last_name=""):
    """_summary_

    Args:
        first_name (str): The first namr of the individual
        last_name (str, optional): The econd name of the individual
            Defaults to ""

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
