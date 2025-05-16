#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1,2,3,4]), 4)
    
    def test_is_empty(self):
        self.assertEqual(max_integer([]), None)
    
    def test_not_int(self):
        with self.assertRaises(TypeError):
            max_integer(['h', 3])

if __name__ == '__main__':
    unittest.main()