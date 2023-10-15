#!/usr/bin/python3
"""unittest module for the User class"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
from datetime import datetime


class TestUser(unittest.TestCase):
    """the test case for User"""
    base_model = BaseModel()
    user = User()

    def setUp(self):
        self.user = User()

    def test_InitWithNoKwargs(self):
        """test the function when no kwargs are given"""
        base_model = BaseModel()
        user = User()
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
    
    def test_InitWithTheKwargs(self):
        """test the function when the kwargs are given"""
        user_dict = {
            "id": "12345",
            "created_at": "2023-01-01T12:00:00.000000",
            "updated_at": "2023-01-02T12:00:00.000000",
            "first_name": "Zipho",
            "last_name": "ncayiyana",
            "emal": "user@example.com",
            "password": "54321"
        }
        userObject = User(**user_dict)
        self.assertIsInstance(userObject.id, str)
        self.assertIsInstance(userObject.created_at, datetime)
        self.assertIsInstance(userObject.updated_at, datetime)
        self.assertIsInstance(userObject.email, str)
        self.assertIsInstance(userObject.password, str)
        self.assertIsInstance(userObject.first_name, str)
        self.assertIsInstance(userObject.last_name, str)
        self.assertIsInstance(userObject, User)

        self.assertEqual(userObject.id, user_dict["id"])
        self.assertNotEqual(userObject.created_at.isoformat(),
                         user_dict["created_at"])
        self.assertNotEqual(userObject.updated_at.isoformat(),
                         user_dict["updated_at"])
        self.assertEqual(userObject.first_name,
                         user_dict["first_name"])
        self.assertEqual(userObject.last_name,
                         user_dict["last_name"])
        try:
            email = user_dict["emal"]
        except KeyError:
            print ("key 'email' does not exist")
        self.assertEqual(userObject.password,
                         user_dict["password"])

    def test_InitWithInvalidKwargs(self):
        """test the function when the kwargs coantain an invalid key"""
        user_dict = {
                "__class__": "User"
                }
        user = User(**user_dict)
        self.assertNotIn("__class__", user.__dict__)

    def test_str(self):
        """test __str__ method string representation"""
        n = self.user.__class__.__name__
        exStr = f"[{n}] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(self.user.__str__(), exStr)

    def test_save(self):
        """test save methods of the User class"""
        user = User()
        oldUpDatedAt = user.updated_at
        user.save()
        newUpDatedAt = user.updated_at
        self.assertNotEqual(oldUpDatedAt, newUpDatedAt)
        self.assertTrue(storage.save)

    def test_toDict(self):
        """test toDict method of the User class"""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'],
                         "User")
        self.assertNotEqual(user_dict['created_at'],
                         self.user.created_at.isoformat())
        self.assertNotEqual(user_dict["updated_at"],
                         self.user.updated_at.isoformat())
        first_name = user_dict.get("first_name", None)
        last_name = user_dict.get('las_name', None)
        email = user_dict.get("emal", None)
        password = user_dict.get('password', None)
        self.assertEqual(user_dict["id"],
                         self.user.id)


if __name__ == "__main__":
    unittest.main()
