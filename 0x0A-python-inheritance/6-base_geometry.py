#!/usr/bin/python3
"""This module contains a class"""


class BaseGeometry:
    """Defines the same class as in 5-base_geometry.py but with new methods
    """

    def area(self):
        """It is meant to compute the area of the geometric question in shape

        Raises:
            Exception: always because we dont even have a shape yet
        """
        raise Exception("area() is not implemented")
