#!/usr/bin/python3
"""
State Module, contains State class
"""

from .base_model import BaseModel


class State(BaseModel):
    """
    Inherits from BaseModel

    Attributes:
        name -> string
    """

    name = ""
