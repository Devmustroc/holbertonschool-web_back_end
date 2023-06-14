#!/usr/bin/env python3
"""Script Test client.py"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from typing import Dict, List, Callable


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Callable) -> None:
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

    def test_public_repos_url(self) -> None:
        """Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "test_url"}
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class._public_repos_url, "test_url")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Callable) \
            -> None:
        """
        Test that the list of repos is what you
        expect from the chosen payload.
        """
        mock_get_json.return_value = [{"name": "google"},
                                      {"name": "abc"}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "test_url"
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class.public_repos(), ["google", "abc"])
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()
