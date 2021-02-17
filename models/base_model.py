#!/usr/bin/python3
"""Module for BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """This is Base Class for this proyect"""

    def __init__(self, *args, **kargs):
        """
        Constructor method
        Arguments
            - *args: is a list with all individual arguments(won't be used)
            - **kargs: is a dictionary with all arguments
                    """
        if kargs:
            for k, v in kargs.items():
                if "__class__" == k:
                    pass
                elif "created_at" == k:
                    self.created_at = datetime.strptime(kargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == k:
                    self.updated_at = datetime.strptime(kargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Prints class description"""
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance atributte update_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict.updated({'__class__': self.__class__.__name__})
        my_dict.updated({'created_at': self.created_at.isoformat()})
        my_dict.updated({'update_at': self.update_at.isoformat()})
        return my_dict
