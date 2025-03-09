#!/usr/bin/env python3
"""Test file for client.py"""
from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock


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

    def test_public_repos_url(self):
        """Method that tests the
        _public_repo_url method
        """
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
            return_value={
                "repos_url": "https://api.github.com/orgs/myorg/repos",
                "id": 1234,
            },
        ):
            x = GithubOrgClient("hello")
            self.assertEqual(
                "https://api.github.com/orgs/myorg/repos", x._public_repos_url
            )

    @patch("client.get_json", return_value=[{"name": "elyes"},
                                            {"name": "mohamed"}])
    def test_public_repos(self, mocked_get_json):
        """Method that tests the
        _public_repos method"""

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mocked_public_repos_url:
            mocked_public_repos_url.return_value = """https://api.github.
                                                     com/orgs/adobe/repos"""
            x = GithubOrgClient("hello")
            result = x.public_repos()
            self.assertEqual(result, ["elyes", "mohamed"])
            mocked_public_repos_url.assert_called_once()
        mocked_get_json.assert_called_once()
