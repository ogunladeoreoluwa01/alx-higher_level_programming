#!/usr/bin/python3
"""This square contains a new method, area
    which gives us the area of the square"""


class Square:
    """IT has two methond, init and  area
    THeir job is to intiialzie the class and return its area srespectively"""
    def __init__(self, size=0):
        """This intializes the size attribute in a safe mode"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """"This returns the value of the area of the size"""
        return self.__size ** 2
