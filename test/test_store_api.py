# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

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
from swagger_client.apis.store_api import StoreApi


class TestStoreApi(unittest.TestCase):
    """ StoreApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.store_api.StoreApi()

    def tearDown(self):
        pass

    def test_create_item_template_using_post(self):
        """
        Test case for create_item_template_using_post

        Create an item template
        """
        pass

    def test_create_store_item_external_using_post(self):
        """
        Test case for create_store_item_external_using_post

        Create a store item
        """
        pass

    def test_delete_item_template_using_delete(self):
        """
        Test case for delete_item_template_using_delete

        Delete an item template
        """
        pass

    def test_delete_store_item_using_delete1(self):
        """
        Test case for delete_store_item_using_delete1

        Delete a store item
        """
        pass

    def test_get_item_template_using_get(self):
        """
        Test case for get_item_template_using_get

        Get a single item template
        """
        pass

    def test_get_item_templates_using_get(self):
        """
        Test case for get_item_templates_using_get

        List and search item templates
        """
        pass

    def test_get_store_item_using_get1(self):
        """
        Test case for get_store_item_using_get1

        Get a single store item
        """
        pass

    def test_get_store_items_using_get(self):
        """
        Test case for get_store_items_using_get

        List and search store items
        """
        pass

    def test_get_using_get2(self):
        """
        Test case for get_using_get2

        Get a listing of store items
        """
        pass

    def test_update_item_template_using_put(self):
        """
        Test case for update_item_template_using_put

        Update an item template
        """
        pass

    def test_update_store_item_external_using_put(self):
        """
        Test case for update_store_item_external_using_put

        Update a store item
        """
        pass


if __name__ == '__main__':
    unittest.main()
