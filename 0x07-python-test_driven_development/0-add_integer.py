#!/usr/bin/python3

"""add integers"""


def add_integer(a, b=98):
    """Return the addition of a and b"""
    if not (isinstance(a, int)) and not (isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return(int(a) + int(b))