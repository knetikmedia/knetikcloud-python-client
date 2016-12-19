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
from swagger_client.apis.payments_xsolla_api import PaymentsXsollaApi


class TestPaymentsXsollaApi(unittest.TestCase):
    """ PaymentsXsollaApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.payments_xsolla_api.PaymentsXsollaApi()

    def tearDown(self):
        pass

    def test_create_token_url_using_post(self):
        """
        Test case for create_token_url_using_post

        Create a payment token that should be used to forward the user to Xsolla so they can complete payment
        """
        pass

    def test_receive_notification_using_post(self):
        """
        Test case for receive_notification_using_post

        Receives payment response from Xsolla
        """
        pass


if __name__ == '__main__':
    unittest.main()
