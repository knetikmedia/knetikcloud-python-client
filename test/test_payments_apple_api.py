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
from swagger_client.apis.payments_apple_api import PaymentsAppleApi


class TestPaymentsAppleApi(unittest.TestCase):
    """ PaymentsAppleApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.payments_apple_api.PaymentsAppleApi()

    def tearDown(self):
        pass

    def test_verify_receipt_using_post(self):
        """
        Test case for verify_receipt_using_post

        Pay invoice with Apple receipt
        """
        pass


if __name__ == '__main__':
    unittest.main()
