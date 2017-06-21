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
from knetik_cloud.apis.bre_rule_engine_variables_api import BRERuleEngineVariablesApi


class TestBRERuleEngineVariablesApi(unittest.TestCase):
    """ BRERuleEngineVariablesApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.bre_rule_engine_variables_api.BRERuleEngineVariablesApi()

    def tearDown(self):
        pass

    def test_get_bre_variable_types(self):
        """
        Test case for get_bre_variable_types

        Get a list of variable types available
        """
        pass

    def test_get_bre_variable_values(self):
        """
        Test case for get_bre_variable_values

        List valid values for a type
        """
        pass


if __name__ == '__main__':
    unittest.main()
