#!/usr/bin/python3
"""This module contains a class"""


class BaseGeometry:
    """defines a class
    """
    def area(self):
        """Returns the area of the shape

        Raises:
            Exception: always because we do not know
            the shape we're dealing with yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Makes sure the integers given are of the right kind

        Args:
            name (str): the integer's label
            value (int): the integer's value

        Raises:
            TypeError: the value must be an integer
            ValueError: the value must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
