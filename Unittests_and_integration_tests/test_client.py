#!/usr/bin/env python3
"""Test file for client.py"""
from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """Class that has methods
    used to test client.py methods
    """

    @parameterized.expand(
        [("google", "{message: google}"), ("abc", "{message: not found}")]
    )
    @patch("client.get_json")
    def test_org(self, org_name, expected, mocked_get_json):
        """Module that checks if the org method works properly"""
        mocked_get_json.return_value = expected
        x = GithubOrgClient(org_name)
        x.org
        self.assertEqual(x.org, expected)
        mocked_get_json.assert_called_once()
