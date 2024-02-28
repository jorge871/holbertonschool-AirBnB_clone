#!/usr/bin/python3
"""Created class for this project"""
from datetime import datetime
import uuid


class BaseModel():
    """create class that will inherited by the other classes in this project"""
    def __init__(self, *args, **kwargs):
        """Initialize new basemodel"""
    
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now("%Y-%m-%dT%H:%M:%S.%f")


    def __str__(self):
        """ this is a representation of string"""
        return ("[{}] ({}) <{}>".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def save(self):
        """updates the public instance attribute created_at"""
        self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        return {
            "my_number": self.my_number,
            "name": self.name,
            "__class__": self.__class__.__name__,
            "updated_at": self.update_at,
            "id": self.id,
            "created_at": self.created_at
        }
