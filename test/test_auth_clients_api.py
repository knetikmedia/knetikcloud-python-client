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
from knetik_cloud.apis.auth_clients_api import AuthClientsApi


class TestAuthClientsApi(unittest.TestCase):
    """ AuthClientsApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.auth_clients_api.AuthClientsApi()

    def tearDown(self):
        pass

    def test_create_client(self):
        """
        Test case for create_client

        Create a new client
        """
        pass

    def test_delete_client(self):
        """
        Test case for delete_client

        Delete a client
        """
        pass

    def test_get_client(self):
        """
        Test case for get_client

        Get a single client
        """
        pass

    def test_get_client_grant_types(self):
        """
        Test case for get_client_grant_types

        List available client grant types
        """
        pass

    def test_get_clients(self):
        """
        Test case for get_clients

        List and search clients
        """
        pass

    def test_set_client_grant_types(self):
        """
        Test case for set_client_grant_types

        Set grant types for a client
        """
        pass

    def test_set_client_redirect_uris(self):
        """
        Test case for set_client_redirect_uris

        Set redirect uris for a client
        """
        pass

    def test_update_client(self):
        """
        Test case for update_client

        Update a client
        """
        pass


if __name__ == '__main__':
    unittest.main()
