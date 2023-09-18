#!/usr/bin/python3
""" This is the Base class Module """
import json


class Base:
    """ This is the Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ This is the constructor function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """ This function dumps to json """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(list_objs):
        """ Save json to file """
        for items in list_objs:
            nme = items.__class__.__name__
            with open("{}.json".format(nme), mode='w', encoding='UTF8') as file:
                if list_objs is None:
                    file.write("[]")
                else:
                    file.write(Base.to_json_string(items.__dict__))

    @staticmethod
    def from_json_string(json_string):
        """ This is the from_json_string function """
        if json_string is None:
            return []
        return json.loads(json_string)

    def create(cls, **dictionary):
        """ This is the create function """
        if dictionary and len(dictionary) > 0:
            if cls.__name__ == "Square":
                obj = cls(1)
            else:
                obj = cls(1, 1)
            obj.update(**dictionary)
            return obj
        pass

    def load_from_file(cls):
        """ this is the load_from_file function """
        try:
            with open("{}.json".format(cls.__name__), mode='rw', encoding='UTF8') as file:
                filesArray = Base.from_json_string(file.read())
                return [cls.create(**k) for k in filesArray]
        except IOError:
            return []
