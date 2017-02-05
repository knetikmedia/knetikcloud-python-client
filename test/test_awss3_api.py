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
from swagger_client.apis.awss3_api import AWSS3Api


class TestAWSS3Api(unittest.TestCase):
    """ AWSS3Api unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.awss3_api.AWSS3Api()

    def tearDown(self):
        pass

    def test_pre_sign_url_using_get(self):
        """
        Test case for pre_sign_url_using_get

        Get a signed S3 URL
        """
        pass


if __name__ == '__main__':
    unittest.main()
