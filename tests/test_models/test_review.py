#!/usr/bin/python3
"""Test module for review module"""

import unittest
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review"""

    def setUp(self):
        """Setup Review object"""
        self.rev = Review()

    def test_instance_attributes(self):
        """Test instance attributes"""
        self.assertTrue(hasattr(self.rev, 'place_id'))
        self.assertEqual(self.rev.place_id, "")
        self.assertTrue(hasattr(self.rev, 'user_id'))
        self.assertEqual(self.rev.user_id, "")
        self.assertTrue(hasattr(self.rev, 'text'))
        self.assertEqual(self.rev.text, "")
        self.assertTrue(hasattr(self.rev, 'created_at'))
        self.assertTrue(isinstance(self.rev.created_at, datetime))
        self.assertTrue(hasattr(self.rev, 'updated_at'))
        self.assertTrue(isinstance(self.rev.updated_at, datetime))
        self.assertTrue(hasattr(self.rev, 'id'))
        self.assertTrue(isinstance(self.rev.id, str))

    def test_str_method(self):
        """Test __str__ method"""
        expected_str = "[Review] ({}) {}".format(
            self.rev.id, self.rev.__dict__)
        self.assertEqual(str(self.rev), expected_str)

    def test_save_method(self):
        """Test save method"""
        prev_updated_at = self.rev.updated_at
        self.rev.save()
        self.assertNotEqual(prev_updated_at, self.rev.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        rev_dict = self.rev.to_dict()
        self.assertEqual(rev_dict['__class__'], 'Review')
        self.assertIsInstance(rev_dict['created_at'], str)
        self.assertIsInstance(rev_dict['updated_at'], str)
        self.assertIsInstance(rev_dict['id'], str)

    def test_dict_to_instance(self):
        """Test dictionary to instance"""
        rev_dict = self.rev.to_dict()
        new_inst = Review(**rev_dict)
        self.assertEqual(new_inst.id, self.rev.id)
        self.assertEqual(new_inst.created_at, self.rev.created_at)
        self.assertEqual(new_inst.updated_at, self.rev.updated_at)
        self.assertEqual(new_inst.place_id, self.rev.place_id)
        self.assertEqual(new_inst.user_id, self.rev.user_id)
        self.assertEqual(new_inst.text, self.rev.text)


if __name__ == '__main__':
    unittest.main()
