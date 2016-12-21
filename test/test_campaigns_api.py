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
from swagger_client.apis.campaigns_api import CampaignsApi


class TestCampaignsApi(unittest.TestCase):
    """ CampaignsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.campaigns_api.CampaignsApi()

    def tearDown(self):
        pass

    def test_add_challenges_using_post(self):
        """
        Test case for add_challenges_using_post

        Add a challenge to a campaign
        """
        pass

    def test_create_campaign_template_using_post(self):
        """
        Test case for create_campaign_template_using_post

        Create a campaign template
        """
        pass

    def test_create_campaign_using_post(self):
        """
        Test case for create_campaign_using_post

        Create a campaign
        """
        pass

    def test_delete_campaign_template_using_delete(self):
        """
        Test case for delete_campaign_template_using_delete

        Delete a campaign template
        """
        pass

    def test_delete_campaign_using_delete(self):
        """
        Test case for delete_campaign_using_delete

        Delete a campaign
        """
        pass

    def test_get_campaign_template_using_get(self):
        """
        Test case for get_campaign_template_using_get

        Get a single campaign template
        """
        pass

    def test_get_campaign_templates_using_get(self):
        """
        Test case for get_campaign_templates_using_get

        List and search campaign templates
        """
        pass

    def test_get_campaign_using_get(self):
        """
        Test case for get_campaign_using_get

        Returns a single campaign
        """
        pass

    def test_get_campaigns_using_get(self):
        """
        Test case for get_campaigns_using_get

        List and search campaigns
        """
        pass

    def test_get_challenges_using_get(self):
        """
        Test case for get_challenges_using_get

        List the challenges associated with a campaign
        """
        pass

    def test_remove_challenge_using_delete(self):
        """
        Test case for remove_challenge_using_delete

        Remove a challenge from a campaign
        """
        pass

    def test_update_campaign_template_using_put(self):
        """
        Test case for update_campaign_template_using_put

        Update an campaign template
        """
        pass

    def test_update_campaign_using_put(self):
        """
        Test case for update_campaign_using_put

        Update a campaign
        """
        pass


if __name__ == '__main__':
    unittest.main()
