#!/usr/bin/python3
'''User Module'''
from models.base_model import BaseModel


class User(BaseModel):
    """class User inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __inti__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
