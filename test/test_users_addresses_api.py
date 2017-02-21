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

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.users_addresses_api import UsersAddressesApi


class TestUsersAddressesApi(unittest.TestCase):
    """ UsersAddressesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.users_addresses_api.UsersAddressesApi()

    def tearDown(self):
        pass

    def test_create_address(self):
        """
        Test case for create_address

        Create a new address
        """
        pass

    def test_delete_address(self):
        """
        Test case for delete_address

        Delete an address
        """
        pass

    def test_get_address(self):
        """
        Test case for get_address

        Get a single address
        """
        pass

    def test_get_addresses(self):
        """
        Test case for get_addresses

        List and search addresses
        """
        pass

    def test_update_address(self):
        """
        Test case for update_address

        Update an address
        """
        pass


if __name__ == '__main__':
    unittest.main()
