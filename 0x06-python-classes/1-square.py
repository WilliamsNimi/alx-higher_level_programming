#!/usr/bin/python3

# -*- coding: utf-8 -*-
""" This module contains implementation of the geometric square"""


class Square:
    """ This is the Square class
    Attributes:
              _Square__size: This is the size of the square
    """
    _Square__size = None

    def __init__(self, size):
        """ This is the __init__ function.
        Args:
             self: the class object
             size: The size of the square
             Returns: Returns nothing
        """
        self._Square__size = size
