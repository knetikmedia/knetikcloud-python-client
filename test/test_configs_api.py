# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.configs_api import ConfigsApi


class TestConfigsApi(unittest.TestCase):
    """ ConfigsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.configs_api.ConfigsApi()

    def tearDown(self):
        pass

    def test_create_config_using_post(self):
        """
        Test case for create_config_using_post

        Create a new config
        """
        pass

    def test_delete_config_using_delete(self):
        """
        Test case for delete_config_using_delete

        Delete an existing config.
        """
        pass

    def test_get_config_using_get(self):
        """
        Test case for get_config_using_get

        Get a single config
        """
        pass

    def test_get_configs_using_get(self):
        """
        Test case for get_configs_using_get

        List and search configs
        """
        pass

    def test_update_config_using_put(self):
        """
        Test case for update_config_using_put

        Update an existing config.
        """
        pass


if __name__ == '__main__':
    unittest.main()
