# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

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
from swagger_client.models.payment_method_resource import PaymentMethodResource


class TestPaymentMethodResource(unittest.TestCase):
    """ PaymentMethodResource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentMethodResource(self):
        """
        Test PaymentMethodResource
        """
        model = swagger_client.models.payment_method_resource.PaymentMethodResource()


if __name__ == '__main__':
    unittest.main()
