#!/usr/bin/python3

# -*- coding: utf-8 -*-
""" This module is the implementation of the geometric square """


class Square:
    """ This is the square class
    Attributes:
              _Square__size: This is the size of the square
    """
    _Square__size = None

    def __init__(self, size=0):
        """ This is the __init__ method
        Args:
            self: this is the object instatiation
            size: This is the size of the square
        Returns:
               returns nothing
        Raises:
               ValueError: Checks the value of the size
               TypeError: Checks the type of size
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
        """ This is the area method
        Args:
             self: this is the object instatiation
        Returns:
                returns the area of the square
        """
        return self._Square__size * self._Square__size

    def size(self):
        """ This is the size method
        Args:
             self: This is the object instatiation
        Returns:
               returns the size of the square
        """
        return self._Square__size

    def size(self, value):
        """ This is the size setter method
        Args:
             self: This is the object instatiation
             value: The value of the square to be set as size
        Returns:
               returns nothing
        Raises:
              TypeError: Checks the size of the integer
              ValueError: Checks the value of the integer
        """
        try:
            if type(value) == int:
                if value >= 0:
                    self._Square__size = value
                else:
                    raise ValueError("size must be >=0")
            else:
                raise TypeError("size must be an integer")
        except ValueError as er:
            print(er)
        except TypeError as err:
            print(err)

    def my_print(self):
        """ This is the my_print method. Prints the square
            using #
        Args:
             self: This is the object instatiation
        Returns:
                returns nothing
        """
        if self_Square__size == 0:
            print("")
        else:
            for i in range(self._Square__size):
                for i in range(self._Square__size):
                    print("#", end="")
                print("")
