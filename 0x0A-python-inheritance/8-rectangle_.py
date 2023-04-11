#!/usr/bin/python3


""" This is the rectangle Module """
class Rectangle(BaseGeometry):
    """ This is the rectangle class """
    _Rectangle__height = None
    _Rectangle__width = None

    def __init__(self, width, height):
        """ This is the __init__ function """
        self.integer_validator(width)
        self.integer_validator(height)
        self._Rectangle__height = height
        self._Rectangle__width = width
