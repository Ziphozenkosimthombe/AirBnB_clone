#!/usr/bin/python3
import json
import uuid
from datetime import datetime


class BaseModel:

	def __init__(self)->None:
		"""The constructor
		"""
		self.id = str(uuid.uuid4())
		self.created_at = datetime.utcnow()
		self.updated_at = datetime.utcnow()

	def __str__(self)->str:
		"""Returns a string representation of the class instance
		"""
		return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"

	def save(self)->None:
		"""updates the public instance attribute updated_at with the current datetime
		"""
		self.updated_at = datetime.utcnow()

	def to_dict(self)->dict:
		"""
		Returns a dictionary containing all keys/values of __dict__ of the instance
		"""
		dictionary = {key: val.isoformat() if key == 'created_at' or key == 'updated_at' else val for (key, val) in self.__dict__.items()}
		dictionary['__class__'] = BaseModel.__name__
		return  dictionary

