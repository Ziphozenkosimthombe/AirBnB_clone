#!/usr/bin/python3
"""Unittest module for the BaseModel Class"""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """the test case for BaseModel class"""
    base_model = BaseModel()

    def setUp(self):
        pass

    def test_InitWithNoKwargs(self):
        """test the function when no kwargs are
        given"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at,
                              datetime)
        self.assertIsInstance(base_model.updated_at,
                              datetime)
        self.assertNotEqual(base_model.created_at,
                            base_model.updated_at)

    def test_InitWithTheKwargs(self):
        """test the function when kwargs are given"""
        kwargsOnjects = {
            "id": "12345678910",
            "created_at": "2023-01-01T12:00:00.000000",
            "updated_at": "2023-01-02T12:00:00.000000",
            "name": "My First Model"
        }
        base_model = BaseModel(**kwargsOnjects)
        self.assertEqual(base_model.id, "12345678910")
        self.assertEqual(base_model.created_at,
                         datetime(2023, 1, 1, 12, 0))
        self.assertEqual(base_model.updated_at,
                         datetime(2023, 1, 2, 12, 0))
        self.assertEqual(base_model.name, "My First Model")

    def test_InitWithInvalidKwargs(self):
        """test the function when kwargs contain an invalid key"""
        kwargsObjests = {
            "__class__": "BaseModel"
        }
        base_model = BaseModel(**kwargsObjests)
        self.assertNotIn("__class__", base_model.__dict__)

    def test_str(self):
        """test __str__ method string representation"""
        n = self.base_model.__class__.__name__
        exStr = f"[{n}] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(self.base_model.__str__(), exStr)

    def test_save(self):
        """test save methos of the BaseModel class"""
        base_model = BaseModel()
        oldUpDateAt = base_model.updated_at
        base_model.save()
        newUpDatedAt = base_model.updated_at
        self.assertNotEqual(oldUpDateAt, newUpDatedAt)
        self.assertTrue(storage.save)

    def test_toDict(self):
        """test toDict methos of the BaseModel class"""
        base_model = BaseModel()
        baseModelDict = base_model.to_dict()
        self.assertIsInstance(baseModelDict, dict)
        self.assertEqual(baseModelDict['__class__'],
                         "BaseModel")
        self.assertNotEqual(baseModelDict['created_at'],
                         base_model.created_at.isoformat())
        self.assertNotEqual(baseModelDict["updated_at"],
                         base_model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
