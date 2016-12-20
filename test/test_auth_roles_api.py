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
from swagger_client.apis.auth_roles_api import AuthRolesApi


class TestAuthRolesApi(unittest.TestCase):
    """ AuthRolesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.auth_roles_api.AuthRolesApi()

    def tearDown(self):
        pass

    def test_assign_client_roles_using_put(self):
        """
        Test case for assign_client_roles_using_put

        Set roles for a client
        """
        pass

    def test_assign_permissions_using_put(self):
        """
        Test case for assign_permissions_using_put

        Set permissions for a role
        """
        pass

    def test_assign_user_roles_external_using_put(self):
        """
        Test case for assign_user_roles_external_using_put

        Set roles for a user
        """
        pass

    def test_create_role_using_post(self):
        """
        Test case for create_role_using_post

        Create a new role
        """
        pass

    def test_delete_role_using_delete(self):
        """
        Test case for delete_role_using_delete

        Delete a role
        """
        pass

    def test_get_client_roles_using_get(self):
        """
        Test case for get_client_roles_using_get

        Get roles for a client
        """
        pass

    def test_get_role_using_get(self):
        """
        Test case for get_role_using_get

        Get a single role
        """
        pass

    def test_get_roles_using_get(self):
        """
        Test case for get_roles_using_get

        List and search roles
        """
        pass

    def test_get_user_roles_using_get(self):
        """
        Test case for get_user_roles_using_get

        Get roles for a user
        """
        pass

    def test_update_role_using_put(self):
        """
        Test case for update_role_using_put

        Update a role
        """
        pass


if __name__ == '__main__':
    unittest.main()