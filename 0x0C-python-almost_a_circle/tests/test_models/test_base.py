#!/usr/bin/python3

"""Contains tests for the Base Class"""

import unittest
import os
# from base import Base
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
