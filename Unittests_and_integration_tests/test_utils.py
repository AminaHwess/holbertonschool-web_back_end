#!/usr/bin/env python3
"""Parameterize a unit test"""

from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """test for utils.access_nested_ma"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """test_access_nested_map method test
        that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test_access_nested_map_exception method
        that test that a KeyError is raised"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])
