#!/usr/bin/python3
"""unittest module for the Review class"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from models import storage
from datetime import datetime


class TestReview(unittest.TestCase):
    """the test case for review"""
    review = Review()
    review.place_id = "p-123"
    review.user_id = "user-321"
    review.text = "good place"

    def setUp(self):
        self.review = Review(
                place_id = "p-123",
                user_id = "user-321",
                text = "good place",
                id = "12345",
                created_at = "2023-01-01T12:00:00.000000",
                updated_at = "2023-01-02T12:00:00.000000",
            )
    def test_InitWithNoKwargs(self):
        """test the function when no kwargs are given"""
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

        self.assertEqual(self.review.place_id, "p-123")
        self.assertEqual(self.review.user_id, "user-321")
        self.assertEqual(self.review.text, "good place")

    def test_InitWithTheKwargs(self):
        """test the function when the kwargs are given"""
        reviewDict = {
            "id": "1111-1111-123",
            "created_at": "2023-01-01T12:00:00.000000",
            "updated_at": "2023-01-02T12:00:00.000000",
            "place_id": "p-2001",
            "user_id": "1979",
            "text": "good place to stay during holidays"
        }
        reviewObject = Review(**reviewDict)
        self.assertIsInstance(reviewObject.id, str)
        self.assertIsInstance(reviewObject.created_at, datetime)
        self.assertIsInstance(reviewObject.updated_at, datetime)
        self.assertIsInstance(reviewObject.place_id, str)
        self.assertIsInstance(reviewObject.user_id, str)
        self.assertIsInstance(reviewObject.text, str)
        self.assertIsInstance(reviewObject, Review)

        self.assertEqual(reviewObject.id, reviewDict["id"])
        self.assertNotEqual(reviewObject.created_at.isoformat(),
                         reviewDict["created_at"])
        self.assertNotEqual(reviewObject.updated_at.isoformat(),
                         reviewDict["updated_at"])
        self.assertEqual(reviewObject.place_id,
                         reviewDict["place_id"])
        self.assertEqual(reviewObject.user_id,
                         reviewDict["user_id"])
        self.assertEqual(reviewObject.text,
                         reviewDict["text"])
    
    def test_InitWithInvalidKwargs(self):
        """test the function when the kwargs coantain an invalid key"""
        reviewDict = {
                "__class__": "Review"
                }
        review = Review(**reviewDict)
        self.assertNotIn("__class__", review.__dict__)

    def test_str(self):
        """test __str__ method string representation"""
        n = self.review.__class__.__name__
        exStr = f"[{n}] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(self.review.__str__(), exStr)

    def test_save(self):
        """test save methods of the Review class"""
        review = Review()
        oldUpDatedAt = review.updated_at
        review.save()
        newUpDatedAt = review.updated_at
        self.assertNotEqual(oldUpDatedAt, newUpDatedAt)
        self.assertTrue(storage.save)

    def test_toDict(self):
        """test toDict method of the Review class"""
        reviewDict = self.review.to_dict()
        self.assertIsInstance(reviewDict, dict)
        self.assertEqual(reviewDict['__class__'],
                         "Review")
        self.assertNotEqual(reviewDict['created_at'],
                         self.review.created_at.isoformat())
        self.assertNotEqual(reviewDict["updated_at"],
                         self.review.updated_at.isoformat())
        self.assertEqual(reviewDict["id"],
                         self.review.id)
        self.assertEqual(reviewDict["place_id"],
                         self.review.place_id)
        self.assertEqual(reviewDict["user_id"],
                         self.review.user_id)
        self.assertEqual(reviewDict["text"],
                         self.review.text)


if __name__ == "__main__":
    unittest.main()
