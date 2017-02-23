# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.util_security_api import UtilSecurityApi


class TestUtilSecurityApi(unittest.TestCase):
    """ UtilSecurityApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.util_security_api.UtilSecurityApi()

    def tearDown(self):
        pass

    def test_get_user_location_log(self):
        """
        Test case for get_user_location_log

        Returns the authentication log for a user
        """
        pass

    def test_get_user_token_details(self):
        """
        Test case for get_user_token_details

        Returns the authentication token details. Use /users endpoint for detailed user's info
        """
        pass


if __name__ == '__main__':
    unittest.main()