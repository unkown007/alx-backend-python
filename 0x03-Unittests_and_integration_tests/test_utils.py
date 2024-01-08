#!/usr/bin/env python3
""" TestAccessNestedMap module
"""
from parameterized import parameterized
import unittest


nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Nested Map tests
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, _map, path, expected):
        """ Test Nested Map return the expected value """
        self.assertEqual(nested_map(_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, _map, path):
        """ Raise KeyError when some inputs are expected """
        with self.assertRaises(KeyError, msg="Invalid key"):
            nested_map(_map, path)
