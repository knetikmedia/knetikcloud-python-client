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


class BRERuleEngineExpressionsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_bre_expression(self, type, **kwargs):
        """
        Lookup a specific expression
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_bre_expression(type, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: Specifiy the type of expression as returned by the listing endpoint (required)
        :return: ExpressionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_bre_expression_with_http_info(type, **kwargs)
        else:
            (data) = self.get_bre_expression_with_http_info(type, **kwargs)
            return data

    def get_bre_expression_with_http_info(self, type, **kwargs):
        """
        Lookup a specific expression
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_bre_expression_with_http_info(type, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: Specifiy the type of expression as returned by the listing endpoint (required)
        :return: ExpressionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bre_expression" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params) or (params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_bre_expression`")


        collection_formats = {}

        path_params = {}
        if 'type' in params:
            path_params['type'] = params['type']

        query_params = []

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
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/bre/expressions/{type}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ExpressionResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_bre_expressions(self, **kwargs):
        """
        Get a list of supported expressions to use in conditions or actions.
        Each resource contains a type and a definition that are read-only, all the other fields must be provided when using the expression in a rule.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_bre_expressions(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter_type_group: Filter for expressions by type group
        :return: list[ExpressionResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_bre_expressions_with_http_info(**kwargs)
        else:
            (data) = self.get_bre_expressions_with_http_info(**kwargs)
            return data

    def get_bre_expressions_with_http_info(self, **kwargs):
        """
        Get a list of supported expressions to use in conditions or actions.
        Each resource contains a type and a definition that are read-only, all the other fields must be provided when using the expression in a rule.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_bre_expressions_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter_type_group: Filter for expressions by type group
        :return: list[ExpressionResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_type_group']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bre_expressions" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter_type_group' in params:
            query_params.append(('filter_type_group', params['filter_type_group']))

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
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/bre/expressions', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[ExpressionResource]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_expression_as_text(self, **kwargs):
        """
        Returns the textual representation of an expression
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_expression_as_text(async=True)
        >>> result = thread.get()

        :param async bool
        :param ExpressionResource expression: The expression resource to be converted
        :return: StringWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_expression_as_text_with_http_info(**kwargs)
        else:
            (data) = self.get_expression_as_text_with_http_info(**kwargs)
            return data

    def get_expression_as_text_with_http_info(self, **kwargs):
        """
        Returns the textual representation of an expression
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_expression_as_text_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param ExpressionResource expression: The expression resource to be converted
        :return: StringWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['expression']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_expression_as_text" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'expression' in params:
            body_params = params['expression']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/bre/expressions', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StringWrapper',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
