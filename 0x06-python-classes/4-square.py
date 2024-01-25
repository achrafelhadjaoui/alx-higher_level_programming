#!/usr/bin/python3

"""Define a Class Square"""


class Square:
    """Represent of the Square"""

    def __init__(self, size=0):
        """initialize a Square

        Args:
            size: The size of the new square
        """
        self.__size = size

    @property
    def size(self):
        """"Retrive the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the new size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)
