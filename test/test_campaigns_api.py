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
from knetik_cloud.apis.campaigns_api import CampaignsApi


class TestCampaignsApi(unittest.TestCase):
    """ CampaignsApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.campaigns_api.CampaignsApi()

    def tearDown(self):
        pass

    def test_add_challenge_to_campaign(self):
        """
        Test case for add_challenge_to_campaign

        Add a challenge to a campaign
        """
        pass

    def test_create_campaign(self):
        """
        Test case for create_campaign

        Create a campaign
        """
        pass

    def test_create_campaign_template(self):
        """
        Test case for create_campaign_template

        Create a campaign template
        """
        pass

    def test_delete_campaign(self):
        """
        Test case for delete_campaign

        Delete a campaign
        """
        pass

    def test_delete_campaign_template(self):
        """
        Test case for delete_campaign_template

        Delete a campaign template
        """
        pass

    def test_get_campaign(self):
        """
        Test case for get_campaign

        Returns a single campaign
        """
        pass

    def test_get_campaign_challenges(self):
        """
        Test case for get_campaign_challenges

        List the challenges associated with a campaign
        """
        pass

    def test_get_campaign_template(self):
        """
        Test case for get_campaign_template

        Get a single campaign template
        """
        pass

    def test_get_campaign_templates(self):
        """
        Test case for get_campaign_templates

        List and search campaign templates
        """
        pass

    def test_get_campaigns(self):
        """
        Test case for get_campaigns

        List and search campaigns
        """
        pass

    def test_remove_challenge_from_campaign(self):
        """
        Test case for remove_challenge_from_campaign

        Remove a challenge from a campaign
        """
        pass

    def test_update_campaign(self):
        """
        Test case for update_campaign

        Update a campaign
        """
        pass

    def test_update_campaign_template(self):
        """
        Test case for update_campaign_template

        Update an campaign template
        """
        pass


if __name__ == '__main__':
    unittest.main()
