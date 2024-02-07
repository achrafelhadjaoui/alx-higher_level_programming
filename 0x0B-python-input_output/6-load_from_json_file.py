#!/usr/bin/python3

"""Define a function load_from_json_file"""
import json


def load_from_json_file(filename):
    """a function that creats an Object from a JSON file

    Args:
        filename
    """

    with open(filename, mode="r", encoding="utf-8") as f:
        read_data = f.read()
        json_data = json.loads(read_data)
        return json_data
