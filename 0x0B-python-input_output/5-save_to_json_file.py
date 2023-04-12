#!/usr/bin/python3
import json
""" This is a JSON to file module """


def save_to_json_file(my_obj, filename):
    """ This function saves JSON objects to file"""
    with open(filename, mode='w', encoding='UTF8') as file:
        file.write(json.dumps(my_obj))
