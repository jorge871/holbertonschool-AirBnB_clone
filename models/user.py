#!/usr/bin/python3
"""create user class that inerithance of the 'basemodel' class"""
from models.base_model import BaseModel


class User(BaseModel):
    """create the class user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """init user"""
        super().__init__(*args, **kwargs)
