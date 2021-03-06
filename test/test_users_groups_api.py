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
from knetik_cloud.apis.users_groups_api import UsersGroupsApi


class TestUsersGroupsApi(unittest.TestCase):
    """ UsersGroupsApi unit test stubs """

    def setUp(self):
        self.api = knetik_cloud.apis.users_groups_api.UsersGroupsApi()

    def tearDown(self):
        pass

    def test_add_member_to_group(self):
        """
        Test case for add_member_to_group

        Adds a new member to the group
        """
        pass

    def test_add_members_to_group(self):
        """
        Test case for add_members_to_group

        Adds multiple members to the group
        """
        pass

    def test_create_group(self):
        """
        Test case for create_group

        Create a group
        """
        pass

    def test_create_group_member_template(self):
        """
        Test case for create_group_member_template

        Create an group member template
        """
        pass

    def test_create_group_template(self):
        """
        Test case for create_group_template

        Create a group template
        """
        pass

    def test_delete_group(self):
        """
        Test case for delete_group

        Removes a group from the system
        """
        pass

    def test_delete_group_member_template(self):
        """
        Test case for delete_group_member_template

        Delete an group member template
        """
        pass

    def test_delete_group_template(self):
        """
        Test case for delete_group_template

        Delete a group template
        """
        pass

    def test_disable_group_notification(self):
        """
        Test case for disable_group_notification

        Enable or disable notification of group messages
        """
        pass

    def test_get_group(self):
        """
        Test case for get_group

        Loads a specific group's details
        """
        pass

    def test_get_group_ancestors(self):
        """
        Test case for get_group_ancestors

        Get group ancestors
        """
        pass

    def test_get_group_member(self):
        """
        Test case for get_group_member

        Get a user from a group
        """
        pass

    def test_get_group_member_template(self):
        """
        Test case for get_group_member_template

        Get a single group member template
        """
        pass

    def test_get_group_member_templates(self):
        """
        Test case for get_group_member_templates

        List and search group member templates
        """
        pass

    def test_get_group_members(self):
        """
        Test case for get_group_members

        Lists members of the group
        """
        pass

    def test_get_group_messages(self):
        """
        Test case for get_group_messages

        Get a list of group messages
        """
        pass

    def test_get_group_template(self):
        """
        Test case for get_group_template

        Get a single group template
        """
        pass

    def test_get_group_templates(self):
        """
        Test case for get_group_templates

        List and search group templates
        """
        pass

    def test_get_groups_for_user(self):
        """
        Test case for get_groups_for_user

        List groups a user is in
        """
        pass

    def test_list_groups(self):
        """
        Test case for list_groups

        List and search groups
        """
        pass

    def test_post_group_message(self):
        """
        Test case for post_group_message

        Send a group message
        """
        pass

    def test_remove_group_member(self):
        """
        Test case for remove_group_member

        Removes a user from a group
        """
        pass

    def test_update_group(self):
        """
        Test case for update_group

        Update a group
        """
        pass

    def test_update_group_member_properties(self):
        """
        Test case for update_group_member_properties

        Change a user's order
        """
        pass

    def test_update_group_member_properties1(self):
        """
        Test case for update_group_member_properties1

        Change a user's membership properties
        """
        pass

    def test_update_group_member_status(self):
        """
        Test case for update_group_member_status

        Change a user's status
        """
        pass

    def test_update_group_member_template(self):
        """
        Test case for update_group_member_template

        Update an group member template
        """
        pass

    def test_update_group_template(self):
        """
        Test case for update_group_template

        Update a group template
        """
        pass


if __name__ == '__main__':
    unittest.main()
