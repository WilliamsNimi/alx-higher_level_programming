#!/usr/bin/python3

# -*- coding: utf-8 -*-
""" This module contains the implementation of the geometric square """


class Square:
    """ This is the Square class
    Attributes:
              _Square__size: this is the size of the square
    """
    _Square__size = None

    def __init__(self, size=0):
        """ This is the __init__ method
        Args:
             self: This is the self object attribute
             size: This is the size of the square
        Returns:
             returns nothing
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
