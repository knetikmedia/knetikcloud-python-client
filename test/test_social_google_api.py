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
from knetik_cloud.apis.social_google_api import SocialGoogleApi


class TestSocialGoogleApi(unittest.TestCase):
    """ SocialGoogleApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.social_google_api.SocialGoogleApi()

    def tearDown(self):
        pass

    def test_link_accounts1(self):
        """
        Test case for link_accounts1

        Link facebook account
        """
        pass


if __name__ == '__main__':
    unittest.main()
