#!/usr/bin/python3
"""
City Module, contains City class
"""

from .base_model import BaseModel


class City(BaseModel):
    """
    Inherits from BaseModel

    Attributes:
        name -> string
        state_id -> string
    """

    name = ""
    state_id = ""
