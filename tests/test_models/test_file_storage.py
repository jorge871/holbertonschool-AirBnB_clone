#!/usr/bin/python3
""" created unittest for file storage """
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import *


class TestFileStorage(unittest.TestCase):
    """ class to test the File Storage methods """
    def setUp(self):
        self.storage = FileStorage()
        self.storage.reload()

    def test_if_variable_path_exists(self):
        """ check if path variable exists in the class """
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_if_variable_objects_exists(self):
        """ check if objects variable is initialized as empty dictionary """
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_if_return_all_objects_of_dictionary(self):
        """ check if return all objects from the dictionary """
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects,dict)

    def test_if_add_an_new_object_to_the_objects(self):
        """ check if added the new object into the objects list and save it """
        obj = BaseModel()
        self.storage.new(obj)
        obj_two = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(obj_two, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[obj_two], obj)

    def test_if_save_data_on_json_file(self):
        """ check if save data on a json file """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        with open(self.storage._FileStorage__file_path, "r") as file:
                data_saved = json.load(file)
        obj_two = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(obj_two, data_saved)
        self.assertEqual(data_saved[obj_two], obj.to_dict())

    def test_if_reload_the_data_of_json_file(self):
        """ check if load data of json file """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()

        obj_two = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(obj_two, self.storage._FileStorage__objects)

        reload_obj = self.storage._FileStorage__objects[obj_two]
        self.assertEqual(reload_obj.__dict__, obj.__dict__)

    def test_if_path_exist(self):
        """ check if exist a path """
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_if_all_data_reload(self):
        storage = FileStorage()
        storage.all().clear()
        storage.reload()
        self.assertFalse(len(storage.all()) < 0)

if __name__ == '__main__':
    unittest.main()
