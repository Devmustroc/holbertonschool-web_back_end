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
        mock_response = mock.Mock()
        mock_response.json.return_value = test_payload
        with mock.patch('requests.get', return_value=mock_response):
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mock_response.json.assert_called_once()

class TestMemoize(TestCase):
    """TestMemoize class"""
    def test_memoize(self) -> None:
        """Tests the memoize function"""
        class TestClass:
            """TestClass class"""
            def a_method(self):
                """a_method method"""
                return 42

            @memoize
            def a_property(self):
                """a_property method"""
                return self.a_method()
        with mock.patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test = TestClass()
            test.a_property
            test.a_property
            mock_method.assert_called_once()
