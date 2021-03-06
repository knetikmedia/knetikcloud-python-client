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
from knetik_cloud.apis.store_api import StoreApi


class TestStoreApi(unittest.TestCase):
    """ StoreApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.store_api.StoreApi()

    def tearDown(self):
        pass

    def test_create_item_template(self):
        """
        Test case for create_item_template

        Create an item template
        """
        pass

    def test_create_store_item(self):
        """
        Test case for create_store_item

        Create a store item
        """
        pass

    def test_delete_item_template(self):
        """
        Test case for delete_item_template

        Delete an item template
        """
        pass

    def test_delete_store_item(self):
        """
        Test case for delete_store_item

        Delete a store item
        """
        pass

    def test_get_behaviors(self):
        """
        Test case for get_behaviors

        List available item behaviors
        """
        pass

    def test_get_item_template(self):
        """
        Test case for get_item_template

        Get a single item template
        """
        pass

    def test_get_item_templates(self):
        """
        Test case for get_item_templates

        List and search item templates
        """
        pass

    def test_get_store_item(self):
        """
        Test case for get_store_item

        Get a single store item
        """
        pass

    def test_get_store_items(self):
        """
        Test case for get_store_items

        List and search store items
        """
        pass

    def test_quick_buy(self):
        """
        Test case for quick_buy

        One-step purchase and pay for a single SKU item from a user's wallet
        """
        pass

    def test_update_item_template(self):
        """
        Test case for update_item_template

        Update an item template
        """
        pass

    def test_update_store_item(self):
        """
        Test case for update_store_item

        Update a store item
        """
        pass


if __name__ == '__main__':
    unittest.main()
