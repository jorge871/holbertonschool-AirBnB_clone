#!/usr/bin/python3
"""create city class that inerithance of the 'basemodel' class"""
from models.base_model import BaseModel


class City(BaseModel):
    """create the class city"""
    state_id = ""
    name = ""
