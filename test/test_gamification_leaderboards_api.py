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
from knetik_cloud.apis.gamification_leaderboards_api import GamificationLeaderboardsApi


class TestGamificationLeaderboardsApi(unittest.TestCase):
    """ GamificationLeaderboardsApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.gamification_leaderboards_api.GamificationLeaderboardsApi()

    def tearDown(self):
        pass

    def test_get_leaderboard(self):
        """
        Test case for get_leaderboard

        Retrieves leaderboard details and paginated entries
        """
        pass

    def test_get_leaderboard_rank(self):
        """
        Test case for get_leaderboard_rank

        Retrieves a specific user entry with rank
        """
        pass

    def test_get_leaderboard_strategies(self):
        """
        Test case for get_leaderboard_strategies

        Get a list of available leaderboard strategy names
        """
        pass


if __name__ == '__main__':
    unittest.main()
