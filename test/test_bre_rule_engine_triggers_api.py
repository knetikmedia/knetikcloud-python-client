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
from swagger_client.apis.bre_rule_engine_triggers_api import BRERuleEngineTriggersApi


class TestBRERuleEngineTriggersApi(unittest.TestCase):
    """ BRERuleEngineTriggersApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.bre_rule_engine_triggers_api.BRERuleEngineTriggersApi()

    def tearDown(self):
        pass

    def test_create_bre_trigger(self):
        """
        Test case for create_bre_trigger

        Create a trigger
        """
        pass

    def test_delete_bre_trigger(self):
        """
        Test case for delete_bre_trigger

        Delete a trigger
        """
        pass

    def test_get_bre_trigger(self):
        """
        Test case for get_bre_trigger

        Get a single trigger
        """
        pass

    def test_get_bre_triggers(self):
        """
        Test case for get_bre_triggers

        List triggers
        """
        pass

    def test_update_bre_trigger(self):
        """
        Test case for update_bre_trigger

        Update a trigger
        """
        pass


if __name__ == '__main__':
    unittest.main()