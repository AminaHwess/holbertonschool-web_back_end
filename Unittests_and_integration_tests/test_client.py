#!/usr/bin/env python3
"""Test file for client.py"""
from client import GithubOrgClient
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock
import requests
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repository, lics, expected):
        """test method used to test
        the has license method"""
        x = GithubOrgClient.has_license(repository, lics)
        self.assertEqual(x, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient.public_repos method."""

    @classmethod
    def setUpClass(cls):
        """Set up the test class."""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Side effect function for the mock."""
            if url.endswith("/orgs/google"):
                return Mock(json=lambda: cls.org_payload)
            elif url.endswith("/orgs/google/repos"):
                return Mock(json=lambda: cls.repos_payload)
            return Mock(json=lambda: {})  # Default case

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class."""
        cls.get_patcher.stop()
