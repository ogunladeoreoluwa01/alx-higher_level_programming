#!/usr/bin/python3
"""This module contains a class named rectangle
"""


class Rectangle:
    """This creates an empty class
    """

    def __init__(self, width=0, height=0):
        """This initializes the class

        Args:
            width (int, optional): the size. Defaults to 0.
            height (int, optional): the height. Defaults to 0.
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        """Returns the width

        Returns:
            int: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width

        Args:
            value (int): the new value

        Raises:
            TypeError: value should be an integer
            ValueError: value should be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height

        Returns:
            int: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height

        Args:
            value (int): the new value

        Raises:
            TypeError: value should be an integer
            ValueError: value should be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Gives the area of the rectangle

        Returns:
            int: the area
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * self.height

    def perimeter(self):
        """gives the perimeter of the rectangle

        Returns:
            int: the perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
