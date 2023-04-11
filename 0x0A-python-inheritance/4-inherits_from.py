#!/usr/bin/python3

""" This is the inherits from function """


def inherits_from(obj, a_class):
    """ This is a checker for inherited classes """
    return issubclass(type(obj), a_class)
