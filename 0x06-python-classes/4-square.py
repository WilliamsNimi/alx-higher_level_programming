#!/usr/bin/python3

# -*- coding: utf-8 -*-
""" This module contains the implementation of the geometric square """


class Square:
    """ This is the Square class
    Attributes:
              _Square__size: This is the size of the square
    """
    _Square__size = None

    def __init__(self, size=0):
        """ This is the __init__ method
        Args:
            self: This is the object instatiation
            size: This is the size of the square
        Returns:
               returns nothing
        Raises:
               ValueError: This checks the value of the size
               TypeError: Checks the type of the size
        """
        if type(size) == int:
            if size >= 0:
                self._Square__size = size
            else:
                raise ValueError("size must be >=0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ This is the area method
        Args:
            self: this is the object instatiation
        Returns:
               returns the area of the sqaure
        """
        return self._Square__size * self._Square__size

    def size(self):
        """ This is the size method
        Args:
             self: this is the obejct instatiation
        Returns:
               returns the size of the square
        """
        return self._Square__size

    def size(self, value):
        """ This is the size setter method
        Args:
             self: this is the obejct instatiation
             value: The value of the square to be set
        Returns:
               returns nothing
        Raises:
               ValueError: This checks the value of the size
               TypeError: Checks the type of the size
        """
        if type(value) == int:
            if value >= 0:
                self._Square__size = value
            else:
                raise ValueError("size must be >=0")
        else:
            raise TypeError("size must be an integer")
