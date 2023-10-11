#!/usr/bin/python3
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
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(file=FileStorage.__file_path, mode='r', encoding='utf-8') as js_file:
                for key, val in js.load(js_file).items():
                    instance = eval(val['__class__'])(**val)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass

