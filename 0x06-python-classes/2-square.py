#!/usr/bin/python3

"""Define a Class Square"""


class Square:
    """Reprent a Square"""

    def __init__(self, size=0):
        """Initialize a new aquare.

        Args:
            size: the of the new square
        """

        if type(size) is not int:
            raise TypeError("size must be an intege")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
