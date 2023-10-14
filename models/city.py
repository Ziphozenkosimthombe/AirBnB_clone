#!/usr/bin/python3
'''City module'''
from models.base_model import BaseModel


class City(BaseModel):
    """city class inheerits from BaseModel"""

    """State.id"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
