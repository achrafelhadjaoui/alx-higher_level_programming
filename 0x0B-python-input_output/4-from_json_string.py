#!/usr/bin/python3

"""Define a function from_json_string"""
import json


def from_json_string(my_str):
    """a function that returns an object represented
        by json string

    Args:
        my_str
    """

    return json.loads(my_str)
