#!/usr/bin/python3

# -*- coding: utf-8 -*-
""" This module is the implementation of a geometric square """


class Square:
    """ This is the Square class
    Attributes:
               size: This is the size of the square
               position: this is a position attribute required for print
    """
    size = None
    position = None

    def __init__(self, size=0, position=(0, 0)):
        """ This is the __init__ method
        Args:
             self: This is the object instantiation
             size: This is the size of the square
             position: This is the print position of the square
        Returns:
                returns nothing
        Raises:
              ValueError: Checks size of the size attribute
              TypeError: Checks the type of the size attribute
        """
        if len(position) == 2 and position[0] >= 0 and position[1] >= 0:
            if type(position[0]) == int and type(position[1]) == int:
                self.position = position
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise IndexError("position must be a tuple of 2 positive integers")
        if type(size) == int:
            if size >= 0:
                self.size = size
            else:
                raise ValueError("size must be >=0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ This is the area method
        Args:
             self: object instantiation
        Returns:
               returns the area of the square
        """
        return self.size * self.size

    def size(self):
        """ This is the size getter method
        Args:
            self: this is the object instantiation
        Returns:
               returns the size of the square
        """
        return self.size

    def size(self, value):
        """ This is the size setter method
        Args:
            self: this is the object instantiation
            value: this is the value to be made the size of the square
        Returns:
               returns nothing
        Raises:
              ValueError: Checks the value of the size is greater than 0
              TypeError: Checks the type of the size
        """
        if type(value) == int:
            if value >= 0:
                self.size = value
            else:
                raise ValueError("size must be >=0")
        else:
            raise TypeError("size must be an integer")

    def position(self):
        """ This is the position getter method
        Args:
            self: this is the object instantiation
        Returns:
               returns the position of the square
        """
        return self.position

    def position(self, value):
        """ This is the position setter method
        Args:
            self: this is the object instantiation
            value: this is the value to be made the size of the square
        Returns:
               returns nothing
        Raises:
              ValueError: Checks the value of the size is greater than 0
              TypeError: Checks the type of the size
        """
        if type(value[0]) == int and type(value[1]) == int:
            if value[0] < 0 or value[1] < 0:
                self.position = value
            else:
                raise Exception("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """ This is the my_print method
        Args:
             self: This is the object instatiation
        Returns:
               returns nothing
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for i in range(self.position[0]):
                    if self.position[1] >= 0 and self.position[0] > 0:
                        print(" ", end="")
                for i in range(self.size):
                    print("#", end="")
                print("")

    def __str__(self):
        """ This is the __repr__ method
        Args:
             self: This is the object instatantiation
        Return:
              returns nothing
        """
        self.my_print()
        return ""
