# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com.

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class MessagingTopicsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def disable_topic_subscriber(self, id, user_id, disabled, **kwargs):
        """
        Enable or disable messages for a user
        Useful for opt-out options on a single topic. Consider multiple topics for multiple opt-out options. <br><br><b>Permissions Needed:</b> TOPICS_ADMIN or self
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.disable_topic_subscriber(id, user_id, disabled, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the topic (required)
        :param str user_id: The id of the subscriber or 'me' (required)
        :param ValueWrapperboolean disabled: disabled (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.disable_topic_subscriber_with_http_info(id, user_id, disabled, **kwargs)
        else:
            (data) = self.disable_topic_subscriber_with_http_info(id, user_id, disabled, **kwargs)
            return data

    def disable_topic_subscriber_with_http_info(self, id, user_id, disabled, **kwargs):
        """
        Enable or disable messages for a user
        Useful for opt-out options on a single topic. Consider multiple topics for multiple opt-out options. <br><br><b>Permissions Needed:</b> TOPICS_ADMIN or self
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.disable_topic_subscriber_with_http_info(id, user_id, disabled, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the topic (required)
        :param str user_id: The id of the subscriber or 'me' (required)
        :param ValueWrapperboolean disabled: disabled (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'user_id', 'disabled']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method disable_topic_subscriber" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `disable_topic_subscriber`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `disable_topic_subscriber`")
        # verify the required parameter 'disabled' is set
        if ('disabled' not in params) or (params['disabled'] is None):
            raise ValueError("Missing the required parameter `disabled` when calling `disable_topic_subscriber`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'disabled' in params:
            body_params = params['disabled']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/messaging/topics/{id}/subscribers/{user_id}/disabled', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_topic_subscriber(self, id, user_id, **kwargs):
        """
        Get a subscriber to a topic
        <b>Permissions Needed:</b> TOPICS_ADMIN or self
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_topic_subscriber(id, user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the topic (required)
        :param str user_id: The id of the subscriber or 'me' (required)
        :return: TopicSubscriberResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_topic_subscriber_with_http_info(id, user_id, **kwargs)
        else:
            (data) = self.get_topic_subscriber_with_http_info(id, user_id, **kwargs)
            return data

    def get_topic_subscriber_with_http_info(self, id, user_id, **kwargs):
        """
        Get a subscriber to a topic
        <b>Permissions Needed:</b> TOPICS_ADMIN or self
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_topic_subscriber_with_http_info(id, user_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the topic (required)
        :param str user_id: The id of the subscriber or 'me' (required)
        :return: TopicSubscriberResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'user_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_topic_subscriber" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_topic_subscriber`")
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_topic_subscriber`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/messaging/topics/{id}/subscribers/{user_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TopicSubscriberResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_user_topics(self, id, **kwargs):
        """
        Get all messaging topics for a given user
        <b>Permissions Needed:</b> TOPICS_ADMIN or self
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_topics(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the user or 'me' (required)
        :return: PageResourceTopicResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_user_topics_with_http_info(id, **kwargs)
        else:
            (data) = self.get_user_topics_with_http_info(id, **kwargs)
            return data

    def get_user_topics_with_http_info(self, id, **kwargs):
        """
        Get all messaging topics for a given user
        <b>Permissions Needed:</b> TOPICS_ADMIN or self
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_topics_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the user or 'me' (required)
        :return: PageResourceTopicResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_topics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_user_topics`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/users/{id}/topics', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceTopicResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
