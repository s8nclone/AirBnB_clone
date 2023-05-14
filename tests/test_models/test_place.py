#!/usr/bin/python3
"""Test module for place module"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def setUp(self) -> None:
        """Set up test fixtures"""
        self.place = Place()

    def test_instance_creation(self):
        """Test if instance of Place class is properly created"""
        self.assertIsInstance(self.place, Place)
        self.assertEqual(type(self.place.id), str)
        self.assertEqual(type(self.place.created_at).__name__, "datetime")
        self.assertEqual(type(self.place.updated_at).__name__, "datetime")

    def test_attributes(self):
        """Test if attributes of Place class are properly set"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_save_method(self):
        """Test if save method updates updated_at attribute"""
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a dictionary"""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(type(place_dict["created_at"]), str)
        self.assertEqual(type(place_dict["updated_at"]), str)


if __name__ == '__main__':
    unittest.main()
