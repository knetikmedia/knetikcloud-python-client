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
from knetik_cloud.apis.payments_api import PaymentsApi


class TestPaymentsApi(unittest.TestCase):
    """ PaymentsApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.payments_api.PaymentsApi()

    def tearDown(self):
        pass

    def test_create_payment_method(self):
        """
        Test case for create_payment_method

        Create a new payment method for a user
        """
        pass

    def test_delete_payment_method(self):
        """
        Test case for delete_payment_method

        Delete an existing payment method for a user
        """
        pass

    def test_get_payment_method(self):
        """
        Test case for get_payment_method

        Get a single payment method for a user
        """
        pass

    def test_get_payment_method_type(self):
        """
        Test case for get_payment_method_type

        Get a single payment method type
        """
        pass

    def test_get_payment_method_types(self):
        """
        Test case for get_payment_method_types

        Get all payment method types
        """
        pass

    def test_get_payment_methods(self):
        """
        Test case for get_payment_methods

        Get all payment methods for a user
        """
        pass

    def test_payment_authorization(self):
        """
        Test case for payment_authorization

        Authorize payment of an invoice for later capture
        """
        pass

    def test_payment_capture(self):
        """
        Test case for payment_capture

        Capture an existing invoice payment authorization
        """
        pass

    def test_update_payment_method(self):
        """
        Test case for update_payment_method

        Update an existing payment method for a user
        """
        pass


if __name__ == '__main__':
    unittest.main()
