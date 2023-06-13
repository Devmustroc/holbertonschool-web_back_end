#!/usr/bin/env python3
"""Unittests for utils.py"""
from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """TestAccessNestedMap class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)