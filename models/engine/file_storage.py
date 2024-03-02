#!/usr/bin/python3
""" create file storage class """
import json
from models.base_model import *


class FileStorage():
    """this is the class to handle the file operations of our
    interpreter"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """reload"""
        self.reload()

    def all(self):
        """return a dictionary with all objects in memory"""
        return self.__objects

    def new(self, obj):
        """Assigns to the object in the '__objects' set the value
        specified by the key '<object class name>.id'"""
        if obj is not None:
            FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serialized a objects to file json"""
        with open(self.__file_path, "w") as f:
            json.dump({key: value.to_dict() if hasattr(value, 'to_dict') else value for key, value in self.__objects.items()}, f)

    def reload(self):
        """deserializes a objects to file json"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    """obj_class = value["__class__"]"""
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
