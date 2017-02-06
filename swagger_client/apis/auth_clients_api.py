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


class AuthClientsApi(object):
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

    def create_client(self, **kwargs):
        """
        Create a new client
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_client(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ClientResource client_resource: The client resource object
        :return: ClientResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_client_with_http_info(**kwargs)
        else:
            (data) = self.create_client_with_http_info(**kwargs)
            return data

    def create_client_with_http_info(self, **kwargs):
        """
        Create a new client
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_client_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ClientResource client_resource: The client resource object
        :return: ClientResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_client" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/auth/clients'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'client_resource' in params:
            body_params = params['client_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['knetik_oauth']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ClientResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_client(self, client_key, **kwargs):
        """
        Delete a client
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_client(client_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_key: The key of the client (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_client_with_http_info(client_key, **kwargs)
        else:
            (data) = self.delete_client_with_http_info(client_key, **kwargs)
            return data

    def delete_client_with_http_info(self, client_key, **kwargs):
        """
        Delete a client
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_client_with_http_info(client_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_key: The key of the client (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_client" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_key' is set
        if ('client_key' not in params) or (params['client_key'] is None):
            raise ValueError("Missing the required parameter `client_key` when calling `delete_client`")


        collection_formats = {}

        resource_path = '/auth/clients/{client_key}'.replace('{format}', 'json')
        path_params = {}
        if 'client_key' in params:
            path_params['client_key'] = params['client_key']

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

    def get_client(self, client_key, **kwargs):
        """
        Get a single client
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_client(client_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_key: The key of the client (required)
        :return: ClientResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_client_with_http_info(client_key, **kwargs)
        else:
            (data) = self.get_client_with_http_info(client_key, **kwargs)
            return data

    def get_client_with_http_info(self, client_key, **kwargs):
        """
        Get a single client
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_client_with_http_info(client_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_key: The key of the client (required)
        :return: ClientResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_key']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_client" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_key' is set
        if ('client_key' not in params) or (params['client_key'] is None):
            raise ValueError("Missing the required parameter `client_key` when calling `get_client`")


        collection_formats = {}

        resource_path = '/auth/clients/{client_key}'.replace('{format}', 'json')
        path_params = {}
        if 'client_key' in params:
            path_params['client_key'] = params['client_key']

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
                                        response_type='ClientResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_client_grant_types(self, **kwargs):
        """
        List available client grant types
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_client_grant_types(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[GrantTypeResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_client_grant_types_with_http_info(**kwargs)
        else:
            (data) = self.get_client_grant_types_with_http_info(**kwargs)
            return data

    def get_client_grant_types_with_http_info(self, **kwargs):
        """
        List available client grant types
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_client_grant_types_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[GrantTypeResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_client_grant_types" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/auth/clients/grant-types'.replace('{format}', 'json')
        path_params = {}

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
                                        response_type='list[GrantTypeResource]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_clients(self, **kwargs):
        """
        List and search clients
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_clients(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceClientResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_clients_with_http_info(**kwargs)
        else:
            (data) = self.get_clients_with_http_info(**kwargs)
            return data

    def get_clients_with_http_info(self, **kwargs):
        """
        List and search clients
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_clients_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceClientResource
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
                    " to method get_clients" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/auth/clients'.replace('{format}', 'json')
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
        auth_settings = ['knetik_oauth']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceClientResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def set_client_grant_types(self, client_key, **kwargs):
        """
        Set grant types for a client
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_client_grant_types(client_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_key: The key of the client (required)
        :param list[str] grant_list: A list of unique grant types
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.set_client_grant_types_with_http_info(client_key, **kwargs)
        else:
            (data) = self.set_client_grant_types_with_http_info(client_key, **kwargs)
            return data

    def set_client_grant_types_with_http_info(self, client_key, **kwargs):
        """
        Set grant types for a client
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_client_grant_types_with_http_info(client_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_key: The key of the client (required)
        :param list[str] grant_list: A list of unique grant types
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_key', 'grant_list']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_client_grant_types" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_key' is set
        if ('client_key' not in params) or (params['client_key'] is None):
            raise ValueError("Missing the required parameter `client_key` when calling `set_client_grant_types`")


        collection_formats = {}

        resource_path = '/auth/clients/{client_key}/grant-types'.replace('{format}', 'json')
        path_params = {}
        if 'client_key' in params:
            path_params['client_key'] = params['client_key']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'grant_list' in params:
            body_params = params['grant_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['knetik_oauth']

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

    def set_client_redirect_uris(self, client_key, **kwargs):
        """
        Set redirect uris for a client
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_client_redirect_uris(client_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_key: The key of the client (required)
        :param list[str] redirect_list: A list of unique redirect uris
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.set_client_redirect_uris_with_http_info(client_key, **kwargs)
        else:
            (data) = self.set_client_redirect_uris_with_http_info(client_key, **kwargs)
            return data

    def set_client_redirect_uris_with_http_info(self, client_key, **kwargs):
        """
        Set redirect uris for a client
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_client_redirect_uris_with_http_info(client_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_key: The key of the client (required)
        :param list[str] redirect_list: A list of unique redirect uris
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_key', 'redirect_list']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_client_redirect_uris" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_key' is set
        if ('client_key' not in params) or (params['client_key'] is None):
            raise ValueError("Missing the required parameter `client_key` when calling `set_client_redirect_uris`")


        collection_formats = {}

        resource_path = '/auth/clients/{client_key}/redirect-uris'.replace('{format}', 'json')
        path_params = {}
        if 'client_key' in params:
            path_params['client_key'] = params['client_key']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'redirect_list' in params:
            body_params = params['redirect_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['knetik_oauth']

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

    def update_client(self, client_key, **kwargs):
        """
        Update a client
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_client(client_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_key: The key of the client (required)
        :param ClientResource client_resource: The client resource object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_client_with_http_info(client_key, **kwargs)
        else:
            (data) = self.update_client_with_http_info(client_key, **kwargs)
            return data

    def update_client_with_http_info(self, client_key, **kwargs):
        """
        Update a client
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_client_with_http_info(client_key, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str client_key: The key of the client (required)
        :param ClientResource client_resource: The client resource object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['client_key', 'client_resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_client" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'client_key' is set
        if ('client_key' not in params) or (params['client_key'] is None):
            raise ValueError("Missing the required parameter `client_key` when calling `update_client`")


        collection_formats = {}

        resource_path = '/auth/clients/{client_key}'.replace('{format}', 'json')
        path_params = {}
        if 'client_key' in params:
            path_params['client_key'] = params['client_key']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'client_resource' in params:
            body_params = params['client_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['knetik_oauth']

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
