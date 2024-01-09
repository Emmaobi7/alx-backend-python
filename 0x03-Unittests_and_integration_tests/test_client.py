#!/usr/bin/env python3
"""
client test module
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """
    tests for org
    no extanall http calls
    """
    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, x, mock_get):
        """
        test_org
        test for corect output
        """
        exp = {'key': 'value'}
        mock_get.return_value = exp
        git_client = GithubOrgClient(x)
        org_test = git_client.org
        self.assertEqual(org_test, exp)
        mock_get.assert_called_once()

    @patch('client.get_json',
           return_value=[{'name': 'google'}, {"name": 'face'}])
    def test_public_repos(self, mock_get):
        """
        test pblic repos and
        punlic repos url
        """
        with patch('client.GithubOrgClient._public_repos_url',
                   return_value='google') as git_pub:
            git_client = GithubOrgClient('x')
            res = git_client.public_repos()
            git_pub.assert_called_once()
            mock_get.assert_called_once_with('google')
            self.assertEqual(res, ["google", "face"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, lis, exp):
        """
        test for has_license
        correct out put
        """
        self.assertEqual(GithubOrgClient.has_license(repo, lis), exp)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGihthubOrgClient(unittest.TestCase):
    """
    integration testing class
    """
    @classmethod
    def setUpClass(cls):
        """
        pre arrange test variables
        """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        stop patcher
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        tests public repos
        """
        t = GithubOrgClient('goggle')
        assert True

    def test_public_repos_with_license(self, license="apache-2.0"):
        """
        test public repos with license
        """
        t = GithubOrgClient('goggle')
        assert True
