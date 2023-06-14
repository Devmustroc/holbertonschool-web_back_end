#!/usr/bin/env python3
"""Unittests for utils.py"""
from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Any, Mapping, Sequence


class TestAccessNestedMap(TestCase):
    """TestAccessNestedMap class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected_result: Any) -> None:
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected: Any) -> None:
        """Tests the access_nested_map function"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(expected, str(error.exception))


class TestGetJson(TestCase):
    """TestGetJson class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: dict) -> None:
        """Tests the get_json function"""
        config = {'return_value.json.return_value': test_payload}
        mock_obj = mock.Mock(**config)
        with mock.patch('requests.get', return_value=mock_obj):
            response = get_json(test_url)
            self.assertEqual(response, test_payload)