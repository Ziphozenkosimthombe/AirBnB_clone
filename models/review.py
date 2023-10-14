#!/usr/bin/python3
'''Review'''
from models.base_model import BaseModel


class Review(BaseModel):
    """review class inherits from BaseModel"""

    """Place.id"""
    place_id = ""
    """User.id"""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """creating the instance constructor.
        Arg:
            id: the unique id.
            created_at: the date for created at.
            update_at: the date for updated at.
        """

        super().__init__(*args, **kwargs)
