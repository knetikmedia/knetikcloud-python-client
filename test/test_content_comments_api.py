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
from swagger_client.apis.content_comments_api import ContentCommentsApi


class TestContentCommentsApi(unittest.TestCase):
    """ ContentCommentsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.content_comments_api.ContentCommentsApi()

    def tearDown(self):
        pass

    def test_add_comment_using_post(self):
        """
        Test case for add_comment_using_post

        Add a new comment
        """
        pass

    def test_delete_comment_using_delete(self):
        """
        Test case for delete_comment_using_delete

        Delete a comment
        """
        pass

    def test_get_comment_using_get(self):
        """
        Test case for get_comment_using_get

        Returns a comment by comment id
        """
        pass

    def test_get_comments_using_get(self):
        """
        Test case for get_comments_using_get

        Returns a page of comments
        """
        pass

    def test_search_comments_using_post(self):
        """
        Test case for search_comments_using_post

        Search the comment index
        """
        pass

    def test_update_comment_using_put(self):
        """
        Test case for update_comment_using_put

        Update comment content
        """
        pass


if __name__ == '__main__':
    unittest.main()
