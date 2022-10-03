#!/usr/bin/python3
"""test module for FileStorage class"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import pep8


class TestFileStorage(unittest.TestCase):
    """tests FileStorage class"""

    def setUp(self):
        self.f1 = FileStorage()
        self.b1 = BaseModel(created_at='2022-10-03T10:37:52.844475', updated_at='2022-10-03T10:37:52.844475', id='1', )

    def tearDown(self):
        del self.f1
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_all(self):
        self.assertIsInstance(self.f1.all(), dict)

    def test_new(self):
        self.f1.new(self.b1)
        for objs in self.f1.all().values():
            self.assertTrue(issubclass(objs.__class__, BaseModel))

    def test_save(self):
        if os.path.exists('file.json'):
            self.assertTrue(os.stat("file.json").st_size == 0)
        self.f1.save()
        self.assertFalse(os.stat("file.json").st_size == 0)
