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
from swagger_client.models.version import Version


class TestVersion(unittest.TestCase):
    """ Version unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVersion(self):
        """
        Test Version
        """
        model = swagger_client.models.version.Version()


if __name__ == '__main__':
    unittest.main()