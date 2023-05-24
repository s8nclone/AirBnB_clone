#!/usr/bin/python3
"""
User Module, contain User class
"""

from .base_model import BaseModel


class User(BaseModel):
    """
    Inherits from BaseModel

    Attributes:
        email -> string
        password -> string
        first_name -> string
        last_name -> string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
