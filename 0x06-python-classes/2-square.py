#!/usr/bin/python3
"""This class initializes size but in this case, it checks
     to see if the size is an appropriate value"""


class Square:
    """The class takes a value in a try and except block"""
    def __init__(self, size=0):
        """This initializes the size attribue in a safe mode"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
