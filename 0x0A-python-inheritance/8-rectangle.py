#!/usr/bin/python3
"""This module contains a class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a subclass that inherits from our BaseGeometry class

    Args:
        BaseGeometry (class): the parent class
    """
    def __init__(self, width, height):
        """initializes the rectangle's dimensions

        Args:
            width (int): the width
            height (height): the height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
