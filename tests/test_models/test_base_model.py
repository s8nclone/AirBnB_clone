#!/usr/bin/python3
"""Test file for BaseModel
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests the `BaseModel` class."""

    def setUp(self) -> None:
        """Set up test fixtures, if any."""
        pass

    def tearDown(self) -> None:
        """Tear down test fixtures, if any."""
        pass

    def test_init(self):
        """Test that the object is initialized with the correct attributes"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertTrue(hasattr(model1, "id"))
        self.assertTrue(hasattr(model1, "created_at"))
        self.assertTrue(hasattr(model1, "updated_at"))
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model1.created_at, datetime)
        self.assertIsInstance(model1.updated_at, datetime)
        self.assertNotEqual(model1.id, model2.id)

    def test_str(self):
        """Test that the object's string representation is correct"""
        model = BaseModel()
        expected_str = f"[{type(model).__name__}] \
({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        """Test case for BaseModel save method"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test case for BaseModel to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(model_dict["id"], str)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
