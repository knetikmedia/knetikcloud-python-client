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
from swagger_client.apis.store_bundles_api import StoreBundlesApi


class TestStoreBundlesApi(unittest.TestCase):
    """ StoreBundlesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.store_bundles_api.StoreBundlesApi()

    def tearDown(self):
        pass

    def test_create_bundle_item_using_post(self):
        """
        Test case for create_bundle_item_using_post

        Create a bundle item
        """
        pass

    def test_create_bundle_template_using_post(self):
        """
        Test case for create_bundle_template_using_post

        Create a bundle template
        """
        pass

    def test_delete_bundle_template_using_delete(self):
        """
        Test case for delete_bundle_template_using_delete

        Delete a bundle template
        """
        pass

    def test_delete_store_item_using_delete(self):
        """
        Test case for delete_store_item_using_delete

        Delete a bundle item
        """
        pass

    def test_get_bundle_template_using_get(self):
        """
        Test case for get_bundle_template_using_get

        Get a single bundle template
        """
        pass

    def test_get_bundle_templates_using_get(self):
        """
        Test case for get_bundle_templates_using_get

        List and search bundle templates
        """
        pass

    def test_get_store_item_using_get(self):
        """
        Test case for get_store_item_using_get

        Get a single bundle item
        """
        pass

    def test_update_bundle_item_using_put(self):
        """
        Test case for update_bundle_item_using_put

        Update a bundle item
        """
        pass

    def test_update_bundle_template_using_put(self):
        """
        Test case for update_bundle_template_using_put

        Update a bundle template
        """
        pass


if __name__ == '__main__':
    unittest.main()
