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
from knetik_cloud.apis.rule_engine_events_api import RuleEngineEventsApi


class TestRuleEngineEventsApi(unittest.TestCase):
    """ RuleEngineEventsApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.rule_engine_events_api.RuleEngineEventsApi()

    def tearDown(self):
        pass

    def test_send_bre_event(self):
        """
        Test case for send_bre_event

        Fire a new event, based on an existing trigger
        """
        pass


if __name__ == '__main__':
    unittest.main()
