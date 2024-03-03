#!/usr/bin/python3
""" create file storage class """
import json
from models.base_model import BaseModel
import os.path


class FileStorage():
    """this is the class to handle the file operations of our
    interpreter"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return a dictionary with all objects in memory"""
        return FileStorage.__objects

    def new(self, obj):
        """Assigns to the object in the '__objects' set the value
        specified by the key '<object class name>.id'"""
        if obj:
            key = type(obj).__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """serialized a objects to file json"""
        s = {}
        for key, obj in FileStorage.__objects.items():
            s[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(s, f)

    def reload(self):
        """deserializes a objects to file json"""
        try:
            if os.path.isfile(FileStorage.__file_path):
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    for key, obj in json.loads(f.read()).items():
                        obj = eval(obj['__class__'])(**obj)
                        FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
