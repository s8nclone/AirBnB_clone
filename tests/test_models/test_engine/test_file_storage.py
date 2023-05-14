#!/usr/bin/python3
"""Test for file storage"""

import json
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    """Tests the `FileStorage` class."""

    def setUp(self):
        """Set up test fixtures"""
        # Change the file path to use a test file
        FileStorage._FileStorage__file_path = "test_file.json"

        # Create a new `FileStorage` instance.
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down test fixtures"""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        """Test that all method returns a dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test that new method adds an object to the __objects dictionary"""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save(self):
        """Test that save method creates a file"""

        self.storage._FileStorage__objects["BaseModel.1"] = BaseModel()
        # Save the `__objects` dictionary to the JSON file.
        self.storage.save()

        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        """Test that reload method loads objects from file"""

        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
