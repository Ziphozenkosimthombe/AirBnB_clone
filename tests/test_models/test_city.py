#!/usr/bin/python3
"""Unittest module for the City class"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage
from datetime import datetime


class TestCity(unittest.TestCase):
    """the test case for City class""" 
    def setUp(self):
        """instance of city test"""
        self.city = City(name = "Durban",
                state_id = "ND",
                id = '1111-1111',
                created_at = "2023-01-01T12:00:00.000000",
                updated_at = "2023-01-02T12:00:00.000000")

    def test_InitWithNoKwargs(self):
        base_model = BaseModel()
        city = City()
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertNotEqual(self.city.state_id, "")
        self.assertNotEqual(self.city.name, "")

    def test_InitWithTheKwargs(self):
        """test the function when kwargs are given"""
        myCityJson = self.city.to_dict()
        newCity = City(**myCityJson)
        self.assertIsInstance(newCity, City)
        self.assertIsInstance(newCity.created_at, datetime)
        self.assertIsInstance(newCity.updated_at, datetime)
        self.assertIsInstance(newCity.id, str)
        self.assertEqual(newCity.state_id, "ND")
        self.assertEqual(newCity.name, "Durban")
        self.assertEqual(newCity.id, '1111-1111')
        self.assertNotEqual(newCity, self.city)
        newCity.state_id = "ND"
        newCity.name = "Durban"
        newCity.save()
        self.assertEqual(newCity.state_id, "ND")
        self.assertEqual(newCity.name, "Durban")
        self.assertEqual(newCity.__dict__["name"], "Durban")
        self.assertEqual(newCity.__dict__["state_id"], "ND")

    def test_toDict(self):
        """test toDict methos of the Amenity class"""
        cityDict = self.city.to_dict()
        self.assertEqual(cityDict['__class__'],
                         "City")
        self.assertEqual(cityDict["name"],
                         "Durban")
        self.assertEqual(cityDict["state_id"],
                         "ND")
        self.assertIsInstance(cityDict["created_at"],
                              str)
        self.assertIsInstance(cityDict["updated_at"],
                              str)

    def test_save(self):
        """test save methods of the City class"""
        oldUpDatedAt = self.city.updated_at
        self.city.name = "Harding"
        self.city.save()
        newUpDatedAt = self.city.updated_at
        self.assertNotEqual(oldUpDatedAt, newUpDatedAt)
        self.assertTrue(storage.save)

    def test_str(self):
        """test __str__ method string representation"""
        n = self.city.__class__.__name__
        exStr = f"[{n}] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(self.city.__str__(), exStr)
