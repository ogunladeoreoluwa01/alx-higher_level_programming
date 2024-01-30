#!/usr/bin/python3
"""THis module contains a class named rectangle
"""


class Rectangle:
    """This creates an empty class
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """This initializes the class

        Args:
            width (int, optional): the size. Defaults to 0.
            height (int, optional): the height. Defaults to 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        type(self).number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * self.__height

    def perimeter(self):
        """gives the perimeter of the rectangle

        Returns:
            int: the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """string representation of the class

        Returns:
            str: the string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        s = ""
        for i in range(self.__height):
            for j in range(self.__width):
                s += "#"
            if i != (self.__height - 1):
                s += "\n"
        return s

    def __repr__(self):
        """Returns a string representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"
        return s

    def __del__(self):
        """This deletes the class
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
