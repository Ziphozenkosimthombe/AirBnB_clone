#!/usr/bin/python3
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
