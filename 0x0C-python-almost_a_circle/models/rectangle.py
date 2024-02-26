#!/usr/bin/python3

"""Define a Class Rectangle that inherits from Base"""

from base import Base


class Rectangle(Base):
    """Represent the Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialized function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set new value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height new value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x value"""
        return self.__x

    @x.setter
    def x(self, x):
        """set new value to x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @property
    def y(self):
        """get the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set new value to y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return the area value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """print to the stdout the Rectangle instance with char #"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for q in range(self.__x):
                print(end=" ")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Return the print() and str() representation
        of the Rectangle."""
        return"[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                      self.__y,
                                                      self.__width,
                                                      self.__height)

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""
        if len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.__width = arg
                elif count == 2:
                    self.__height = arg
                elif count == 3:
                    self.__x = arg
                elif count == 4:
                    self.__y = arg
                count += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """method that returns the dictionary
        representation of a Rectangle"""
        new = {'x': self.x, 'y': self.y, 'id': self.id,
               'width': self.width, 'height': self.height}
        return new
