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
from knetik_cloud.apis.content_polls_api import ContentPollsApi


class TestContentPollsApi(unittest.TestCase):
    """ ContentPollsApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.content_polls_api.ContentPollsApi()

    def tearDown(self):
        pass

    def test_answer_poll(self):
        """
        Test case for answer_poll

        Add your vote to a poll
        """
        pass

    def test_create_poll(self):
        """
        Test case for create_poll

        Create a new poll
        """
        pass

    def test_create_poll_template(self):
        """
        Test case for create_poll_template

        Create a poll template
        """
        pass

    def test_delete_poll(self):
        """
        Test case for delete_poll

        Delete an existing poll
        """
        pass

    def test_delete_poll_template(self):
        """
        Test case for delete_poll_template

        Delete a poll template
        """
        pass

    def test_get_poll(self):
        """
        Test case for get_poll

        Get a single poll
        """
        pass

    def test_get_poll_answer(self):
        """
        Test case for get_poll_answer

        Get poll answer
        """
        pass

    def test_get_poll_template(self):
        """
        Test case for get_poll_template

        Get a single poll template
        """
        pass

    def test_get_poll_templates(self):
        """
        Test case for get_poll_templates

        List and search poll templates
        """
        pass

    def test_get_polls(self):
        """
        Test case for get_polls

        List and search polls
        """
        pass

    def test_update_poll(self):
        """
        Test case for update_poll

        Update an existing poll
        """
        pass

    def test_update_poll_template(self):
        """
        Test case for update_poll_template

        Update a poll template
        """
        pass


if __name__ == '__main__':
    unittest.main()
