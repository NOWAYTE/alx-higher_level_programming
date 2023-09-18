#!/usr/bin/python3
"""Unittest for max_integer()"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unitttest.TestCase):
    """unittest for max_integer"""


    def test_l(self):
        list_ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(list_ordered), 4)

    def test_u(self):
        list_unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(list_unorded), 4)

    def test_e(self):
        list_empty = []
        self.assertEqual(max_integer(empty), None)


    if __name__ == '__main__':
        unittest.main
