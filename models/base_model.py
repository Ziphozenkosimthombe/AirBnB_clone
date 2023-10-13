#!/usr/bin/python3
<<<<<<< HEAD
import models
from datetime import datetime
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        """The constructor"""

        if kwargs is not None and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(val)
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(val)
                elif key == '__class__':
                    # __class__ should not be added as an attribute
                    continue
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self) -> str:
        """
        Returns a string representation of the class instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self) -> None:
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self) -> dict:
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        new_dict = {k: v.isoformat() if k == 'created_at' or k == 'updated_at'
                    else v for (k, v) in self.__dict__.items()}
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
=======
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
                        self.updated_at = (dt.strptime(kwargs['updated_at'],
                                                       "%Y-%m-%dT%H:%M:%S.%f"))
                    elif key == 'created_at':
                        self.created_at = (dt.strptime(kwargs['created_at'],
                                                       "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        """Sets the named attribute on the given object
                        to the specified value.
                        """
                        setattr(self, key, value)

    def __str__(self):
        """__str__ or the string representation.
        with the string format."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

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
        dictClass['created_at'] = dt.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        dictClass['updated_at'] = dt.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dictClass
>>>>>>> dae40e51c191d141474748eb5dcd95cfb95a8ee8
