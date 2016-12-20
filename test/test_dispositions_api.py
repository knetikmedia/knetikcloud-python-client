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
from swagger_client.apis.dispositions_api import DispositionsApi


class TestDispositionsApi(unittest.TestCase):
    """ DispositionsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.dispositions_api.DispositionsApi()

    def tearDown(self):
        pass

    def test_add_disposition_using_post(self):
        """
        Test case for add_disposition_using_post

        Add a new disposition. 
        """
        pass

    def test_delete_disposition_using_delete(self):
        """
        Test case for delete_disposition_using_delete

        Delete a disposition
        """
        pass

    def test_get_disposition_count_using_get(self):
        """
        Test case for get_disposition_count_using_get

        Returns a list of disposition counts
        """
        pass

    def test_get_disposition_using_get(self):
        """
        Test case for get_disposition_using_get

        Returns a disposition
        """
        pass

    def test_get_dispositions_using_get(self):
        """
        Test case for get_dispositions_using_get

        Returns a page of dispositions
        """
        pass


if __name__ == '__main__':
    unittest.main()
