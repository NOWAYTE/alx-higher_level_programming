#!/usr/bin/python3

"""Unittests for max_integer([..])."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittests for max_integer([..])."""

    def test_ordered_list(self):
        o = [1, 2, 3, 4]
        self.assertEqual(max_integer(o), 4)

    def test_unordered_list(self):
        u = [1, 2, 4, 3]
        self.assertEqual(max_integer(u), 4)

    def test_max_at_begginning(self):
        m = [4, 3, 2, 1]
        self.assertEqual(max_integer(m), 4)

    def test_empty_list(self):
        e = []
        self.assertEqual(max_integer(e), None)

    def test_one_element_list(self):
        one = [7]
        self.assertEqual(max_integer(one), 7)

    def test_floats(self):
        f = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(f), 15.2)

    def test_ints_and_floats(self):
        i = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(i), 15.5)

    def test_s(self):
        string = "Ben"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        strings = ["Ben", "i", "y", "am"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
