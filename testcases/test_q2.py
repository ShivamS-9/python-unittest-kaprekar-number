import unittest
import sys
sys.path.append("../Code")
from kaprekarroutine import cal_func

class Test(unittest.TestCase):
    def test_4dig_valid_num(self):
        result = cal_func(2123)
        self.assertEqual(result, 6174)

    def test_4dig_valid_num_leading_0(self):
        result = cal_func('0176')
        self.assertEqual(result, 6174)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            cal_func(1111)

        with self.assertRaises(ValueError):
            cal_func(0000)

    def test_input_descending_order(self):
        result = cal_func(8731)
        self.assertEqual(result, 6174)

    def test_input_ascending_order(self):
        result = cal_func(1234)
        self.assertEqual(result, 6174)

    def test_same_digits_input(self):
        self.assertRaises(ValueError, cal_func, 2222)

    def test_negative_input(self):
        self.assertRaises(ValueError, cal_func, -7634)
            
    def test_empty_input(self):
        self.assertRaises(ValueError, cal_func, '')

    def test_non_integer_input(self):
        self.assertRaises(ValueError, cal_func, 'dassssss')
