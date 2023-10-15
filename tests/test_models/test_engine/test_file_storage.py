#!/usr/bin/python3
"""module test"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from models.user import User
from models.place import Place
import json


class TestConstrutor(unittest.TestCase):

    def test_init(self):
        file_storage = FileStorage()
        self.assertEqual(file_storage._FileStorage__file_path,
                         'file.json')

    def test_all(self):
        """the instance of the FileStorage"""
        file_storage = FileStorage()
        object1 = BaseModel()
        object2 = User()
        object3 = Place()
        file_storage._FileStorage__objects = {
            "BaseModel.1": object1,
            "User.2": object2,
            "Place.3": object3
        }
        self.assertEqual(file_storage.all(),
                         file_storage._FileStorage__objects)

    def test_new(self):
        """the instance of the FileStorage"""
        file_storage = FileStorage()
        obj = BaseModel()
        file_storage.new(obj)
        """check that the object is added to the objects
        dictionary with the correct key
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, file_storage._FileStorage__objects)
        self.assertEqual(file_storage._FileStorage__objects[key],
                         obj)

    def test_save(self):
        """instance of the FileStorage"""
        file_storage = FileStorage()
        obj = BaseModel()
        file_storage.new(obj)
        file_storage.save()
        """check that the json file is created and
        has the correct content"""
        with open(file_storage._FileStorage__file_path,
                  'r', encoding='utf-8') as file:
            data = json.load(file)
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.assertIn(key, data)
            self.assertNotEqual(data[key], obj.to_dict())

    def test_reload(self):
        """instance of the FileStorage"""
        file_storage = FileStorage()
        obj = BaseModel()
        file_storage.new(obj)
        """class the save method to create the Json file"""
        file_storage.save()
        file_storage._FileStorage__objects = {}
        file_storage.reload()
        """
        check that the object is restore in the
        objects dictionary
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, file_storage._FileStorage__objects)
        self.assertNotEqual(file_storage._FileStorage__objects[key].to_dict(),
                         obj.to_dict())


if __name__ == "__main__":
    unittest.main()
