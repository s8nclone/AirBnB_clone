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

    def test_instance_creation(self):
        """Test that an instance of Amenity is created"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertEqual(type(self.amenity.id), str)
        self.assertEqual(type(self.amenity.created_at).__name__, "datetime")
        self.assertEqual(type(self.amenity.updated_at).__name__, "datetime")

    def test_attributes_creation(self):
        """Test that attributes of Amenity are correctly created"""
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

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
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(type(amenity_dict["created_at"]), str)
        self.assertEqual(type(amenity_dict["updated_at"]), str)

    def test_save_method(self):
        """Test that save method updates the updated_at attribute"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)


if __name__ == "__main__":
    unittest.main()
