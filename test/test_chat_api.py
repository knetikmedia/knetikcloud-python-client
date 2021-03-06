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
from knetik_cloud.apis.chat_api import ChatApi


class TestChatApi(unittest.TestCase):
    """ ChatApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.chat_api.ChatApi()

    def tearDown(self):
        pass

    def test_acknowledge_chat_message(self):
        """
        Test case for acknowledge_chat_message

        Acknowledge number of messages in a thread
        """
        pass

    def test_add_chat_message_blacklist(self):
        """
        Test case for add_chat_message_blacklist

        Add a user to a chat message blacklist
        """
        pass

    def test_delete_chat_message(self):
        """
        Test case for delete_chat_message

        Delete a message
        """
        pass

    def test_edit_chat_message(self):
        """
        Test case for edit_chat_message

        Edit your message
        """
        pass

    def test_get_chat_message(self):
        """
        Test case for get_chat_message

        Get a message
        """
        pass

    def test_get_chat_message_blacklist(self):
        """
        Test case for get_chat_message_blacklist

        Get a list of blocked users for chat messaging
        """
        pass

    def test_get_chat_threads(self):
        """
        Test case for get_chat_threads

        List your threads
        """
        pass

    def test_get_direct_messages(self):
        """
        Test case for get_direct_messages

        List messages with a user
        """
        pass

    def test_get_thread_messages(self):
        """
        Test case for get_thread_messages

        List messages in a thread
        """
        pass

    def test_get_topic_messages(self):
        """
        Test case for get_topic_messages

        List messages in a topic
        """
        pass

    def test_remove_chat_blacklist(self):
        """
        Test case for remove_chat_blacklist

        Remove a user from a blacklist
        """
        pass

    def test_send_chat_message(self):
        """
        Test case for send_chat_message

        Send a message
        """
        pass


if __name__ == '__main__':
    unittest.main()
