#!/usr/bin/python3
"""
This module contain functions
Serializes an instance to a JSON file
and deserializes JSONfile to instances
"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """
    Class that serializes an instance to a JSON file
    and deserializes JSONfile to instances
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City, "\
Place": Place, "Review": Review, "State": State, "User": User}

    def all(self):
        """Returns the dictionary '__objects'"""
        return (self.__objects)

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path)
        """
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dictionary, f)

    def reload(self):
        """
        Deserializes the JSON file(__file_path) to __objects
        only if JSON file exist
        """
        try:
            with open(__file_path, "r") as f:
                new_obj = json.load(f)
            for k, v in new_obj.items():
                obj = self.class_dict[v["__class__"]](**v)
                self.__objects[k] = obj
        except Exception:
            pass
