#!/usr/bin/python3
"""Unit tests for Base class"""

import unittest, json, sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class test_Base_class(unittest.TestCase):
    """ Test Base class """

    def setup(self):
        """ Redirect stdout to filestream """
        sys.stdout = StringIO()

    def teardown(self):
        """ Revert back stdout """
        sys.stdout = sys.__stdout__

    def test_id(self):
        """Test id attribute """
        self.a1, self.a2, self.a3 = Base(), Base(5), Base()

        self.assertEqual(self.a1.id, 1)
        self.assertEqual(self.a2.id, 5)
        self.assertEqual(self.a3.id, 2)

    def test_to_json_string(self):
        """ Test json string """

        self.assertEqual(Base.to_json_string(


