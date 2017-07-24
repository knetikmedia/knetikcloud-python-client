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
from knetik_cloud.apis.templates_properties_api import TemplatesPropertiesApi


class TestTemplatesPropertiesApi(unittest.TestCase):
    """ TemplatesPropertiesApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.templates_properties_api.TemplatesPropertiesApi()

    def tearDown(self):
        pass

    def test_get_template_property_type(self):
        """
        Test case for get_template_property_type

        Get details for a template property type
        """
        pass

    def test_get_template_property_types(self):
        """
        Test case for get_template_property_types

        List template property types
        """
        pass


if __name__ == '__main__':
    unittest.main()