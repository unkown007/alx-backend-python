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
