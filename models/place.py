#!/usr/bin/python3
"""
Place Module, contains Place class
"""

from .base_model import BaseModel


class Place(BaseModel):
    """
    Inherits from BaseModel

    Attributes:
        city_id -> string, will be city.id
        user_id -> string, will be user.id
        name -> string
        description -> string
        number_rooms -> integer
        number_bathrooms -> integer
        max_guest -> integer
        price_by_night -> integer
        latitude -> float - 0.0
        longitude -> float - 0.0
        amenity_ids -> list of string, it will be the list of Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
