#!/usr/bin/python3
"""
Amenity Module, contains Amenity class
"""

from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Inherits from BaseModel

    Attributes:
        name -> string
    """

    name = ""
