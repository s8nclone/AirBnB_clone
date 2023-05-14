#!/usr/bin/python3
"""
Unittest for City class
"""

import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up a City object to be used in the test cases"""
        self.city = City()

    def test_instance_creation(self):
        """Test that an instance of the City class is created"""
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """Test that the City object has the expected attributes"""
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_attribute_types(self):
        """Test that the City object has attributes of the correct type"""
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_to_dict(self):
        """Test that the to_dict method returns a dictionary"""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)

    def test_str_representation(self):
        """Test that the __str__ method returns the expected string"""
        expected_str = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected_str)


if __name__ == '__main__':
    unittest.main()
