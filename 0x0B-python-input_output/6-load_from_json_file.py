#!/usr/bin/python3
""" This is the load from json file module """
import json


def load_from_json_file(filename):
    """ This function loads data from a json file """
    with open(filename, encoding="UTF8") as file:
        return (json.load(file))
