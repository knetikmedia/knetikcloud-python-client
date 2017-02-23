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

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.content_comments_api import ContentCommentsApi


class TestContentCommentsApi(unittest.TestCase):
    """ ContentCommentsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.content_comments_api.ContentCommentsApi()

    def tearDown(self):
        pass

    def test_add_comment(self):
        """
        Test case for add_comment

        Add a new comment
        """
        pass

    def test_delete_comment(self):
        """
        Test case for delete_comment

        Delete a comment
        """
        pass

    def test_get_comment(self):
        """
        Test case for get_comment

        Return a comment
        """
        pass

    def test_get_comments(self):
        """
        Test case for get_comments

        Returns a page of comments
        """
        pass

    def test_search_comments(self):
        """
        Test case for search_comments

        Search the comment index
        """
        pass

    def test_update_comment(self):
        """
        Test case for update_comment

        Update a comment
        """
        pass


if __name__ == '__main__':
    unittest.main()