#!/usr/bin/python3

""" This is the MyInt class """


class MyInt(int):
    """ This is the MyInt class """
    ot = None

    def __init__(self, ot):
        """ This is the __init__ function """
        self.ot = ot

    def __eq__(self, other):
        """ This is the equality function """
        return self.ot != other

    def __ne__(self, other):
        """ This is the negation function """
        return self.ot == other
