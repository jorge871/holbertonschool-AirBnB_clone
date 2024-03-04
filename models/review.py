#!/usr/bin/python3
"""create review class that inerithance of the 'basemodel' class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """create the class review"""
    place_id = ""
    user_id = ""
    text = ""
