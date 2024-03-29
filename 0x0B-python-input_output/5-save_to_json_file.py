#!/usr/bin/python3

"""Define a function def save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
        using JSON representation

    Args:
        my_obj
        filename
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        json_data = json.dumps(my_obj)
        f.write(json_data)
