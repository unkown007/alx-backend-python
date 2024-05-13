#!/usr/bin/env python3
""" TestAccessNestedMap module
"""
from parameterized import parameterized
from typing import Dict
from unittest.mock import patch, Mock
import unittest

from utils import (nested_map, get_json)


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
        ({}, ("a",), "Invalid key"),
        ({"a": 1}, ("a", "b"), "Invalid key"),
    ])
    def test_access_nested_map_exception(self, _map, path, expected):
        """ Raise KeyError when some inputs are expected """
        with self.assertRaises(KeyError, msg=expected):
            nested_map(_map, path)


class TestGetJson(unittest.TestCase):
    """" Implements the TestGetJson.test_get_json """

    @parametized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict
            ) -> None:
        """ Test get_json from utils """

        attrs = {"json.return_value": test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)
