#!/usr/bin/python3
"""Created class for this project"""
from datetime import datetime
import uuid
import models

class BaseModel():
    """create class that will be inherited by the other classes in this project"""
    def __init__(self, *args, **kwargs):
        """Initialize new basemodel"""

        self.id = 
        self.created_at = datetime
        self.updated_at = datetime

    def save(self):
        """updates the public instance attribute updated_at"""
        self.update_at = datetime

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

