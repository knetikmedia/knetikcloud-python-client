# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

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
from swagger_client.apis.store_sales_api import StoreSalesApi


class TestStoreSalesApi(unittest.TestCase):
    """ StoreSalesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.store_sales_api.StoreSalesApi()

    def tearDown(self):
        pass

    def test_create_catalog_sale_using_post(self):
        """
        Test case for create_catalog_sale_using_post

        Create a sale
        """
        pass

    def test_delete_catalog_sale_using_delete(self):
        """
        Test case for delete_catalog_sale_using_delete

        Delete a sale
        """
        pass

    def test_get_catalog_sale_using_get(self):
        """
        Test case for get_catalog_sale_using_get

        Get a single sale
        """
        pass

    def test_get_catalog_sales_using_get(self):
        """
        Test case for get_catalog_sales_using_get

        List and search sales
        """
        pass

    def test_update_catalog_sale_using_put(self):
        """
        Test case for update_catalog_sale_using_put

        Update a sale
        """
        pass


if __name__ == '__main__':
    unittest.main()
