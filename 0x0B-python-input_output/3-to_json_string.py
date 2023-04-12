#!/usr/bin/python3
import json
""" This is a JSON writer Module """


def to_json_string(my_obj):
    """ This function returns the JSON rep of an object or string """
    if type(my_obj) == set:
        raise TypeError("{} is not a JSON serializable".format(my_obj))
    return json.dumps(my_obj)
