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
from knetik_cloud.apis.util_maintenance_api import UtilMaintenanceApi


class TestUtilMaintenanceApi(unittest.TestCase):
    """ UtilMaintenanceApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.util_maintenance_api.UtilMaintenanceApi()

    def tearDown(self):
        pass

    def test_delete_maintenance(self):
        """
        Test case for delete_maintenance

        Delete maintenance info
        """
        pass

    def test_get_maintenance(self):
        """
        Test case for get_maintenance

        Get current maintenance info
        """
        pass

    def test_set_maintenance(self):
        """
        Test case for set_maintenance

        Set current maintenance info
        """
        pass

    def test_update_maintenance(self):
        """
        Test case for update_maintenance

        Update current maintenance info
        """
        pass


if __name__ == '__main__':
    unittest.main()
