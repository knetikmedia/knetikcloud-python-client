# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

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
from swagger_client.apis.payments_stripe_api import PaymentsStripeApi


class TestPaymentsStripeApi(unittest.TestCase):
    """ PaymentsStripeApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.payments_stripe_api.PaymentsStripeApi()

    def tearDown(self):
        pass

    def test_create_customer_using_post1(self):
        """
        Test case for create_customer_using_post1

        Create a Stripe payment method for a user
        """
        pass

    def test_pay_invoice_using_post1(self):
        """
        Test case for pay_invoice_using_post1

        Pay with a single use token
        """
        pass


if __name__ == '__main__':
    unittest.main()
