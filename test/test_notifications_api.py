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
from knetik_cloud.apis.notifications_api import NotificationsApi


class TestNotificationsApi(unittest.TestCase):
    """ NotificationsApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.notifications_api.NotificationsApi()

    def tearDown(self):
        pass

    def test_create_notification_type(self):
        """
        Test case for create_notification_type

        Create a notification type
        """
        pass

    def test_delete_notification_type(self):
        """
        Test case for delete_notification_type

        Delete a notification type
        """
        pass

    def test_get_notification_type(self):
        """
        Test case for get_notification_type

        Get a single notification type
        """
        pass

    def test_get_notification_types(self):
        """
        Test case for get_notification_types

        List and search notification types
        """
        pass

    def test_get_user_notification_info(self):
        """
        Test case for get_user_notification_info

        View a user's notification settings for a type
        """
        pass

    def test_get_user_notification_info_list(self):
        """
        Test case for get_user_notification_info_list

        View a user's notification settings
        """
        pass

    def test_get_user_notifications(self):
        """
        Test case for get_user_notifications

        Get notifications
        """
        pass

    def test_send_notification(self):
        """
        Test case for send_notification

        Send a notification
        """
        pass

    def test_set_user_notification_status(self):
        """
        Test case for set_user_notification_status

        Set notification status
        """
        pass

    def test_silence_direct_notifications(self):
        """
        Test case for silence_direct_notifications

        Enable or disable direct notifications for a user
        """
        pass

    def test_update_notification_type(self):
        """
        Test case for update_notification_type

        Update a notificationType
        """
        pass


if __name__ == '__main__':
    unittest.main()
