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
        """creating the instance constructor.
        Arg:
            id: the unique id.
            created_at: the date for created at.
            update_at: the date for updated at.
        """
        super().__init__(*args, **kwargs)
