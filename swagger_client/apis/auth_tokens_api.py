# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com

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

from ..configuration import Configuration
from ..api_client import ApiClient


class AuthTokensApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_token(self, username, client_id, **kwargs):
        """
        Delete a token by username and client id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_token(username, client_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str username: The username of the user (required)
        :param str client_id: The id of the client (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_token_with_http_info(username, client_id, **kwargs)
        else:
            (data) = self.delete_token_with_http_info(username, client_id, **kwargs)
            return data

    def delete_token_with_http_info(self, username, client_id, **kwargs):
        """
        Delete a token by username and client id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_token_with_http_info(username, client_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str username: The username of the user (required)
        :param str client_id: The id of the client (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'client_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `delete_token`")
        # verify the required parameter 'client_id' is set
        if ('client_id' not in params) or (params['client_id'] is None):
            raise ValueError("Missing the required parameter `client_id` when calling `delete_token`")


        collection_formats = {}

        resource_path = '/auth/tokens/{username}/{client_id}'.replace('{format}', 'json')
        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']
        if 'client_id' in params:
            path_params['client_id'] = params['client_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['knetik_oauth']

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_tokens(self, username, **kwargs):
        """
        Delete all tokens by username
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_tokens(username, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str username: The username of the user (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_tokens_with_http_info(username, **kwargs)
        else:
            (data) = self.delete_tokens_with_http_info(username, **kwargs)
            return data

    def delete_tokens_with_http_info(self, username, **kwargs):
        """
        Delete all tokens by username
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_tokens_with_http_info(username, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str username: The username of the user (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username']
        all_params.append('callback')
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
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `delete_tokens`")


        collection_formats = {}

        resource_path = '/auth/tokens/{username}'.replace('{format}', 'json')
        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['knetik_oauth']

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_token(self, username, client_id, **kwargs):
        """
        Get a single token by username and client id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_token(username, client_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str username: The username of the user (required)
        :param str client_id: The id of the client (required)
        :return: OauthAccessTokenResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_token_with_http_info(username, client_id, **kwargs)
        else:
            (data) = self.get_token_with_http_info(username, client_id, **kwargs)
            return data

    def get_token_with_http_info(self, username, client_id, **kwargs):
        """
        Get a single token by username and client id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_token_with_http_info(username, client_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str username: The username of the user (required)
        :param str client_id: The id of the client (required)
        :return: OauthAccessTokenResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username', 'client_id']
        all_params.append('callback')
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

        resource_path = '/auth/tokens/{username}/{client_id}'.replace('{format}', 'json')
        path_params = {}
        if 'username' in params:
            path_params['username'] = params['username']
        if 'client_id' in params:
            path_params['client_id'] = params['client_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['knetik_oauth']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='OauthAccessTokenResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_tokens(self, **kwargs):
        """
        List usernames and client ids
        Token value not shown
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tokens(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
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
        if kwargs.get('callback'):
            return self.get_tokens_with_http_info(**kwargs)
        else:
            (data) = self.get_tokens_with_http_info(**kwargs)
            return data

    def get_tokens_with_http_info(self, **kwargs):
        """
        List usernames and client ids
        Token value not shown
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tokens_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
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
        all_params.append('callback')
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

        resource_path = '/auth/tokens'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'filter_client_id' in params:
            query_params['filter_client_id'] = params['filter_client_id']
        if 'filter_username' in params:
            query_params['filter_username'] = params['filter_username']
        if 'size' in params:
            query_params['size'] = params['size']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'order' in params:
            query_params['order'] = params['order']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['knetik_oauth']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceOauthAccessTokenResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
