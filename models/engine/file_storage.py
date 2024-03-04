#!/usr/bin/python3
""" create file storage class """
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """this is the class to handle the file operations of our
    interpreter"""
    __file_path = "file.json"
    __objects = {}

    classes = {
            "BaseModel": BaseModel,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User
        }

    def __init__(self):
        """init self"""
        pass

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
        s = {}
        for key, obj in self.__objects.items():
            s[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(s, f)

    def reload(self):
        """deserializes a objects to file json"""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
            for key, value in data.items():
                class_name, obj_id = key.split(".")
                obj = globals()[class_name](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
