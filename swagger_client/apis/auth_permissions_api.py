# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: Latest
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

    def create_permission_using_post(self, **kwargs):
        """
        Create a new permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_permission_using_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PermissionResource permission_resource: The permission resource object
        :return: PermissionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_permission_using_post_with_http_info(**kwargs)
        else:
            (data) = self.create_permission_using_post_with_http_info(**kwargs)
            return data

    def create_permission_using_post_with_http_info(self, **kwargs):
        """
        Create a new permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_permission_using_post_with_http_info(callback=callback_function)

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
                    " to method create_permission_using_post" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/auth/permissions'.replace('{format}', 'json')
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
            select_header_accept(['*/*'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
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

    def delete_permission_using_delete(self, permission, **kwargs):
        """
        Delete a permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_permission_using_delete(permission, callback=callback_function)

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
            return self.delete_permission_using_delete_with_http_info(permission, **kwargs)
        else:
            (data) = self.delete_permission_using_delete_with_http_info(permission, **kwargs)
            return data

    def delete_permission_using_delete_with_http_info(self, permission, **kwargs):
        """
        Delete a permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_permission_using_delete_with_http_info(permission, callback=callback_function)

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
                    " to method delete_permission_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'permission' is set
        if ('permission' not in params) or (params['permission'] is None):
            raise ValueError("Missing the required parameter `permission` when calling `delete_permission_using_delete`")


        collection_formats = {}

        resource_path = '/auth/permissions/{permission}'.replace('{format}', 'json')
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
            select_header_accept(['*/*'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

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

    def get_permission_using_get(self, permission, **kwargs):
        """
        Get a single permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_permission_using_get(permission, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str permission: The permission value (required)
        :return: PermissionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_permission_using_get_with_http_info(permission, **kwargs)
        else:
            (data) = self.get_permission_using_get_with_http_info(permission, **kwargs)
            return data

    def get_permission_using_get_with_http_info(self, permission, **kwargs):
        """
        Get a single permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_permission_using_get_with_http_info(permission, callback=callback_function)

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
                    " to method get_permission_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'permission' is set
        if ('permission' not in params) or (params['permission'] is None):
            raise ValueError("Missing the required parameter `permission` when calling `get_permission_using_get`")


        collection_formats = {}

        resource_path = '/auth/permissions/{permission}'.replace('{format}', 'json')
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
            select_header_accept(['*/*'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
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

    def get_permission_using_get1(self, **kwargs):
        """
        List and search permissions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_permission_using_get1(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PagePermissionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_permission_using_get1_with_http_info(**kwargs)
        else:
            (data) = self.get_permission_using_get1_with_http_info(**kwargs)
            return data

    def get_permission_using_get1_with_http_info(self, **kwargs):
        """
        List and search permissions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_permission_using_get1_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PagePermissionResource
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
                    " to method get_permission_using_get1" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/auth/permissions'.replace('{format}', 'json')
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
            select_header_accept(['*/*'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PagePermissionResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_permission_using_put(self, permission, **kwargs):
        """
        Update a permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_permission_using_put(permission, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str permission: The permission value (required)
        :param PermissionResource permission_resource: The permission resource object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_permission_using_put_with_http_info(permission, **kwargs)
        else:
            (data) = self.update_permission_using_put_with_http_info(permission, **kwargs)
            return data

    def update_permission_using_put_with_http_info(self, permission, **kwargs):
        """
        Update a permission
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_permission_using_put_with_http_info(permission, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str permission: The permission value (required)
        :param PermissionResource permission_resource: The permission resource object
        :return: None
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
                    " to method update_permission_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'permission' is set
        if ('permission' not in params) or (params['permission'] is None):
            raise ValueError("Missing the required parameter `permission` when calling `update_permission_using_put`")


        collection_formats = {}

        resource_path = '/auth/permissions/{permission}'.replace('{format}', 'json')
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
            select_header_accept(['*/*'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
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
