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
from knetik_cloud.apis.content_articles_api import ContentArticlesApi


class TestContentArticlesApi(unittest.TestCase):
    """ ContentArticlesApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.content_articles_api.ContentArticlesApi()

    def tearDown(self):
        pass

    def test_create_article(self):
        """
        Test case for create_article

        Create a new article
        """
        pass

    def test_create_article_template(self):
        """
        Test case for create_article_template

        Create an article template
        """
        pass

    def test_delete_article(self):
        """
        Test case for delete_article

        Delete an existing article
        """
        pass

    def test_delete_article_template(self):
        """
        Test case for delete_article_template

        Delete an article template
        """
        pass

    def test_get_article(self):
        """
        Test case for get_article

        Get a single article
        """
        pass

    def test_get_article_template(self):
        """
        Test case for get_article_template

        Get a single article template
        """
        pass

    def test_get_article_templates(self):
        """
        Test case for get_article_templates

        List and search article templates
        """
        pass

    def test_get_articles(self):
        """
        Test case for get_articles

        List and search articles
        """
        pass

    def test_update_article(self):
        """
        Test case for update_article

        Update an existing article
        """
        pass

    def test_update_article_template(self):
        """
        Test case for update_article_template

        Update an article template
        """
        pass


if __name__ == '__main__':
    unittest.main()
