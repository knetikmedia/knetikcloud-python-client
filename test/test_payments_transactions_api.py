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
from swagger_client.apis.payments_transactions_api import PaymentsTransactionsApi


class TestPaymentsTransactionsApi(unittest.TestCase):
    """ PaymentsTransactionsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.payments_transactions_api.PaymentsTransactionsApi()

    def tearDown(self):
        pass

    def test_get_transaction_using_get(self):
        """
        Test case for get_transaction_using_get

        Get the details for a single transaction
        """
        pass

    def test_get_transactions_using_get(self):
        """
        Test case for get_transactions_using_get

        List and search transactions
        """
        pass

    def test_refund_transaction_using_post(self):
        """
        Test case for refund_transaction_using_post

        Refund a payment transaction, in full or in part
        """
        pass


if __name__ == '__main__':
    unittest.main()
