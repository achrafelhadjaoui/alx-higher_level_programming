#!/usr/bin/python3

"""Define is_kind_o_class function"""


def is_kind_of_class(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""
    if not isinstance(obj, a_class):
        return False
    else:
        return True
