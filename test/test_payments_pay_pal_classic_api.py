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
from swagger_client.apis.payments_pay_pal_classic_api import PaymentsPayPalClassicApi


class TestPaymentsPayPalClassicApi(unittest.TestCase):
    """ PaymentsPayPalClassicApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.payments_pay_pal_classic_api.PaymentsPayPalClassicApi()

    def tearDown(self):
        pass

    def test_create_pay_pal_billing_agreement_url(self):
        """
        Test case for create_pay_pal_billing_agreement_url

        Create a PayPal Classic billing agreement for the user
        """
        pass

    def test_create_pay_pal_express_checkout(self):
        """
        Test case for create_pay_pal_express_checkout

        Create a payment token for PayPal express checkout
        """
        pass

    def test_finalize_pay_pal_billing_agreement(self):
        """
        Test case for finalize_pay_pal_billing_agreement

        Finalizes a billing agreement after the user has accepted through PayPal
        """
        pass

    def test_finalize_pay_pal_checkout(self):
        """
        Test case for finalize_pay_pal_checkout

        Finalizes a payment after the user has completed checkout with PayPal
        """
        pass


if __name__ == '__main__':
    unittest.main()
