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


class UtilMaintenanceApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_maintenance(self, **kwargs):
        """
        Delete maintenance info
        <b>Permissions Needed:</b> MAINTENANCE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_maintenance(async=True)
        >>> result = thread.get()

        :param async bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_maintenance_with_http_info(**kwargs)
        else:
            (data) = self.delete_maintenance_with_http_info(**kwargs)
            return data

    def delete_maintenance_with_http_info(self, **kwargs):
        """
        Delete maintenance info
        <b>Permissions Needed:</b> MAINTENANCE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_maintenance_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_maintenance" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/maintenance', 'DELETE',
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

    def get_maintenance(self, **kwargs):
        """
        Get current maintenance info
        Get current maintenance info. 404 if no maintenance. <br><br><b>Permissions Needed:</b> ANY
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_maintenance(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Maintenance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_maintenance_with_http_info(**kwargs)
        else:
            (data) = self.get_maintenance_with_http_info(**kwargs)
            return data

    def get_maintenance_with_http_info(self, **kwargs):
        """
        Get current maintenance info
        Get current maintenance info. 404 if no maintenance. <br><br><b>Permissions Needed:</b> ANY
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_maintenance_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Maintenance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_maintenance" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/maintenance', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Maintenance',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def set_maintenance(self, **kwargs):
        """
        Set current maintenance info
        <b>Permissions Needed:</b> MAINTENANCE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_maintenance(async=True)
        >>> result = thread.get()

        :param async bool
        :param Maintenance maintenance: The maintenance object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.set_maintenance_with_http_info(**kwargs)
        else:
            (data) = self.set_maintenance_with_http_info(**kwargs)
            return data

    def set_maintenance_with_http_info(self, **kwargs):
        """
        Set current maintenance info
        <b>Permissions Needed:</b> MAINTENANCE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.set_maintenance_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param Maintenance maintenance: The maintenance object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['maintenance']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_maintenance" % key
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
        if 'maintenance' in params:
            body_params = params['maintenance']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/maintenance', 'POST',
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

    def update_maintenance(self, **kwargs):
        """
        Update current maintenance info
        <b>Permissions Needed:</b> MAINTENANCE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_maintenance(async=True)
        >>> result = thread.get()

        :param async bool
        :param Maintenance maintenance: The maintenance object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_maintenance_with_http_info(**kwargs)
        else:
            (data) = self.update_maintenance_with_http_info(**kwargs)
            return data

    def update_maintenance_with_http_info(self, **kwargs):
        """
        Update current maintenance info
        <b>Permissions Needed:</b> MAINTENANCE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_maintenance_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param Maintenance maintenance: The maintenance object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['maintenance']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_maintenance" % key
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
        if 'maintenance' in params:
            body_params = params['maintenance']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/maintenance', 'PUT',
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
