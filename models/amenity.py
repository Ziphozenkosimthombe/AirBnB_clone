#!/usr/bin/python3
'''Amenities Module'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity class inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """creating the instance constructor.
        Arg:
            id: the unique id.
            created_at: the date for created at.
            update_at: the date for updated at.
        """

        super().__init__(*args, **kwargs)
