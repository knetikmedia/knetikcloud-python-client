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
from swagger_client.models.invoice_create_request import InvoiceCreateRequest


class TestInvoiceCreateRequest(unittest.TestCase):
    """ InvoiceCreateRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInvoiceCreateRequest(self):
        """
        Test InvoiceCreateRequest
        """
        model = swagger_client.models.invoice_create_request.InvoiceCreateRequest()


if __name__ == '__main__':
    unittest.main()
