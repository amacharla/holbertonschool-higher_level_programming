#!/usr/bin/python3
"""Unit tests for Base class"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class test_Base_class(unittest.TestCase):
    """ Test Base class """

    def test_id(self):
        """Test id attribute """
        self.a1, self.a2, self.a3 = Base(), Base(5), Base()

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b4.id, 5)
        self.assertEqual(self.b5.id, 4)

    def test_to_json_string(self):
        """ Test json string """
