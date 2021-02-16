#!/usr/bin/python3
"""Module for BaseModel"""
import uuid
from datetime import datetime


class BaseModel():
    """This is Base Class for this proyect"""

    id = str(uuid.uuid4())
    created_at = datetime.now()
    update_at = datetime.now()

    def __str__(self):
        """Prints class description"""
        return ("[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__))
    
    def save(self):
        """
        Updates the public instance atributte update_at
        with the current datetime
        """
        self.update_at = datetime.now()
    
    def to_dict(self):
        """
        Return dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict.update({'__class__': self.__class__.__name__})
        my_dict.update({'created_at': self.created_at.isoformat()})
        my_dict.update({'update_at': self.update_at.isoformat()})
        return my_dict