#!/usr/bin/env python3
"""Unittests for utils.py"""
from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Mapping, Sequence


class TestAccessNestedMap(TestCase):
    """TestAccessNestedMap class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected: Any) -> None:
        """Tests the access_nested_map function"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(expected, str(err.exception))
