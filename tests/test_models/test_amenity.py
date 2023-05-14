#!/usr/bin/python3
"""
Unittest for Amenity class
"""

import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def setUp(self):
        """Set up test fixtures"""
        self.amenity = Amenity()
        self.amenity.name = "Wifi"

    def test_instance_creation(self):
        """Test that an instance of Amenity is created"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes_creation(self):
        """Test that attributes of Amenity are correctly created"""
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_attributes_type(self):
        """Test that attributes of Amenity have the correct type"""
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertIsInstance(self.amenity.name, str)

    def test_str_representation(self):
        """Test that __str__ returns the correct string"""
        expected_str = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_to_dict_method(self):
        """Test that to_dict method returns the correct dictionary"""
        expected_dict = {
            "id": self.amenity.id,
            "created_at": self.amenity.created_at.isoformat(),
            "updated_at": self.amenity.updated_at.isoformat(),
            "name": "Wifi",
            "__class__": "Amenity",
        }
        self.assertDictEqual(self.amenity.to_dict(), expected_dict)

    def test_save_method(self):
        """Test that save method updates the updated_at attribute"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)


if __name__ == "__main__":
    unittest.main()
