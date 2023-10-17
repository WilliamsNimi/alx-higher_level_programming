#!/usr/bin/python3
""" This is the rectangle Class module """
from models.base import Base


class Rectangle(Base):
    """ This is the Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ This is the init constructor """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ This is the getter function for the width attribute """
        return self.__width

    @width.setter
    def width(self, width):
        """ This is a setter function for the width """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ This is the getter function for the height attribute """
        return self.__height

    @height.setter
    def height(self, height):
        """ This is the setter function for the height attribute """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ This is the getter function for the x attribute """
        return self.__x

    @x.setter
    def x(self, x):
        """ This is the setter class for the x attribute """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x


    @property
    def y(self):
        """ This is the getter function for the y attribute """
        return self.__y

    @y.setter
    def y(self, y):
        """ This is the setter class for the y attribute """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ This is the area calculation function """
        return self.__width * self.__height

    def display(self):
        """ This is a function to display the rectangle with # """
        if self.__y > 0:
            for l in range(0, self.__y):
                print("")
        for i in range(0, self.height):
            for k in range(0, self.__x):
                if self.__x >= 0 and self.__y >= 0:
                    print(" ", end="")
            for j in range(0, self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ This function overrides the __str__ function """
        id = self.id
        x = self.__x
        y = self.__y
        width = self.__width
        height = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}". format(id, x, y, width, height)

    def update(self, *args, **kwargs):
        """ This is an update with args function """
        if len(args) != 0:
            for i in range(0, len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.__width = args[1]
                if i == 2:
                    self.__height = args[2]
                if i == 3:
                    self.__x = args[3]
                if i == 4:
                    self.__y = args[4]
        else:
            for key, values in kwargs.items():
                if key == "id":
                    self.id = values
                elif key == "width":
                    self.__width = values
                elif key == "height":
                    self.__height = values
                elif key == "x":
                    self.__x = values
                elif key == "y":
                    self.__y = values

    def to_dictionary(self):
        """ Returns the dictionary representation of Rectangle """
        return self.__dict__
