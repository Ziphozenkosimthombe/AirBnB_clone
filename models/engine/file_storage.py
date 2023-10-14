#!/usr/bin/python3
"""file storange json"""
import json
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
    class_list = {
            'BaseModel': BaseModel,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State,
            'User': User,
            'Amenity': Amenity
            }

    def all(self):
        """return all the object classes in the Basemodel"""
        return self.__objects

    def new(self, obj):
        """will push the obj to the objects"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serialize __objects to the JSON file (path: __file_path)"""
        myDict = {}
        for key, value in self.__objects.items():
            myDict[key] = value.to_dict()
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
                myDict = json.load(file)
                for key, value in myDict.items():
                    # instance = value['__class__']
                    if value['__class__'] in self.class_list.keys():
                        self.__objects[key] = self.class_list[
                                value['__class__']](**value)
        except FileNotFoundError:
            pass
