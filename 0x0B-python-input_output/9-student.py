#!/usr/bin/python3
import json
""" This is a Student class module """


class Student:
    """ This is the Student Class """
    first_name = ""
    last_name = ""
    age = None

    def __init__(self, first_name, last_name, age):
        """ This is the __init__ function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ This function converts dictionary rep of the class to Json """
        return json.dumps(vars(self))
