# coding: utf-8

"""
    DagsHub API

    This API is used to interact with DagsHub.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.issues_api import IssuesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIssuesApi(unittest.TestCase):
    """IssuesApi unit test stubs"""

    def setUp(self):
        self.api = IssuesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_issue(self):
        """Test case for create_issue

        Create an issue  # noqa: E501
        """
        pass

    def test_edit_issue(self):
        """Test case for edit_issue

        Edit an issue  # noqa: E501
        """
        pass

    def test_get_issue(self):
        """Test case for get_issue

        Get a single issue  # noqa: E501
        """
        pass

    def test_list_repo_issues(self):
        """Test case for list_repo_issues

        List issues for a repository  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
