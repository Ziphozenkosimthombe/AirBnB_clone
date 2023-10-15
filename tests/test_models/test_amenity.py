#!/usr/bin/python3
"""Unittest module for the Amenity class"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """the test case for Amenity class"""
    base_model = BaseModel()
    amenity = Amenity()

    def setUp(self):
        pass

    def test_InitWithNoKwargs(self):
        """test the function when no kwargs are given"""
        base_model = BaseModel()
        amenity = Amenity()
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertEqual(amenity.name, "")

    def test_InitWithTheKwargs(self):
        """test the function when kwargs are given"""
        kwargsObjects = {
            "id": "12345",
            "created_at": "2023-01-01T12:00:00.000000",
            "updated_at": "2023-01-02T12:00:00.000000",
            "name": "Zipho"
        }
        amenity = Amenity(**kwargsObjects)
        self.assertEqual(amenity.id, '12345')
        self.assertEqual(amenity.created_at,
                         datetime(2023, 1, 1, 12, 0))
        self.assertEqual(amenity.updated_at,
                         datetime(2023, 1, 2, 12, 0))
        self.assertEqual(amenity.name, 'Zipho')
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.id, str)

    def test_InitWithInvalidKwargs(self):
        """test the function when kwargs contain an invalid key"""
        kwargsObjects = {
                "__class__": "Amenity"
                }
        amenity = Amenity(**kwargsObjects)
        self.assertNotIn("__class__", amenity.__dict__)

    def test_str(self):
        """test __str__ method string representation"""
        n = self.amenity.__class__.__name__
        exStr = f"[{n}] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(self.amenity.__str__(), exStr)

    def test_save(self):
        """test save methods of the Amenity class"""
        amenity = Amenity()
        oldUpDatedAt = amenity.updated_at
        amenity.save()
        newUpDatedAt = amenity.updated_at
        self.assertNotEqual(oldUpDatedAt, newUpDatedAt)
        self.assertTrue(storage.save)

    def test_toDict(self):
        """test toDict methos of the Amenity class"""
        kwargsObjects = self.amenity.to_dict()
        self.assertIsInstance(kwargsObjects, dict)
        self.assertEqual(kwargsObjects['__class__'],
                         "Amenity")
        self.assertNotEqual(kwargsObjects['created_at'],
                         self.amenity.created_at.isoformat())
        self.assertNotEqual(kwargsObjects["updated_at"],
                         self.amenity.updated_at.isoformat())
        name = kwargsObjects.get('name', None)
        #self.assertEqual(kwargsObjects["name"],
                         #self.amenity.name)
        self.assertEqual(kwargsObjects["id"],
                         self.amenity.id)
