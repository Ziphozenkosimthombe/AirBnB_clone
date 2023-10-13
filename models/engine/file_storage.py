#!/usr/bin/python3
<<<<<<< HEAD
from models.base_model import BaseModel
import json as js
import os

class FileStorage:
    __file_path = "file.json" # string - path to the JSON file (ex: file.json)
    __objects = {} # dictionary - empty but will store all objects by <class name>.id

    def all(self) -> dict:
        """ returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj) -> None:
        """sets in __objects the obj with key <obj class name>.id"""
        id = obj.id
        class_name = obj.__class__.__name__
        key = class_name + '.' + id
        FileStorage.__objects[key] = obj

    def save(self) -> None:
        """: serializes __objects to the JSON file (path: __file_path)"""
        with open(file=FileStorage.__file_path, mode='w', encoding='utf-8') as js_file:
            json_dict = {key: val.to_dict() for (key, val) in FileStorage.__objects.items()}
            js.dump(json_dict, js_file)

    def reload(self) -> None:
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
=======
"""file storange json"""
import json
from models.base_model import BaseModel
from models.user import User
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    """the file storage class"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return all the object classes in the Basemodel"""
        return self.__objects

    def new(self, obj):
        """will push the obj to the objects"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

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
>>>>>>> dae40e51c191d141474748eb5dcd95cfb95a8ee8
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
<<<<<<< HEAD
            with open(file=FileStorage.__file_path, mode='r', encoding='utf-8') as js_file:
                for key, val in js.load(js_file).items():
                    instance = eval(val['__class__'])(**val)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass

=======
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                for key, value in json.load(file).items():
                    construtor = eval(value['__class__'])(**value)
                    self.__objects[key] = construtor
        except FileNotFoundError:
            pass
>>>>>>> dae40e51c191d141474748eb5dcd95cfb95a8ee8
