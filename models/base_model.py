#!/usr/bin/python3
"""the base module"""

from uuid import uuid4 as id4
from datetime import datetime as dt
import models


class BaseModel:
    """the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """creating the instance constructor.
        Arg:
            id: the unique id.
            created_at: the date for created at.
            update_at: the date for updated at.
        """
        if not kwargs:
            self.id = str(id4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            models.storage.new(self)

        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'updated_at':
                        self.updated_at = dt.fromisoformat(value)
                    elif key == 'created_at':
                        self.created_at = dt.fromisoformat(value)
                    else:
                        """Sets the named attribute on the given object
                        to the specified value.
                        """
                        setattr(self, key, value)

    def __str__(self):
        """__str__ or the string representation.
        with the string format."""
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """saving the update of the
        public instance,
        attribte updated_at."""
        self.updated_at = dt.now()
        models.storage.save()

    def to_dict(self):
        """the keys/values of __dict__,
        of the instance will be return as a dictionary."""

        """creating the a variable and assign it to the new copy of
        the dictionary that contains the attributes and values of
        the current instance of the class.
        """
        dictClass = self.__dict__.copy()
        dictClass['__class__'] = self.__class__.__name__
        dictClass['created_at'] = self.created_at.isoformat()
        dictClass['updated_at'] = self.updated_at.isoformat()
        return dictClass
