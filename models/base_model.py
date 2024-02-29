#!/usr/bin/python3
"""Created class for this project"""
from datetime import datetime
import uuid


class BaseModel():
    """create class that will inherited by the other classes in this project"""
    def __init__(self, *args, **kwargs):
        """Initialize new basemodel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """ this is a representation of string"""
        return ("[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
            ))

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        data = self.__dict__.copy()
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat() 
        data["__class__"] = self.__class__.__name__
        return data
