#!/usr/bin/python3
"""This module contains a class that inherits from the Base class.
This is the Rectangle class. Within this class, we would build our first
geometric shape; the rectangle by adding attributes
 peculiar to the rectangle"""
from models.base import Base


class Rectangle(Base):
    """This class inherits from  base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle

        Args:
            width (int): the rectangle's width
            height (int): the rectangle's height
            x (int, optional): the x-coordinate of the rectangle.
                                Defaults to 0.
            y (int, optional): the y-coordinate of the rectangle.
                                Defaults to 0.
            id (int, optional): the instance id. Defaults to None.
        """
        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width getter

        Returns:
            int: the Rectangle's width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """The width setter

        Args:
            value (int): the new value we want to set as the width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The height getter

        Returns:
            int: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """The height setter. It makes sure we put only the right
        values as height

        Args:
            value (int): the new value we want to set as width

        Raises:
            TypeError: height should be an integer
            ValueError: height should be > 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This is the x-coordinate of the shape on the window

        Returns:
            int: the Rectangle's x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """The x setter

        Args:
            value (int): the new x value for the instance of Rectangle

        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This is the y-coordinate of the shape on the window

        Returns:
            int: the Rectangle's y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """The y setter

        Args:
            value (int): the new y value for the instance of Rectangle

        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This returns the area of the Rectangle

        Returns:
            _int_: the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """This prints out a string representation of the area of the rectangle
        """
        for a in range(self.__y):
            print()
        for b in range(self.__height):
            for c in range(self.__x):
                print(" ", end="")
            for d in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """This updates the attributes of the Rectangle instance
        """
        i = 0
        for arg in args:
            if i == 0:
                if args[0] is not None:
                    self.id = args[0]
                else:
                    self.__init__(self.width, self.height, self.x, self.y)

            if i == 1:
                self.width = args[1]
            if i == 2:
                self.height = args[2]
            if i == 3:
                self.x = args[3]
            if i == 4:
                self.y = args[4]
            i += 1
        if not args:
            for key, value in kwargs.items():
                try:
                    setattr(self, key, value)
                except KeyError:
                    continue

    def to_dictionary(self):
        """This returns a dict representing the class attributes

        Returns:
            dict: the class attributes: value pair
        """
        dict_r = {'id': self.id, 'width': self.width, 'height': self.height,
                  'x': self.x, 'y': self.y}
        return dict_r
