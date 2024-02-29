#!/usr/bin/python3
""" create unittest for base model """
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_existence_of_attributes(self):
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "id"))

    def test_existence_of_type(self):
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertIsInstance(self.model.id, str)

    def test_if_it_updated(self):
        principal_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(principal_updated_at, new_updated_at)

    def test_if_dictionary_return(self):
        my_dict = self.model.to_dict()
        self.assertIsInstance(my_dict, dict)

    def test_if_dictionary_contains_all_attributes(self):
        my_dict = self.model.to_dict()
        self.assertIn("created_at", my_dict)
        self.assertIn("updated_at", my_dict)
        self.assertIn("id", my_dict)

    def test_if_dictionary_contains_the_correct_values(self):
        my_dict = self.model.to_dict()
        self.assertEqual(my_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(my_dict["updated_at"], self.model.updated_at.isoformat())
        self.assertEqual(my_dict["id"], self.model.id)

    def tests_how_the_string_is_represented(self):
        string_representation = str(self.model)
        self.assertIn(self.model.__class__.__name__, string_representation)
        self.assertIn(self.model.id, string_representation)
        self.assertIn(str(self.model.__dict__), string_representation)

if __name__ == "__main__":
    unittest.main()
