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


class AuthPermissionsApi(object):
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

    def create_permission(self, **kwargs):
        """
        Create a new permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_permission(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PermissionResource permission_resource: The permission resource object
        :return: PermissionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_permission_with_http_info(**kwargs)
        else:
            (data) = self.create_permission_with_http_info(**kwargs)
            return data

    def create_permission_with_http_info(self, **kwargs):
        """
        Create a new permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_permission_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PermissionResource permission_resource: The permission resource object
        :return: PermissionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['permission_resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_permission" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'permission_resource' in params:
            body_params = params['permission_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/auth/permissions', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PermissionResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_permission(self, permission, **kwargs):
        """
        Delete a permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_permission(permission, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str permission: The permission value (required)
        :param bool force: If true, removes permission assigned to roles
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_permission_with_http_info(permission, **kwargs)
        else:
            (data) = self.delete_permission_with_http_info(permission, **kwargs)
            return data

    def delete_permission_with_http_info(self, permission, **kwargs):
        """
        Delete a permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_permission_with_http_info(permission, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str permission: The permission value (required)
        :param bool force: If true, removes permission assigned to roles
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['permission', 'force']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'permission' is set
        if ('permission' not in params) or (params['permission'] is None):
            raise ValueError("Missing the required parameter `permission` when calling `delete_permission`")


        collection_formats = {}

        path_params = {}
        if 'permission' in params:
            path_params['permission'] = params['permission']

        query_params = {}
        if 'force' in params:
            query_params['force'] = params['force']

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
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/auth/permissions/{permission}', 'DELETE',
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

    def get_permission(self, permission, **kwargs):
        """
        Get a single permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_permission(permission, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str permission: The permission value (required)
        :return: PermissionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_permission_with_http_info(permission, **kwargs)
        else:
            (data) = self.get_permission_with_http_info(permission, **kwargs)
            return data

    def get_permission_with_http_info(self, permission, **kwargs):
        """
        Get a single permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_permission_with_http_info(permission, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str permission: The permission value (required)
        :return: PermissionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['permission']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'permission' is set
        if ('permission' not in params) or (params['permission'] is None):
            raise ValueError("Missing the required parameter `permission` when calling `get_permission`")


        collection_formats = {}

        path_params = {}
        if 'permission' in params:
            path_params['permission'] = params['permission']

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
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/auth/permissions/{permission}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PermissionResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_permissions(self, **kwargs):
        """
        List and search permissions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_permissions(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourcePermissionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_permissions_with_http_info(**kwargs)
        else:
            (data) = self.get_permissions_with_http_info(**kwargs)
            return data

    def get_permissions_with_http_info(self, **kwargs):
        """
        List and search permissions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_permissions_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourcePermissionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['size', 'page', 'order']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_permissions" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = {}
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
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/auth/permissions', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourcePermissionResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_permission(self, permission, **kwargs):
        """
        Update a permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_permission(permission, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str permission: The permission value (required)
        :param PermissionResource permission_resource: The permission resource object
        :return: PermissionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_permission_with_http_info(permission, **kwargs)
        else:
            (data) = self.update_permission_with_http_info(permission, **kwargs)
            return data

    def update_permission_with_http_info(self, permission, **kwargs):
        """
        Update a permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_permission_with_http_info(permission, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str permission: The permission value (required)
        :param PermissionResource permission_resource: The permission resource object
        :return: PermissionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['permission', 'permission_resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_permission" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'permission' is set
        if ('permission' not in params) or (params['permission'] is None):
            raise ValueError("Missing the required parameter `permission` when calling `update_permission`")


        collection_formats = {}

        path_params = {}
        if 'permission' in params:
            path_params['permission'] = params['permission']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'permission_resource' in params:
            body_params = params['permission_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/auth/permissions/{permission}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PermissionResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
