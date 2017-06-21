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
from knetik_cloud.apis.campaigns_challenges_api import CampaignsChallengesApi


class TestCampaignsChallengesApi(unittest.TestCase):
    """ CampaignsChallengesApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.campaigns_challenges_api.CampaignsChallengesApi()

    def tearDown(self):
        pass

    def test_create_challenge(self):
        """
        Test case for create_challenge

        Create a challenge
        """
        pass

    def test_create_challenge_activity(self):
        """
        Test case for create_challenge_activity

        Create a challenge activity
        """
        pass

    def test_create_challenge_activity_template(self):
        """
        Test case for create_challenge_activity_template

        Create a challenge activity template
        """
        pass

    def test_create_challenge_template(self):
        """
        Test case for create_challenge_template

        Create a challenge template
        """
        pass

    def test_delete_challenge(self):
        """
        Test case for delete_challenge

        Delete a challenge
        """
        pass

    def test_delete_challenge_activity(self):
        """
        Test case for delete_challenge_activity

        Delete a challenge activity
        """
        pass

    def test_delete_challenge_activity_template(self):
        """
        Test case for delete_challenge_activity_template

        Delete a challenge activity template
        """
        pass

    def test_delete_challenge_event(self):
        """
        Test case for delete_challenge_event

        Delete a challenge event
        """
        pass

    def test_delete_challenge_template(self):
        """
        Test case for delete_challenge_template

        Delete a challenge template
        """
        pass

    def test_get_challenge(self):
        """
        Test case for get_challenge

        Retrieve a challenge
        """
        pass

    def test_get_challenge_activities(self):
        """
        Test case for get_challenge_activities

        List and search challenge activities
        """
        pass

    def test_get_challenge_activity(self):
        """
        Test case for get_challenge_activity

        Get a single challenge activity
        """
        pass

    def test_get_challenge_activity_template(self):
        """
        Test case for get_challenge_activity_template

        Get a single challenge activity template
        """
        pass

    def test_get_challenge_activity_templates(self):
        """
        Test case for get_challenge_activity_templates

        List and search challenge activity templates
        """
        pass

    def test_get_challenge_event(self):
        """
        Test case for get_challenge_event

        Retrieve a single challenge event details
        """
        pass

    def test_get_challenge_events(self):
        """
        Test case for get_challenge_events

        Retrieve a list of challenge events
        """
        pass

    def test_get_challenge_template(self):
        """
        Test case for get_challenge_template

        Get a single challenge template
        """
        pass

    def test_get_challenge_templates(self):
        """
        Test case for get_challenge_templates

        List and search challenge templates
        """
        pass

    def test_get_challenges(self):
        """
        Test case for get_challenges

        Retrieve a list of challenges
        """
        pass

    def test_update_challenge(self):
        """
        Test case for update_challenge

        Update a challenge
        """
        pass

    def test_update_challenge_activity(self):
        """
        Test case for update_challenge_activity

        Update a challenge activity
        """
        pass

    def test_update_challenge_activity_template(self):
        """
        Test case for update_challenge_activity_template

        Update an challenge activity template
        """
        pass

    def test_update_challenge_template(self):
        """
        Test case for update_challenge_template

        Update a challenge template
        """
        pass


if __name__ == '__main__':
    unittest.main()
