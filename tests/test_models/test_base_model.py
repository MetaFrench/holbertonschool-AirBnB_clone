#!/usr/bin/python3
"""test module for BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    """tests BaseModel class"""

    def setUp(self):
        self.b1 = BaseModel()
        self.b2 = BaseModel()
        self.b3 = BaseModel(created_at='2022-10-03T10:37:52.844475', updated_at='2022-10-03T10:37:52.844475', id='1', )

    def tearDown(self):
        del self.b1
        del self.b2
        del self.b3
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_init(self):
        self.assertNotEqual(self.b1.id, self.b2.id)
        self.assertTrue(hasattr(self.b1, 'created_at'))
        self.assertTrue(hasattr(self.b1, 'updated_at'))
        self.assertEqual(self.b3.id, '1')
        self.assertIsInstance(self.b3.updated_at, datetime)
        self.assertIsInstance(self.b3.created_at, datetime)

    def test_str(self):
        self.assertEqual(self.b3.__str__(), "[BaseModel] (1) {'created_at': datetime.datetime(2022, 10, 3, 10, 37, 52, 844475), 'updated_at': datetime.datetime(2022, 10, 3, 10, 37, 52, 844475), 'id': '1'}")

    def test_save(self):
        old = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(old, self.b1.updated_at)


    def test_to_dict(self):
        self.assertEqual(self.b3.to_dict(), {'__class__': 'BaseModel', 'created_at': '2022-10-03T10:37:52.844475', 'id': '1', 'updated_at': '2022-10-03T10:37:52.844475'})
