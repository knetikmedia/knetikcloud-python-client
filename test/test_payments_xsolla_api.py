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
from knetik_cloud.apis.payments_xsolla_api import PaymentsXsollaApi


class TestPaymentsXsollaApi(unittest.TestCase):
    """ PaymentsXsollaApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.payments_xsolla_api.PaymentsXsollaApi()

    def tearDown(self):
        pass

    def test_create_xsolla_token_url(self):
        """
        Test case for create_xsolla_token_url

        Create a payment token that should be used to forward the user to Xsolla so they can complete payment
        """
        pass


if __name__ == '__main__':
    unittest.main()
