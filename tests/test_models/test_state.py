#!/usr/bin/python3
"""unittest module for the State class"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage
from datetime import datetime


class TestState(unittest.TestCase):
    """the test case for State"""

    def setUp(self):
        self.state = State(name = "",
                created_at = "2023-01-01T12:00:00.000000",
                updated_at = "2023-01-02T12:00:00.000000",
                id = "GP-123"
                )

    def test_InitWithNoKwargs(self):
        """test the function when no kwargs are given"""
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)
        self.assertIsInstance(self.state.name, str)
        self.assertEqual(self.state.name, "")

    def test_InitWithTheKwargs(self):
        """test the function when the kwargs are given"""
        stateDict = {
                "id": "GP-123",
                "name": "Johannesburg",
                "created_at": "2023-01-01T12:00:00.000000",
                "updated_at": "2023-01-02T12:00:00.000000",
                }
        stateObject = State(**stateDict)
        self.assertIsInstance(stateObject.id, str)
        self.assertIsInstance(stateObject.created_at, datetime)
        self.assertIsInstance(stateObject.updated_at, datetime)
        self.assertIsInstance(stateObject, State)
        self.assertIsInstance(stateObject.name, str)

        self.assertEqual(stateObject.id, stateDict["id"])
        self.assertNotEqual(stateObject.created_at.isoformat(),
                         stateDict["created_at"])
        self.assertNotEqual(stateObject.updated_at.isoformat(),
                         stateDict["updated_at"])
        self.assertEqual(stateObject.name, stateDict["name"])


    def test_InitWithInvalidKwargs(self):
        """test the function when the kwargs coantain an invalid key"""
        stateDict = {
                "__class__": "State"
                }
        state = State(**stateDict)
        self.assertNotIn("__class__", state.__dict__)


    def test_str(self):
        """test __str__ method string representation"""
        n = self.state.__class__.__name__
        exStr = f"[{n}] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(self.state.__str__(), exStr)

    def test_save(self):
        """test save methods of the state class"""
        state = State()
        oldUpDatedAt = state.updated_at
        state.save()
        newUpDatedAt = state.updated_at
        self.assertNotEqual(oldUpDatedAt, newUpDatedAt)
        self.assertTrue(storage.save)

    def test_toDict(self):
        """test toDict method of the User class"""
        stateDict = self.state.to_dict()
        self.assertIsInstance(stateDict, dict)
        self.assertEqual(stateDict['__class__'],
                         "State")
        self.assertNotEqual(stateDict['created_at'],
                         self.state.created_at.isoformat())
        self.assertNotEqual(stateDict["updated_at"],
                         self.state.updated_at.isoformat())
        self.assertEqual(stateDict["id"],
                         self.state.id)
        self.assertEqual(stateDict["name"],
                         self.state.name)


if __name__ == "__main__":
    unittest.main()
