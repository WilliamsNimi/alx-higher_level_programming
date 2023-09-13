#!/usr/bin/python3
""" This is a JSON writer Module """
import json


def to_json_string(my_obj):
    """ This function returns the JSON rep of an object or string """
    if type(my_obj) == set:
        raise TypeError("Object of type set is not JSON serializable")
    return json.dumps(my_obj)
