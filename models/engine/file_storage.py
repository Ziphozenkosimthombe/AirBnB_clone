#!/usr/bin/python3
"""file storange json"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """the file storage class"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return all the object classes in the Basemodel"""
        return self.__objects

    def new(self, obj):
        """will push the obj to the objects"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serialize __objects to the JSON file (path: __file_path)"""
        myDict = {
                key: value.to_dict()
                for key, value in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(myDict, file, indent=4)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                for key, value in json.load(file).items():
                    construtor = eval(value['__class__'])(**value)
                    self.__objects[key] = construtor
        except FileNotFoundError:
            pass
