#!/usr/bin/python3
"""This module teaches us more about overriding methods in classes"""


class MyInt(int):
    """Creates a class MyInt whic is a subclass of the int class

    Args:
        int (int): the parent class
    """
    def __eq__(self, other):
        """Reverses the roles of the __eq method in the parent class

        Args:
            other (int): the value to be compared to

        Returns:
            bool: False if self == other, True otherwise
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """Ovverides the method in the parent class to do the reverse

        Args:
            other (int): the value to be compared to

        Returns:
            bool: False if self !=  other, True otherwise
        """
        return int(self) == int(other)
