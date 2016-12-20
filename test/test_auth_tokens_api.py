# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.auth_tokens_api import AuthTokensApi


class TestAuthTokensApi(unittest.TestCase):
    """ AuthTokensApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.auth_tokens_api.AuthTokensApi()

    def tearDown(self):
        pass

    def test_delete_token_using_delete(self):
        """
        Test case for delete_token_using_delete

        Delete all tokens by username
        """
        pass

    def test_delete_token_with_client_id_using_delete(self):
        """
        Test case for delete_token_with_client_id_using_delete

        Delete a token by username and client id
        """
        pass

    def test_get_token_by_user_using_get(self):
        """
        Test case for get_token_by_user_using_get

        Get a single token by username and client id
        """
        pass

    def test_get_tokens_using_get(self):
        """
        Test case for get_tokens_using_get

        List usernames and client ids
        """
        pass


if __name__ == '__main__':
    unittest.main()