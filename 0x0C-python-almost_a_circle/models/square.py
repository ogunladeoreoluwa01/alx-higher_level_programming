#!/usr/bin/python3
"""This module imports from the rectangle's module
and creates a new class, ; the square. We all know that the square is a
special kind of rectangle with equal sides,"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a class that inherits from the Base Class

    Args:
        Rectangle (Rectangle): a class of a geometric shape
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the class

        Args:
            size (int): the width/height
            x (int, optional): the x-coordinate. Defaults to 0.
            y (int, optional): the y-coordinate. Defaults to 0.
            id (int, optional): the instance id. Defaults to None.
        """
        self.size = size
        super(Square, self).__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter

        Returns:
            int: returns the size
        """
        return self.width

    @size.setter
    def size(self, value):
        """Size setter

        Args:
            value (int): the new size

        Raises:
            TypeError: value must be an integer
            ValueError: value must be > 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Overrides str method in parent class

        Returns:
            str: a user-friendly string representation of the class
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """This updates the attributes of the Square instance
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
                self.x = args[2]
            if i == 3:
                self.y = args[3]
            i += 1
        if not args:
            for key, value in kwargs.items():
                try:
                    setattr(self, key, value)
                except KeyError:
                    continue
        self.height = self.width

    def to_dictionary(self):
        """This returns a dict representing the class attributes

        Returns:
            dict: the class attributes: value pair
        """
        dict_s = {'id': self.id, 'size': self.width,
                  'x': self.x, 'y': self.y}
        return dict_s
