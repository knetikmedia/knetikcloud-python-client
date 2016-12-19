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
from swagger_client.apis.gamification_achievements_api import GamificationAchievementsApi


class TestGamificationAchievementsApi(unittest.TestCase):
    """ GamificationAchievementsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.gamification_achievements_api.GamificationAchievementsApi()

    def tearDown(self):
        pass

    def test_create_achievement_using_post(self):
        """
        Test case for create_achievement_using_post

        Create a new achievement definition
        """
        pass

    def test_create_template_using_post(self):
        """
        Test case for create_template_using_post

        Create an achievement template
        """
        pass

    def test_delete_achievement_template_using_delete(self):
        """
        Test case for delete_achievement_template_using_delete

        Delete an achievement template
        """
        pass

    def test_delete_achievement_using_delete(self):
        """
        Test case for delete_achievement_using_delete

        Delete an achievement definition
        """
        pass

    def test_find_all_by_group_name_using_get(self):
        """
        Test case for find_all_by_group_name_using_get

        Get a list of derived achievements
        """
        pass

    def test_get_achievement_template_using_get(self):
        """
        Test case for get_achievement_template_using_get

        Get a single achievement template
        """
        pass

    def test_get_achievement_templates_using_get(self):
        """
        Test case for get_achievement_templates_using_get

        List and search achievement templates
        """
        pass

    def test_get_achievement_using_get(self):
        """
        Test case for get_achievement_using_get

        Get a single achievement definition
        """
        pass

    def test_get_achievements_using_get(self):
        """
        Test case for get_achievements_using_get

        Get all achievement definitions in the system
        """
        pass

    def test_get_all_user_progress_for_achievement_using_get(self):
        """
        Test case for get_all_user_progress_for_achievement_using_get

        Retrieve progress on a given achievement for all users
        """
        pass

    def test_get_all_user_progress_using_get(self):
        """
        Test case for get_all_user_progress_using_get

        Retrieve progress on achievements for all users
        """
        pass

    def test_get_available_triggers_using_get(self):
        """
        Test case for get_available_triggers_using_get

        Get the list of triggers that can be used to trigger an achievement progress update
        """
        pass

    def test_get_user_progress_for_achievement_using_get(self):
        """
        Test case for get_user_progress_for_achievement_using_get

        Retrieve progress on a given achievement for a given user
        """
        pass

    def test_get_user_progress_using_get(self):
        """
        Test case for get_user_progress_using_get

        Retrieve progress on achievements for a given user
        """
        pass

    def test_update_achievement_using_put(self):
        """
        Test case for update_achievement_using_put

        Update an achievement definition
        """
        pass

    def test_update_progress_using_put(self):
        """
        Test case for update_progress_using_put

        Update or create an achievement progress record for a user
        """
        pass

    def test_update_template_using_put(self):
        """
        Test case for update_template_using_put

        Update an achievement template
        """
        pass


if __name__ == '__main__':
    unittest.main()
