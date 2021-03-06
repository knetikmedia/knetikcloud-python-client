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
from knetik_cloud.apis.payments_transactions_api import PaymentsTransactionsApi


class TestPaymentsTransactionsApi(unittest.TestCase):
    """ PaymentsTransactionsApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.payments_transactions_api.PaymentsTransactionsApi()

    def tearDown(self):
        pass

    def test_get_transaction(self):
        """
        Test case for get_transaction

        Get the details for a single transaction
        """
        pass

    def test_get_transactions(self):
        """
        Test case for get_transactions

        List and search transactions
        """
        pass

    def test_refund_transaction(self):
        """
        Test case for refund_transaction

        Refund a payment transaction, in full or in part
        """
        pass


if __name__ == '__main__':
    unittest.main()
