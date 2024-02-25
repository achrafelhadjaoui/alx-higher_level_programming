#!/usr/bin/python3

"""
    add integer module
    this module have one function add_integer()

"""


def add_integer(a, b=98):
    """Return the sum of a and b
    otherwise raise a TypeError exception with a message
    """
    if not (isinstance(a, int)) and not (isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return(int(a) + int(b))
