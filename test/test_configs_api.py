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
from knetik_cloud.apis.configs_api import ConfigsApi


class TestConfigsApi(unittest.TestCase):
    """ ConfigsApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.configs_api.ConfigsApi()

    def tearDown(self):
        pass

    def test_create_config(self):
        """
        Test case for create_config

        Create a new config
        """
        pass

    def test_delete_config(self):
        """
        Test case for delete_config

        Delete an existing config
        """
        pass

    def test_get_config(self):
        """
        Test case for get_config

        Get a single config
        """
        pass

    def test_get_configs(self):
        """
        Test case for get_configs

        List and search configs
        """
        pass

    def test_update_config(self):
        """
        Test case for update_config

        Update an existing config
        """
        pass


if __name__ == '__main__':
    unittest.main()
