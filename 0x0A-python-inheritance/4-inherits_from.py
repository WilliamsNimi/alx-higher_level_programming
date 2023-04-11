#!/usr/bin/python3


def inherits_from(obj, a_class):
    """ This is a checker for inherited classes """
    return issubclass(type(obj), a_class)
