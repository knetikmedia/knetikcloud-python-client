# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com.

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import knetik_cloud
from knetik_cloud.rest import ApiException
from knetik_cloud.apis.auth_tokens_api import AuthTokensApi


class TestAuthTokensApi(unittest.TestCase):
    """ AuthTokensApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.auth_tokens_api.AuthTokensApi()

    def tearDown(self):
        pass

    def test_delete_tokens(self):
        """
        Test case for delete_tokens

        Delete tokens by username, client id, or both
        """
        pass

    def test_get_token(self):
        """
        Test case for get_token

        Get a single token by username and client id
        """
        pass

    def test_get_tokens(self):
        """
        Test case for get_tokens

        List usernames and client ids
        """
        pass


if __name__ == '__main__':
    unittest.main()
