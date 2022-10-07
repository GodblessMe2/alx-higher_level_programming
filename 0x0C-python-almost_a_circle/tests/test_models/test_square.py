#!/usr/bin/python3
"""Defines unittests for models/square.py.
Unittest classes:
    TestSquare_instantiation
    TestSquare_size
    TestSquare_x
    TestSquare_y
    TestSquare_order_of_initialization
    TestSquare_area
    TestSquare_stdout
    TestSquare_update_args
    TestSquare_update_kwargs
    TestSquare_to_dictionary
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class"""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Rectangle)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 5)
        s2 = Square(5, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 5, 2)
        s2 = Square(2, 5, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(2, 5, 10, 4, 6)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(2, 5, 10, 4).__size)

    def test_size_setter(self):
        s = Square(2, 5, 10, 4)
        s.size = 5
        self.assertEqual(5, s.size)

    def test_size_getter(self):
        self.assertEqual(2, Square(2, 5, 10, 4).size)

    def test_width_setter(self):
        s = Square(2, 5, 10, 4)
        s.size = 5
        self.assertEqual(5, s.width)

    def test_height_setter(self):
        s = Square(2, 5, 10, 4)
        s.size = 5
        self.assertEqual(5, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)

class TestSquare_size(unittest.TestCase):
    """Unittests for testing size instantiation of the Square class"""
    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(str, 3)

    def test_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid", 3)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square('string', 4)

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5, 4)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5), 4)

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({'a': 3, 'b': 8}, 4)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 2, 5], 4)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 2, 5), 4)

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 2, 5}, 4)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 5)

    class TestSquare_x(unittest.TestCase):
        """Unittests for testing initialization of Square x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None, 4)

    def test_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "invalid", 2)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 'string')

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 4.6, 6)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, complex(5), 4)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {'a': 3, 'b': 8}, 4)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, [1, 2, 2, 5], 4)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, (1, 2, 2, 5), 4)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {1, 2, 2, 5}, 4)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(3, -1, 4)

class TestSquare_y(unittest.TestCase):
    """Unittests for testing initialization of Square X attribute."""
    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, None)

    def test_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, "invalid")

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, 'string')

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 6, 4.6)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, {'a': 3, 'b': 8})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, [1, 2, 2, 5])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, (1, 2, 2, 5))

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, {1, 2, 2, 5})

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 4, -1)

class TestSquare_order_of_initialization(unittest.TestCase):
    """Unittests for testing order of Square attribute initialization."""
    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")

class TestSquare_area(unittest.TestCase):
    def test_area_equal(self):
        result = Square(10, 6, 0, 0)
        self.assertEqual(100, result.area())

    def test_area_change_attributes(self):
        result = Square(10, 6, 0, 0)
        result.height = 20
        result.width = 5
        self.assertEqual(100, result.area())

    def test_area_one_arg(self):
        result = Square(10, 6, 0, 0)
        with self.assertRaises(TypeError):
            result.area(1)

class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""
    def test_update_args_zero(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_one(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_update_args_two(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_args_three(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_update_args_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_more_than_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.width)

    def test_update_args_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.height)

    def test_update_args_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        s.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(s))

    def test_update_args_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_update_args_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -4)

    def test_update_args_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid", "invalid")


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of Square class."""

    def test_update_kwargs_one(self):
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        s = Square(10, 10, 10, 10)
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))

    def test_update_kwargs_three(self):
        s = Square(10, 10, 10, 10)
        s.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(s))

    def test_update_kwargs_four(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_update_kwargs_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=8)
        self.assertEqual(8, s.width)

    def test_update_kwargs_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=9)
        self.assertEqual(9, s.height)

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(s))

    def test_update_kwargs_invalid_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_kwargs_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(s))

class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""
    def test_to_dictionary_output(self):
        s = Square(10, 10, 10, 10)
        res = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertNotEqual(res, s.to_dictionary)

    def test_to_dictionary_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 10, 10, 1)
        s2 = Square(10, 10, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)
