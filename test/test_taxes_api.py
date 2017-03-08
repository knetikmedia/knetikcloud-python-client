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

import knetik_cloud
from knetik_cloud.rest import ApiException
from knetik_cloud.apis.taxes_api import TaxesApi


class TestTaxesApi(unittest.TestCase):
    """ TaxesApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.taxes_api.TaxesApi()

    def tearDown(self):
        pass

    def test_create_country_tax(self):
        """
        Test case for create_country_tax

        Create a country tax
        """
        pass

    def test_create_state_tax(self):
        """
        Test case for create_state_tax

        Create a state tax
        """
        pass

    def test_delete_country_tax(self):
        """
        Test case for delete_country_tax

        Delete an existing tax
        """
        pass

    def test_delete_state_tax(self):
        """
        Test case for delete_state_tax

        Delete an existing state tax
        """
        pass

    def test_get_country_tax(self):
        """
        Test case for get_country_tax

        Get a single tax
        """
        pass

    def test_get_country_taxes(self):
        """
        Test case for get_country_taxes

        List and search taxes
        """
        pass

    def test_get_state_tax(self):
        """
        Test case for get_state_tax

        Get a single state tax
        """
        pass

    def test_get_state_taxes_for_countries(self):
        """
        Test case for get_state_taxes_for_countries

        List and search taxes across all countries
        """
        pass

    def test_get_state_taxes_for_country(self):
        """
        Test case for get_state_taxes_for_country

        List and search taxes within a country
        """
        pass

    def test_update_country_tax(self):
        """
        Test case for update_country_tax

        Create or update a tax
        """
        pass

    def test_update_state_tax(self):
        """
        Test case for update_state_tax

        Create or update a state tax
        """
        pass


if __name__ == '__main__':
    unittest.main()
