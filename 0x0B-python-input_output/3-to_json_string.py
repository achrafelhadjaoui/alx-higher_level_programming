#!/usr/bin/python3

import json

"""Define a function to_json_string"""


def to_json_string(my_obj):
    """a function that returns the JSON representation
        of an object(string)

    Args:
        my_obj
    """

    return repr(json.dumps(my_obj))
