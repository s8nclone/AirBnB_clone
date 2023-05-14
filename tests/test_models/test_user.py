#!/usr/bin/python3
"""Test module for user module"""

import os
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Tests the `User` class."""

    def setUp(self):
        """Set up test fixtures"""
        storage._FileStorage__file_path = "test_storefile.json"
        self.user = User()
        self.user.first_name = "Betty"
        self.user.last_name = "Bar"
        self.user.email = "testers.airbnb@mail.com"
        self.user.password = "root"
        self.user.save()

    def tearDown(self) -> None:
        """Tear down test fixtures"""
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_has_email_attribute(self):
        """Test for email attribute"""
        self.assertTrue(hasattr(self.user, 'email'))

    def test_has_password_attribute(self):
        """Test for password attribute"""
        self.assertTrue(hasattr(self.user, 'password'))

    def test_has_first_name_attribute(self):
        """Test for first_name attribute"""
        self.assertTrue(hasattr(self.user, 'first_name'))

    def test_has_last_name_attribute(self):
        """Test for last_name attribute"""
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_is_subclass_of_base_model(self):
        """Test is class is sub class of BaseModel attribute"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_attributes_are_strings(self):
        """Test if attributes are of string type"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_user_inherits_base_model_attributes(self):
        """Test that user inherits some attributes from base model"""
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_user_str_representation(self):
        """Test user string representation"""
        expected_output = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected_output)

    def test_user_to_dict_method(self):
        """Test conversion of object to dict"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], self.user.email)
        self.assertEqual(user_dict['password'], self.user.password)
        self.assertEqual(user_dict['first_name'], self.user.first_name)
        self.assertEqual(user_dict['last_name'], self.user.last_name)
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['created_at'],
                         self.user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'],
                         self.user.updated_at.isoformat())
