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
from knetik_cloud.models.location_log_resource import LocationLogResource


class TestLocationLogResource(unittest.TestCase):
    """ LocationLogResource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLocationLogResource(self):
        """
        Test LocationLogResource
        """
        model = knetik_cloud.models.location_log_resource.LocationLogResource()


if __name__ == '__main__':
    unittest.main()
