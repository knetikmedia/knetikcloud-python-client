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
from swagger_client.apis.bre_rule_engine_actions_api import BRERuleEngineActionsApi


class TestBRERuleEngineActionsApi(unittest.TestCase):
    """ BRERuleEngineActionsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.bre_rule_engine_actions_api.BRERuleEngineActionsApi()

    def tearDown(self):
        pass

    def test_get_actions_using_get(self):
        """
        Test case for get_actions_using_get

        Get a list of available actions
        """
        pass


if __name__ == '__main__':
    unittest.main()