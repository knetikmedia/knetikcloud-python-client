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
from knetik_cloud.apis.payments_apple_api import PaymentsAppleApi


class TestPaymentsAppleApi(unittest.TestCase):
    """ PaymentsAppleApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.payments_apple_api.PaymentsAppleApi()

    def tearDown(self):
        pass

    def test_verify_apple_receipt(self):
        """
        Test case for verify_apple_receipt

        Pay invoice with Apple receipt
        """
        pass


if __name__ == '__main__':
    unittest.main()
