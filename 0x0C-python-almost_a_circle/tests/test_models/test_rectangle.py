#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.
Unittest classes:
    TestRectangle_instantiation
    TestRectangle_width
    TestRectangle_height
    TestRectangle_x
    TestRectangle_y
    TestRectangle_order_of_initialization
    TestRectangle_area
    TestRectangle_update_args
    TestRectangle_update_kwargs
    TestRectangle_to_dictionary
"""

import io
import sys
import unittest
Base = __import__('models.base').Base
Rectangle = __import__('models.rectangle').Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_two_args(self):
        r1 = Rectangle(10, 2,)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)
