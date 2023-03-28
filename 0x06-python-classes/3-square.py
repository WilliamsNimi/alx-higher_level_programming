#!/usr/bin/python3

# -*- coding: utf-8 -*-
""" This module contains the implementation of the geometric Square """


class Square:
    """ This is the Square class
    Attributes:
              _Square__size: This is the size of the square
    """
    _Square__size = None

    def __init__(self, size=0):
        """ This is the __init__ method
        Args:
            self: This is the object instantiation
            size: This is the size of the square
        Returns:
            Doesn't return anything
        Raises:
               ValueError: This checks the value of the size
               TypeError: This checks the type of the size
        """
        try:
            if type(size) == int:
                if size >= 0:
                    self._Square__size = size
                else:
                    raise ValueError("size must be >=0")
            else:
                raise TypeError("size must be an integer")
        except ValueError as er:
            print(er)
        except TypeError as err:
            print(err)

    def area(self):
        """ This is the implementation of the area of a square
        Args:
             self: This is the object instatiation
        Returns:
             Returns the area of the square
        """
        return self._Square__size * self._Square__size
