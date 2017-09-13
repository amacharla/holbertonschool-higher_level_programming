#!/usr/bin/python3
""" Unittest for Rectangle class """

import unittest
import json
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class test_Rectangle_class(unittest.TestCase):
    """ Test Base class """

    @classmethod
    def setUpClass(cls):
        """ Create Valid Instances of Rectangle class """
        cls.r1 = Rectangle(1, 2)
        cls.r2 = Rectangle(3, 4, 5, 6)
        cls.r3 = Rectangle(7, 8, 9, 10, 11)
        sys.stdout = StringIO()

    @classmethod
    def tearDownClass(self):
        """ Revert back stdout """
        sys.stdout = sys.__stdout__

    def test_arg_id(self):
        """Test id attribute """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 11)

    def test_arg_width(self):
        """ Test width """
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r2.width, 3)
        self.assertEqual(self.r3.width, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 1)
            Rectangle((2,), 1)
            Rectangle([2], 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 1)

    def test_arg_height(self):
        """ Test height """
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 4)
        self.assertEqual(self.r3.height, 8)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
            Rectangle(1, (2,))
            Rectangle(1, [2])
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -1)

    def test_arg_x_y(self):
        """ Test x and y """
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 5)
        self.assertEqual(self.r3.x, 9)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3, 4)

        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 6)
        self.assertEqual(self.r3.y, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_method_area(self):
        """ Test area """
        self.assertEqual(self.r1.area(), 2)
        self.assertEqual(self.r2.area(), 12)
        self.assertEqual(self.r3.area(), 56)


