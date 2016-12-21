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
from swagger_client.apis.media_videos_api import MediaVideosApi


class TestMediaVideosApi(unittest.TestCase):
    """ MediaVideosApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.media_videos_api.MediaVideosApi()

    def tearDown(self):
        pass

    def test_add_comment_using_post1(self):
        """
        Test case for add_comment_using_post1

        Add a new video comment
        """
        pass

    def test_add_contributor_using_post(self):
        """
        Test case for add_contributor_using_post

        Adds a contributor to a video
        """
        pass

    def test_add_disposition_using_post1(self):
        """
        Test case for add_disposition_using_post1

        Add a new Video disposition
        """
        pass

    def test_add_flag_using_post(self):
        """
        Test case for add_flag_using_post

        Add a new flag
        """
        pass

    def test_add_related_using_post(self):
        """
        Test case for add_related_using_post

        Adds one or more existing videos as related to this one
        """
        pass

    def test_add_video_using_post(self):
        """
        Test case for add_video_using_post

        Adds a new video in the system
        """
        pass

    def test_add_whitelist_using_post(self):
        """
        Test case for add_whitelist_using_post

        Adds a user to a video's whitelist
        """
        pass

    def test_delete_comment_using_delete1(self):
        """
        Test case for delete_comment_using_delete1

        Delete a video comment
        """
        pass

    def test_delete_disposition_using_delete1(self):
        """
        Test case for delete_disposition_using_delete1

        Delete a video comment
        """
        pass

    def test_delete_flag_using_delete(self):
        """
        Test case for delete_flag_using_delete

        Delete a flag
        """
        pass

    def test_delete_relationship_using_delete1(self):
        """
        Test case for delete_relationship_using_delete1

        Delete a video's relationship
        """
        pass

    def test_delete_video_using_delete(self):
        """
        Test case for delete_video_using_delete

        Removes a video from the system if no resources are attached to it
        """
        pass

    def test_get_comments_using_get1(self):
        """
        Test case for get_comments_using_get1

        Returns a page of comments for a video
        """
        pass

    def test_get_dispositions_using_get1(self):
        """
        Test case for get_dispositions_using_get1

        Returns a page of dispositions for a video
        """
        pass

    def test_get_related_using_get(self):
        """
        Test case for get_related_using_get

        Returns a page of video relationships
        """
        pass

    def test_get_user_videos_using_get(self):
        """
        Test case for get_user_videos_using_get

        Get user videos
        """
        pass

    def test_get_video_using_get(self):
        """
        Test case for get_video_using_get

        Loads a specific video details
        """
        pass

    def test_remove_contributor_using_delete(self):
        """
        Test case for remove_contributor_using_delete

        Removes a contributor from a video
        """
        pass

    def test_remove_whitelist_using_delete(self):
        """
        Test case for remove_whitelist_using_delete

        Removes a user from a video's whitelist
        """
        pass

    def test_search_videos_using_get(self):
        """
        Test case for search_videos_using_get

        Search videos using the documented filters
        """
        pass

    def test_update_comment_using_put1(self):
        """
        Test case for update_comment_using_put1

        Update video comment content 
        """
        pass

    def test_update_relationship_using_put1(self):
        """
        Test case for update_relationship_using_put1

        Update a video's relationship details
        """
        pass

    def test_update_video_using_put(self):
        """
        Test case for update_video_using_put

        Modifies a video's details
        """
        pass

    def test_view_video_using_post(self):
        """
        Test case for view_video_using_post

        Increment a video's view count
        """
        pass


if __name__ == '__main__':
    unittest.main()
