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


class AuthTokensApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_tokens(self, **kwargs):
        """
        Delete tokens by username, client id, or both
        <b>Permissions Needed:</b> TOKENS_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_tokens(async=True)
        >>> result = thread.get()

        :param async bool
        :param str username: The username of the user
        :param str client_id: The id of the client
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_tokens_with_http_info(**kwargs)
        else:
            (data) = self.delete_tokens_with_http_info(**kwargs)
            return data

    def delete_tokens_with_http_info(self, **kwargs):
        """
        Delete tokens by username, client id, or both
        <b>Permissions Needed:</b> TOKENS_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_tokens_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str username: The username of the user
        :param str client_id: The id of the client
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'client_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_tokens" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'username' in params:
            query_params.append(('username', params['username']))
        if 'client_id' in params:
            query_params.append(('client_id', params['client_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/auth/tokens', 'DELETE',
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

    def get_token(self, username, client_id, **kwargs):
        """
        Get a single token by username and client id
        <b>Permissions Needed:</b> TOKENS_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_token(username, client_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str username: The username of the user (required)
        :param str client_id: The id of the client (required)
        :return: OauthAccessTokenResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_token_with_http_info(username, client_id, **kwargs)
        else:
            (data) = self.get_token_with_http_info(username, client_id, **kwargs)
            return data

    def get_token_with_http_info(self, username, client_id, **kwargs):
        """
        Get a single token by username and client id
        <b>Permissions Needed:</b> TOKENS_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_token_with_http_info(username, client_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str username: The username of the user (required)
        :param str client_id: The id of the client (required)
        :return: OauthAccessTokenResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'client_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `get_token`")
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params) or (params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `get_token`")


        collection_formats = {}

        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']
        if 'client_id' in params:
            path_params['client_id'] = params['client_id']

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

        return self.api_client.call_api('/auth/tokens/{username}/{client_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='OauthAccessTokenResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_tokens(self, **kwargs):
        """
        List usernames and client ids
        Token value not shown. <br><br><b>Permissions Needed:</b> TOKENS_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tokens(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter_client_id: Filters for token whose client id matches provided string
        :param str filter_username: Filters for token whose username matches provided string
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceOauthAccessTokenResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_tokens_with_http_info(**kwargs)
        else:
            (data) = self.get_tokens_with_http_info(**kwargs)
            return data

    def get_tokens_with_http_info(self, **kwargs):
        """
        List usernames and client ids
        Token value not shown. <br><br><b>Permissions Needed:</b> TOKENS_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tokens_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter_client_id: Filters for token whose client id matches provided string
        :param str filter_username: Filters for token whose username matches provided string
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceOauthAccessTokenResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_client_id', 'filter_username', 'size', 'page', 'order']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tokens" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter_client_id' in params:
            query_params.append(('filter_client_id', params['filter_client_id']))
        if 'filter_username' in params:
            query_params.append(('filter_username', params['filter_username']))
        if 'size' in params:
            query_params.append(('size', params['size']))
        if 'page' in params:
            query_params.append(('page', params['page']))
        if 'order' in params:
            query_params.append(('order', params['order']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/auth/tokens', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceOauthAccessTokenResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
