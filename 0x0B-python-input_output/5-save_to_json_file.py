#!/usr/bin/python3
""" This is a JSON to file module """
import json


def save_to_json_file(my_obj, filename):
    """ This function saves JSON objects to file"""
    with open(filename, mode='w', encoding='UTF8') as file:
        file.write(json.dumps(my_obj))
