#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_beginning(self):
        self.assertEqual(max_integer([5, 1, 2, 3, 4]), 5)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_one_negative(self):
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_max_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_max_one_el(self):
        self.assertEqual(max_integer([1]), 1)

    def test_is_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_not_int(self):
        with self.assertRaises(TypeError):
            max_integer(['h', 3])


if __name__ == '__main__':
    unittest.main()
