#!/usr/bin/python3
"""
Review Module, contains Review class
"""

from .base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from BaseModel

    Attributes:
        place_id -> string, <Place.id>
        user_id -> string, <User.id>
        text -> string
    """

    place_id = ""
    user_id = ""
    text = ""
