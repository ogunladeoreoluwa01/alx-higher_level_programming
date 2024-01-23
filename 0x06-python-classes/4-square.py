#!/usr/bin/python3
"""In this module, we would get our introduction to getters and setters
for the first time"""


class Square:
    """This class contains three methonds:
        an init, a size, and area, then getter and setter"""
    def __init__(self, size=0):
        """This initializes the string in a safe mode"""
        self.__size = size

    @property
    def size(self):
        """This is a getter function.
            It returns the value of size safely"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """This is the setter function. It prevents unwarranted modification
        of the size attribute by users"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This is the former area function.
        it gives the area of the square"""
        return (self.__size ** 2)
