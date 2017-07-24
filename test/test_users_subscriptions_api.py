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
from knetik_cloud.apis.users_subscriptions_api import UsersSubscriptionsApi


class TestUsersSubscriptionsApi(unittest.TestCase):
    """ UsersSubscriptionsApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.users_subscriptions_api.UsersSubscriptionsApi()

    def tearDown(self):
        pass

    def test_get_user_subscription_details(self):
        """
        Test case for get_user_subscription_details

        Get details about a user's subscription
        """
        pass

    def test_get_users_subscription_details(self):
        """
        Test case for get_users_subscription_details

        Get details about a user's subscriptions
        """
        pass

    def test_reactivate_user_subscription(self):
        """
        Test case for reactivate_user_subscription

        Reactivate a subscription and charge fee
        """
        pass

    def test_set_subscription_bill_date(self):
        """
        Test case for set_subscription_bill_date

        Set a new date to bill a subscription on
        """
        pass

    def test_set_subscription_payment_method(self):
        """
        Test case for set_subscription_payment_method

        Set the payment method to use for a subscription
        """
        pass

    def test_set_subscription_status(self):
        """
        Test case for set_subscription_status

        Set the status of a subscription
        """
        pass

    def test_set_user_subscription_plan(self):
        """
        Test case for set_user_subscription_plan

        Set a new subscription plan for a user
        """
        pass

    def test_set_user_subscription_price(self):
        """
        Test case for set_user_subscription_price

        Set a new subscription price for a user
        """
        pass


if __name__ == '__main__':
    unittest.main()
