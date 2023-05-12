#!/usr/bin/python3
"""This is the base model for the AirBnB Clone project.
"""
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """Class Blueprint for other models
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialize a BaseModel object"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in {"created_at", "updated_at"}:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # print(f"\nBefore storage.new is called:\n {self}")
            storage.new(self)
            # print(f"\After storage.new is called:\n {self}")

    def __str__(self) -> str:
        """String representation of BaseModel object
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """Updates the public instance attribute 'updated_at'\
             with current datetime"""
        self.updated_at = datetime.now()
        # print(f"\nThe type of created_at during save in base model is
        # {type(self.created_at)}")
        storage.save()
        # print(f"\nAfter storage.save:\nThe type of created_at is
        # {type(self.created_at)}")

    def to_dict(self) -> dict:
        """Returns a dictionary containing all keys/value\
            of __dict__ of the instance
        """
        # It's quite important that a copy is made
        # so that the reference is not modified
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['created_at'] = new_dict['created_at'].isoformat()

        return new_dict
