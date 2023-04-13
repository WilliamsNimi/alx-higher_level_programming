#!/usr/bin/python3
""" This is the Class to JSON Module """


def class_to_json(obj):
    """ Converts class obj dict to json format """
    return (obj.__dict__)
