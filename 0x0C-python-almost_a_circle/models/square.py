#!/usr/bin/python3

"""Define a Class Square that inherits from Rectangle"""

from rectangle import Rectangle
from base import Base


class Square(Rectangle):
    """Represent of the class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initlaize the instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() Representation
        of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """get the value of width"""
        return self.width

    @size.setter
    def size(self, size):
        """set a new value to width and height"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """using args and kwargs"""
        if len(args) is not 0:
            count = 0
            for i in args:
                if count == 0:
                    self.id = i
                elif count == 1:
                    self.size = i
                elif count == 2:
                    self.x = i
                elif count == 3:
                    self.y = i
                count += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """method tht returns the dictionary
        representation of a square"""
        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
