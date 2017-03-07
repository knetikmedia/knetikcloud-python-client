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
from swagger_client.apis.payments_optimal_api import PaymentsOptimalApi


class TestPaymentsOptimalApi(unittest.TestCase):
    """ PaymentsOptimalApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.payments_optimal_api.PaymentsOptimalApi()

    def tearDown(self):
        pass

    def test_silent_post_optimal(self):
        """
        Test case for silent_post_optimal

        Initiate silent post with Optimal
        """
        pass


if __name__ == '__main__':
    unittest.main()
