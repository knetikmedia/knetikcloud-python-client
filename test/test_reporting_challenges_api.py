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
from swagger_client.apis.reporting_challenges_api import ReportingChallengesApi


class TestReportingChallengesApi(unittest.TestCase):
    """ ReportingChallengesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.reporting_challenges_api.ReportingChallengesApi()

    def tearDown(self):
        pass

    def test_get_challenge_event_leaderboard_using_get(self):
        """
        Test case for get_challenge_event_leaderboard_using_get

        Retrieve a challenge event leaderboard details
        """
        pass

    def test_get_challenge_event_participants_using_get(self):
        """
        Test case for get_challenge_event_participants_using_get

        Retrieve a challenge event participant details
        """
        pass


if __name__ == '__main__':
    unittest.main()