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
from knetik_cloud.models.flag_resource import FlagResource


class TestFlagResource(unittest.TestCase):
    """ FlagResource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFlagResource(self):
        """
        Test FlagResource
        """
        model = knetik_cloud.models.flag_resource.FlagResource()


if __name__ == '__main__':
    unittest.main()
