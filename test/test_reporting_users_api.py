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
from swagger_client.apis.reporting_users_api import ReportingUsersApi


class TestReportingUsersApi(unittest.TestCase):
    """ ReportingUsersApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.reporting_users_api.ReportingUsersApi()

    def tearDown(self):
        pass

    def test_get_user_registrations(self):
        """
        Test case for get_user_registrations

        Get user registration info
        """
        pass


if __name__ == '__main__':
    unittest.main()