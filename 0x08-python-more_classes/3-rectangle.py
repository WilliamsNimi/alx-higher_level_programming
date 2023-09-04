#!/usr/bin/python3

# -*- coding: utf-8 -*-
""" This module contains the rectangle class """


class Rectangle:
    """ This is the rectangle class
       Attributes:
                  width- this is the width of the rectangle
                  height-  This is the height of the rectangle
    """
    width = 0
    height = 0

    def __init__(self, width=0, height=0):
        """ This is the __init__ method
           Args:
               self- This is the instantiation of a class
           Return:
                 returns nothing
        """
        self.width = width
        self.height = height

    def width(self):
        """ This is a getter method for the width of a rectangle
           Args:
                self- This is the instantiation of a class
           Return:
                 returns width of the rectangle
        """
        return self.width

    def width(self, value):
        """ This is a setter method for the width of a rectangle
           Args:
                self- This is the instantiation of a class
                value- New width of the rectangle
           Return:
                 nothing
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.width = value

    def height(self):
        """ This is a getter method for the height of a rectangle
           Args:
                self- This is the instantiation of a class
           Return:
                 returns heigth of the rectangle
        """
        return self.height

    def height(self, value):
        """ This is a setter method for the height of a rectangle
           Args:
                self- This is the instantiation of a class
                value- New height of the rectangle
           Return:
                 nothing
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.height = value

    def area(self):
        """ This is the area function
           Args:
               self- This is the instantiation of a class
           Return:
                  nothing
        """
        return self.height * self.width

    def perimeter(self):
        """ This is the perimeter function
           Args:
               self- This is the instantiation of a class
           Return:
                  nothing
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        """ This is the __str__ function
           Args:
                self- This is the instatiation of a class
           Return:
                  nothing
        """
        if self.height == 0 or self.width == 0:
            return ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                print("#", end="")
            if i < self.height - 1:
                print("")
        return ""
