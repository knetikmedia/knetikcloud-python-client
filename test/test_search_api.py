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
from swagger_client.apis.search_api import SearchApi


class TestSearchApi(unittest.TestCase):
    """ SearchApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.search_api.SearchApi()

    def tearDown(self):
        pass

    def test_external_add_using_post(self):
        """
        Test case for external_add_using_post

        Add a new object to an index
        """
        pass

    def test_external_delete_all_using_delete(self):
        """
        Test case for external_delete_all_using_delete

        Delete all objects in an index
        """
        pass

    def test_external_delete_using_delete(self):
        """
        Test case for external_delete_using_delete

        Delete an object
        """
        pass

    def test_external_register_using_post(self):
        """
        Test case for external_register_using_post

        Register reference mappings
        """
        pass

    def test_search_using_post(self):
        """
        Test case for search_using_post

        Search an index
        """
        pass


if __name__ == '__main__':
    unittest.main()
