#!/usr/bin/python3
"""Test module for user module"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Define TestState class
    """

    def setUp(self):
        """
        Method to set up the instance of the State class
        """
        self.state = State()

    def tearDown(self):
        """
        Method to tear down the instance of the State class
        """
        del self.state

    def test_instance(self):
        """
        Test that verifies if the instance is correctly created
        """
        self.assertIsInstance(self.state, State)

    def test_name(self):
        """
        Test that verifies if the name attribute is correctly created
        """
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_to_dict(self):
        """
        Test that verifies if the to_dict method returns the correct dictionary
        """
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(type(state_dict["created_at"]), str)
        self.assertEqual(type(state_dict["updated_at"]), str)

    def test_str(self):
        """
        Test that verifies if the __str__ method returns the correct string
        """
        string_repr = str(self.state)
        self.assertEqual(type(string_repr), str)
        self.assertTrue("[State]" in string_repr)
        self.assertTrue("id" in string_repr)
        self.assertTrue("created_at" in string_repr)
        self.assertTrue("updated_at" in string_repr)


if __name__ == '__main__':
    unittest.main()
