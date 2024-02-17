#!/usr/bin/python3
"""Define a Class Base"""
import json


class Base:
    """Represent of the Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """a function that initialzes a newly created object

        Args: id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_string):
        """Return the json string"""
        if list_string is None or list_string == "[]":
            return []
        return json.dumps(list_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """write json string to a file"""
        filename = cls.__name__ + '.json'
        with open(filename, "w") as content:
            if list_objs is None:
                content.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                content.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the json string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
