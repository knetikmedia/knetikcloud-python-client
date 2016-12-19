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
from swagger_client.apis.store_subscriptions_api import StoreSubscriptionsApi


class TestStoreSubscriptionsApi(unittest.TestCase):
    """ StoreSubscriptionsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.store_subscriptions_api.StoreSubscriptionsApi()

    def tearDown(self):
        pass

    def test_create_subscription_template_using_post(self):
        """
        Test case for create_subscription_template_using_post

        Create a subscription template
        """
        pass

    def test_create_subscription_using_post(self):
        """
        Test case for create_subscription_using_post

        Creates a subscription item and associated plans
        """
        pass

    def test_delete_plan_using_delete(self):
        """
        Test case for delete_plan_using_delete

        Delete a subscription plan
        """
        pass

    def test_delete_subscription_template_using_delete(self):
        """
        Test case for delete_subscription_template_using_delete

        Delete a subscription template
        """
        pass

    def test_get_subscription_template_using_get(self):
        """
        Test case for get_subscription_template_using_get

        Get a single subscription template
        """
        pass

    def test_get_subscription_templates_using_get(self):
        """
        Test case for get_subscription_templates_using_get

        List and search subscription templates
        """
        pass

    def test_get_subscription_using_get(self):
        """
        Test case for get_subscription_using_get

        Retrieve a single subscription item and associated plans
        """
        pass

    def test_list_subscriptions_using_get(self):
        """
        Test case for list_subscriptions_using_get

        List available subscription items and associated plans
        """
        pass

    def test_process_using_post(self):
        """
        Test case for process_using_post

        Processes subscriptions and charge dues
        """
        pass

    def test_update_subscription_template_using_put(self):
        """
        Test case for update_subscription_template_using_put

        Update a subscription template
        """
        pass

    def test_update_subscription_using_put(self):
        """
        Test case for update_subscription_using_put

        Updates a subscription item and associated plans
        """
        pass


if __name__ == '__main__':
    unittest.main()
