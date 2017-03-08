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
from knetik_cloud.apis.logs_api import LogsApi


class TestLogsApi(unittest.TestCase):
    """ LogsApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.logs_api.LogsApi()

    def tearDown(self):
        pass

    def test_add_user_log(self):
        """
        Test case for add_user_log

        Add a user log entry
        """
        pass

    def test_get_bre_event_log(self):
        """
        Test case for get_bre_event_log

        Get an existing BRE event log entry by id
        """
        pass

    def test_get_bre_event_logs(self):
        """
        Test case for get_bre_event_logs

        Returns a list of BRE event log entries
        """
        pass

    def test_get_bre_forward_log(self):
        """
        Test case for get_bre_forward_log

        Get an existing forward log entry by id
        """
        pass

    def test_get_bre_forward_logs(self):
        """
        Test case for get_bre_forward_logs

        Returns a list of forward log entries
        """
        pass

    def test_get_user_log(self):
        """
        Test case for get_user_log

        Returns a user log entry by id
        """
        pass

    def test_get_user_logs(self):
        """
        Test case for get_user_logs

        Returns a page of user logs entries
        """
        pass


if __name__ == '__main__':
    unittest.main()
