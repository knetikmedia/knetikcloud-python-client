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
from swagger_client.apis.logs_api import LogsApi


class TestLogsApi(unittest.TestCase):
    """ LogsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.logs_api.LogsApi()

    def tearDown(self):
        pass

    def test_add_user_log_using_post(self):
        """
        Test case for add_user_log_using_post

        Add a new user log entry
        """
        pass

    def test_get_event_log_using_get(self):
        """
        Test case for get_event_log_using_get

        Get an existing BRE event log entry by id
        """
        pass

    def test_get_events_logs_using_get(self):
        """
        Test case for get_events_logs_using_get

        Returns a list of BRE event log entries
        """
        pass

    def test_get_forward_log_using_get(self):
        """
        Test case for get_forward_log_using_get

        Get an existing forward log entry by id
        """
        pass

    def test_get_forward_logs_using_get(self):
        """
        Test case for get_forward_logs_using_get

        Returns a list of forward log entries
        """
        pass

    def test_get_user_logs_using_get(self):
        """
        Test case for get_user_logs_using_get

        Returns a user log entry by id
        """
        pass

    def test_get_user_logs_using_get1(self):
        """
        Test case for get_user_logs_using_get1

        Returns a page of user logs entries
        """
        pass


if __name__ == '__main__':
    unittest.main()
