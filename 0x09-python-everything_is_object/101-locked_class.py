#!/usr/bin/python3
"""This module contains a special kind of class
"a locked clas whci cqn only take a certain variable name
"""


class LockedClass:
    """Create a class that can only take one variable as an instance
    an instance attribute named first_name
    """
    __slots__ = ['first_name']
