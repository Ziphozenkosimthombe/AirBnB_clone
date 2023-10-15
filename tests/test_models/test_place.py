#!/usr/bin/python3
"""unittest module for the Place class"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage
from datetime import datetime


class TestPlace(unittest.TestCase):
    """the test case for User"""
    place = Place()
    place.city_id = "city-480"
    place.user_id = "user-084"
    place.name = "MargetBnB"
    place.description = "Durban"
    place.number_rooms = 4
    place.number_bathrooms = 2
    place.max_guest = 4
    place.price_by_night = 300
    place.latitude = 20.12348
    place.longitude = 2.98732
    place.amenity_ids = ["am-1", "am-2"]
    place.id = "111-111-111-111"

    def setUp(self):
        pass

    def test_InitWithNoKwargs(self):
        """test the function when no kwargs are given"""
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

        self.assertEqual(self.place.id, "111-111-111-111")
        self.assertEqual(self.place.city_id, "city-480")
        self.assertEqual(self.place.user_id, "user-084")
        self.assertEqual(self.place.name, "MargetBnB")
        self.assertEqual(self.place.description, "Durban")
        self.assertEqual(self.place.number_rooms, 4)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 300)
        self.assertEqual(self.place.latitude, 20.12348)
        self.assertEqual(self.place.longitude, 2.98732)
        self.assertEqual(self.place.amenity_ids, ["am-1", "am-2"])

    def test_InitWithTheKwargs(self):
        """test the function when the kwargs are given"""
        placeDict = {
                "city_id": "city-102030",
                "user_id": "user-302010",
                "name": "southbeach",
                "description": "having the peace of mind see the ocean",
                "number_rooms": 8,
                "number_bathrooms": 6,
                "max_guest": 8,
                "price_by_night": 500,
                "latitude": 80.12348,
                "longitude": -90.98732,
                "amenity_ids": ["am-4", "am-5"],
                "id": "222-222-222-222",
                "created_at": "2023-01-01T12:00:00.000000",
                 "updated_at": "2023-01-02T12:00:00.000000"
        }
        placeObject = Place(**placeDict)
        self.assertIsInstance(placeObject.id, str)
        self.assertIsInstance(placeObject.created_at, datetime)
        self.assertIsInstance(placeObject.updated_at, datetime)
        self.assertIsInstance(placeObject.city_id, str)
        self.assertIsInstance(placeObject.user_id, str)
        self.assertIsInstance(placeObject.name, str)
        self.assertIsInstance(placeObject.description, str)
        self.assertIsInstance(placeObject.number_rooms, int)
        self.assertIsInstance(placeObject.number_bathrooms, int)
        self.assertIsInstance(placeObject.max_guest, int)
        self.assertIsInstance(placeObject.price_by_night, int)
        self.assertIsInstance(placeObject.latitude, float)
        self.assertIsInstance(placeObject.longitude, float)
        self.assertIsInstance(placeObject.amenity_ids, list)
        self.assertIsInstance(placeObject, Place)

        self.assertEqual(placeObject.id, placeDict["id"])
        self.assertNotEqual(placeObject.created_at.isoformat(),
                         placeDict["created_at"])
        self.assertNotEqual(placeObject.updated_at.isoformat(),
                         placeDict["updated_at"])
        self.assertEqual(placeObject.city_id, placeDict["city_id"])
        self.assertEqual(placeObject.user_id, placeDict["user_id"])
        self.assertEqual(placeObject.name, placeDict["name"])
        self.assertEqual(placeObject.description, placeDict["description"])
        self.assertEqual(placeObject.number_rooms, placeDict["number_rooms"])
        self.assertEqual(placeObject.number_bathrooms, placeDict["number_bathrooms"])
        self.assertEqual(placeObject.max_guest, placeDict["max_guest"])
        self.assertEqual(placeObject.price_by_night, placeDict["price_by_night"])
        self.assertEqual(placeObject.latitude, placeDict["latitude"])
        self.assertEqual(placeObject.longitude, placeDict["longitude"])
        self.assertEqual(placeObject.amenity_ids, placeDict["amenity_ids"])

    def test_InitWithInvalidKwargs(self):
        """test the function when the kwargs coantain an invalid key"""
        placeDict = {
                "__class__": "Place"
                }
        place = Place(**placeDict)
        self.assertNotIn("__class__", place.__dict__)

    def test_str(self):
        """test __str__ method string representation"""
        n = self.place.__class__.__name__
        exStr = f"[{n}] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(self.place.__str__(), exStr)

    def test_save(self):
        """test save methods of the Place class"""
        place = Place()
        oldUpDatedAt = place.updated_at
        place.save()
        newUpDatedAt = place.updated_at
        self.assertNotEqual(oldUpDatedAt, newUpDatedAt)
        self.assertTrue(storage.save)

    def test_toDict(self):
        """test toDict method of the Place class"""
        placeDict = self.place.to_dict()
        self.assertIsInstance(placeDict, dict)
        self.assertEqual(placeDict['__class__'],
                         "Place")
        self.assertNotEqual(placeDict['created_at'],
                         self.place.created_at.isoformat())
        self.assertNotEqual(placeDict["updated_at"],
                         self.place.updated_at.isoformat())
        self.assertEqual(placeDict["id"],
                         self.place.id)
        self.assertEqual(placeDict["city_id"], self.place.city_id)
        self.assertEqual(placeDict["user_id"],
                          self.place.user_id
                          )
        self.assertEqual(placeDict["name"],
                         self.place.name
                         )
        self.assertEqual(placeDict["description"],
                         self.place.description
                         )
        self.assertEqual(placeDict["number_rooms"],
                         self.place.number_rooms
                         )
        self.assertEqual(placeDict["number_bathrooms"],
                         self.place.number_bathrooms
                         )
        self.assertEqual(placeDict["max_guest"],
                         self.place.max_guest
                         )
        self.assertEqual(placeDict["price_by_night"],
                         self.place.price_by_night
                         )
        self.assertEqual(placeDict["latitude"],
                         self.place.latitude
                         )
        self.assertEqual(placeDict["longitude"],
                         self.place.longitude
                         )
        self.assertEqual(placeDict["amenity_ids"],
                         self.place.amenity_ids
                         )


if __name__ == "__main__":
    unittest.main()
