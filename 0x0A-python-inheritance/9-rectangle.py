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

    def __str__(self):
        """A string representation of the class

        Returns:
            str: a strign representation of the class
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Computes the area of the shape

        Returns:
            int: the area of the shape
        """
        return self.__width * self.__height
