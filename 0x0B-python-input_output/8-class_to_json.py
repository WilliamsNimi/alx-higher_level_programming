#!/usr/bin/python3
""" This is the Class to JSON Module """
import json


def class_to_json(obj):
    """ Converts class obj dict to json format """
    return json.dumps(obj.__dict__)
