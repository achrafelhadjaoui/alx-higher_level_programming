#!/usr/bin/python3
"""Define inherits_from func"""


def inherits_from(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""

    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
