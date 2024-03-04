#!/usr/bin/python3
"""create place class that inerithance of the 'basemodel' class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """create the class place"""
    city_id = ""
    user_id = ""
    name = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
