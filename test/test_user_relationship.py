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
from swagger_client.models.user_relationship import UserRelationship


class TestUserRelationship(unittest.TestCase):
    """ UserRelationship unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserRelationship(self):
        """
        Test UserRelationship
        """
        model = swagger_client.models.user_relationship.UserRelationship()


if __name__ == '__main__':
    unittest.main()
