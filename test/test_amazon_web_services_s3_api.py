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
from knetik_cloud.apis.amazon_web_services_s3_api import AmazonWebServicesS3Api


class TestAmazonWebServicesS3Api(unittest.TestCase):
    """ AmazonWebServicesS3Api unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.amazon_web_services_s3_api.AmazonWebServicesS3Api()

    def tearDown(self):
        pass

    def test_get_download_url(self):
        """
        Test case for get_download_url

        Get a temporary signed S3 URL for download
        """
        pass

    def test_get_signed_s3_url(self):
        """
        Test case for get_signed_s3_url

        Get a signed S3 URL for upload
        """
        pass


if __name__ == '__main__':
    unittest.main()
