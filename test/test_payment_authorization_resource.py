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

import knetik_cloud
from knetik_cloud.rest import ApiException
from knetik_cloud.models.payment_authorization_resource import PaymentAuthorizationResource


class TestPaymentAuthorizationResource(unittest.TestCase):
    """ PaymentAuthorizationResource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentAuthorizationResource(self):
        """
        Test PaymentAuthorizationResource
        """
        model = knetik_cloud.models.payment_authorization_resource.PaymentAuthorizationResource()


if __name__ == '__main__':
    unittest.main()
