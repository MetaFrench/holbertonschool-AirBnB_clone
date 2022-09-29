#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertIsNot(b1, b2)
