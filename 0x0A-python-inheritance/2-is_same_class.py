#!/usr/bin/python3

""" This the is_same_class """


def is_same_class(obj, a_class):
    """ This class compares an object with a class name """
    if issubclass(type(obj), a_class):
        return False
    return isinstance(obj, a_class)
