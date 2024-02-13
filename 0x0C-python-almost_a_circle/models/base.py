#!/usr/bin/python3

"""Define a Class Base"""


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
