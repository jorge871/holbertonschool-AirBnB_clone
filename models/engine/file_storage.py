#!/usr/bin/python3
""" create file storage class """
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """this is the class to handle the file operations of our
    interpreter"""
    __file_path = "file.json"
    __objects = {}

    classes = {
            "BaseModel": BaseModel,
            "User": User
            }

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
        with open(FileStorage.__file_path, "w") as f:
            json.dump(s, f)

    def reload(self):
        """deserializes a objects to file json"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, obj in data.items():
                    class_name = key.split(".")[0]
                    if class_name in FileStorage.classes:
                        self.__objects[key] = self.classes[class_name](**obj)
                    """
                    obj_class = obj['__class__']
                    if obj_class in FileStorage.classes.keys():
                        existing_obj = FileStorage.__objects.get(key)
                        if existing_obj:
                            existing_obj.__dict__.update(obj)
                        else:
                            temp = self.classes[obj_class](**obj)
                            FileStorage.__objects[key] = temp
                            """
        except FileNotFoundError:
            pass
