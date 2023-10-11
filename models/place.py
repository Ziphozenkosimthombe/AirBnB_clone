#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """place class inherits from BaseModel"""

    """City.id"""
    city_is = ""
    """User.id"""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    """Amenity.id"""
    amenity_ids = 0.0

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
