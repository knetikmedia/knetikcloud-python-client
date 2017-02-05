# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

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


class BRERuleEngineTriggersApi(object):
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

    def create_trigger_using_post(self, **kwargs):
        """
        Create a trigger
        Customer added triggers will not be fired automatically or have rules associated with them by default. Custom rules must be added to get use from the trigger and it must then be fired from the outside. See the Bre Event services
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_trigger_using_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BreTriggerResource bre_trigger_resource: The BRE trigger resource object
        :return: BreTriggerResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_trigger_using_post_with_http_info(**kwargs)
        else:
            (data) = self.create_trigger_using_post_with_http_info(**kwargs)
            return data

    def create_trigger_using_post_with_http_info(self, **kwargs):
        """
        Create a trigger
        Customer added triggers will not be fired automatically or have rules associated with them by default. Custom rules must be added to get use from the trigger and it must then be fired from the outside. See the Bre Event services
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_trigger_using_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BreTriggerResource bre_trigger_resource: The BRE trigger resource object
        :return: BreTriggerResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bre_trigger_resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_trigger_using_post" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/bre/triggers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bre_trigger_resource' in params:
            body_params = params['bre_trigger_resource']
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
                                        response_type='BreTriggerResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_trigger_using_delete(self, event_name, **kwargs):
        """
        Delete a trigger
        May fail if there are existing rules against it. Cannot delete core triggers
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_trigger_using_delete(event_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str event_name: The trigger event name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_trigger_using_delete_with_http_info(event_name, **kwargs)
        else:
            (data) = self.delete_trigger_using_delete_with_http_info(event_name, **kwargs)
            return data

    def delete_trigger_using_delete_with_http_info(self, event_name, **kwargs):
        """
        Delete a trigger
        May fail if there are existing rules against it. Cannot delete core triggers
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_trigger_using_delete_with_http_info(event_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str event_name: The trigger event name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_trigger_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_name' is set
        if ('event_name' not in params) or (params['event_name'] is None):
            raise ValueError("Missing the required parameter `event_name` when calling `delete_trigger_using_delete`")


        collection_formats = {}

        resource_path = '/bre/triggers/{event_name}'.replace('{format}', 'json')
        path_params = {}
        if 'event_name' in params:
            path_params['event_name'] = params['event_name']

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

    def get_trigger_using_get(self, event_name, **kwargs):
        """
        Get a single trigger
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_trigger_using_get(event_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str event_name: The trigger event name (required)
        :return: BreTriggerResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_trigger_using_get_with_http_info(event_name, **kwargs)
        else:
            (data) = self.get_trigger_using_get_with_http_info(event_name, **kwargs)
            return data

    def get_trigger_using_get_with_http_info(self, event_name, **kwargs):
        """
        Get a single trigger
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_trigger_using_get_with_http_info(event_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str event_name: The trigger event name (required)
        :return: BreTriggerResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_trigger_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_name' is set
        if ('event_name' not in params) or (params['event_name'] is None):
            raise ValueError("Missing the required parameter `event_name` when calling `get_trigger_using_get`")


        collection_formats = {}

        resource_path = '/bre/triggers/{event_name}'.replace('{format}', 'json')
        path_params = {}
        if 'event_name' in params:
            path_params['event_name'] = params['event_name']

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
                                        response_type='BreTriggerResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_triggers_using_get(self, **kwargs):
        """
        List triggers
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_triggers_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool filter_system: Filter for triggers that are system triggers when true, or not when false. Leave off for both mixed
        :param str filter_category: Filter for triggers that are within a specific category
        :param str filter_name: Filter for triggers that have names containing the given string
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageResourceBreTriggerResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_triggers_using_get_with_http_info(**kwargs)
        else:
            (data) = self.get_triggers_using_get_with_http_info(**kwargs)
            return data

    def get_triggers_using_get_with_http_info(self, **kwargs):
        """
        List triggers
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_triggers_using_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool filter_system: Filter for triggers that are system triggers when true, or not when false. Leave off for both mixed
        :param str filter_category: Filter for triggers that are within a specific category
        :param str filter_name: Filter for triggers that have names containing the given string
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageResourceBreTriggerResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_system', 'filter_category', 'filter_name', 'size', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_triggers_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/bre/triggers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'filter_system' in params:
            query_params['filter_system'] = params['filter_system']
        if 'filter_category' in params:
            query_params['filter_category'] = params['filter_category']
        if 'filter_name' in params:
            query_params['filter_name'] = params['filter_name']
        if 'size' in params:
            query_params['size'] = params['size']
        if 'page' in params:
            query_params['page'] = params['page']

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
                                        response_type='PageResourceBreTriggerResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_trigger_using_put(self, event_name, **kwargs):
        """
        Update a trigger
        May fail if new parameters mismatch requirements of existing rules. Cannot update core triggers
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_trigger_using_put(event_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str event_name: The trigger event name (required)
        :param BreTriggerResource bre_trigger_resource: The BRE trigger resource object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_trigger_using_put_with_http_info(event_name, **kwargs)
        else:
            (data) = self.update_trigger_using_put_with_http_info(event_name, **kwargs)
            return data

    def update_trigger_using_put_with_http_info(self, event_name, **kwargs):
        """
        Update a trigger
        May fail if new parameters mismatch requirements of existing rules. Cannot update core triggers
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_trigger_using_put_with_http_info(event_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str event_name: The trigger event name (required)
        :param BreTriggerResource bre_trigger_resource: The BRE trigger resource object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_name', 'bre_trigger_resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_trigger_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_name' is set
        if ('event_name' not in params) or (params['event_name'] is None):
            raise ValueError("Missing the required parameter `event_name` when calling `update_trigger_using_put`")


        collection_formats = {}

        resource_path = '/bre/triggers/{event_name}'.replace('{format}', 'json')
        path_params = {}
        if 'event_name' in params:
            path_params['event_name'] = params['event_name']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bre_trigger_resource' in params:
            body_params = params['bre_trigger_resource']
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
