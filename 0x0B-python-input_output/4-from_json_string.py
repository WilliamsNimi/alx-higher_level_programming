#!/usr/bin/python3
""" This is a JSON loader module """
import json


def from_json_string(my_str):
    """ This function returns strings from json objects """
    return json.loads(my_str)
