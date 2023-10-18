#!/usr/bin/python3
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

    def to_json(self, attrs=None):
        """ This function converts dictionary rep of the class to Json """
        obj_dict1 = self.__dict__
        obj_dict = {}
        if attrs is not None:
            for items in attrs:
                if items in obj_dict1:
                    obj_dict[items] = obj_dict1[items]
            return (obj_dict)
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        """This function reads and converts json to dictionary"""
        self.__dict__ = json
