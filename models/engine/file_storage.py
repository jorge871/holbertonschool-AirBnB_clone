#!/usr/bin/python3
""" create file storage class """
import json
from models import *


class FileStorage():
    """this is the class to handle the file operations of our
    interpreter"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return a dictionary with all objects in memory"""
        return self.__objects

    def new(self, obj):
        """Assigns to the object in the '__objects' set the value
        specified by the key '<object class name>.id'"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialized a objects to file json"""
        with open(self.__file_path, "w") as file:
            json.dump({key: value.to_dict() if hasattr(value, 'to_dict') else value for key, value in self.__objects.items()}, file)

    def reload(self):
        """deserializes a objects to file json"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    obj_class = value["__class__"]
                    del value["__class__"]
                    self.__objects[key] = eval(obj_class)(**value)
        except FileNotFoundError:
            pass
