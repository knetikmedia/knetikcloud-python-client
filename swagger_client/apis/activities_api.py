# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

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


class ActivitiesApi(object):
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

    def complete_activity_occurrence_using_put(self, activity_occurrence_id, **kwargs):
        """
        Updated the status of an activity occurrence
        If setting to 'FINISHED' you must POST to /results instead to record the metrics and get synchronous reward results
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.complete_activity_occurrence_using_put(activity_occurrence_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int activity_occurrence_id: The id of the activity occurrence (required)
        :param str activity_cccurrence_status: The activity occurrence status object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.complete_activity_occurrence_using_put_with_http_info(activity_occurrence_id, **kwargs)
        else:
            (data) = self.complete_activity_occurrence_using_put_with_http_info(activity_occurrence_id, **kwargs)
            return data

    def complete_activity_occurrence_using_put_with_http_info(self, activity_occurrence_id, **kwargs):
        """
        Updated the status of an activity occurrence
        If setting to 'FINISHED' you must POST to /results instead to record the metrics and get synchronous reward results
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.complete_activity_occurrence_using_put_with_http_info(activity_occurrence_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int activity_occurrence_id: The id of the activity occurrence (required)
        :param str activity_cccurrence_status: The activity occurrence status object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activity_occurrence_id', 'activity_cccurrence_status']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method complete_activity_occurrence_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activity_occurrence_id' is set
        if ('activity_occurrence_id' not in params) or (params['activity_occurrence_id'] is None):
            raise ValueError("Missing the required parameter `activity_occurrence_id` when calling `complete_activity_occurrence_using_put`")


        collection_formats = {}

        resource_path = '/activity-occurrences/{activity_occurrence_id}/status'.replace('{format}', 'json')
        path_params = {}
        if 'activity_occurrence_id' in params:
            path_params['activity_occurrence_id'] = params['activity_occurrence_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'activity_cccurrence_status' in params:
            body_params = params['activity_cccurrence_status']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

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

    def create_activity_occurrence_using_post(self, **kwargs):
        """
        Create a new activity occurrence
        Has to enforce extra rules if not used as an admin
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_activity_occurrence_using_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool test: if true, indicates that the occurrence should NOT be created. This can be used to test for eligibility and valid settings
        :param ActivityOccurrenceResource activity_occurrence_resource: The activity occurrence object
        :return: ActivityOccurrenceResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_activity_occurrence_using_post_with_http_info(**kwargs)
        else:
            (data) = self.create_activity_occurrence_using_post_with_http_info(**kwargs)
            return data

    def create_activity_occurrence_using_post_with_http_info(self, **kwargs):
        """
        Create a new activity occurrence
        Has to enforce extra rules if not used as an admin
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_activity_occurrence_using_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool test: if true, indicates that the occurrence should NOT be created. This can be used to test for eligibility and valid settings
        :param ActivityOccurrenceResource activity_occurrence_resource: The activity occurrence object
        :return: ActivityOccurrenceResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['test', 'activity_occurrence_resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_activity_occurrence_using_post" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/activity-occurrences'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'test' in params:
            query_params['test'] = params['test']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'activity_occurrence_resource' in params:
            body_params = params['activity_occurrence_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ActivityOccurrenceResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_activity_using_post(self, **kwargs):
        """
        Create an activity
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_activity_using_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ActivityResource activity_resource: The activity resource object
        :return: ActivityResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_activity_using_post_with_http_info(**kwargs)
        else:
            (data) = self.create_activity_using_post_with_http_info(**kwargs)
            return data

    def create_activity_using_post_with_http_info(self, **kwargs):
        """
        Create an activity
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_activity_using_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ActivityResource activity_resource: The activity resource object
        :return: ActivityResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activity_resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_activity_using_post" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/activities'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'activity_resource' in params:
            body_params = params['activity_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ActivityResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_activity_using_delete(self, id, **kwargs):
        """
        Delete an activity
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_activity_using_delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: The id of the activity (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_activity_using_delete_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_activity_using_delete_with_http_info(id, **kwargs)
            return data

    def delete_activity_using_delete_with_http_info(self, id, **kwargs):
        """
        Delete an activity
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_activity_using_delete_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: The id of the activity (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_activity_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_activity_using_delete`")


        collection_formats = {}

        resource_path = '/activities/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

    def get_activities_using_get(self, **kwargs):
        """
        List activity definitions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_activities_using_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool filter_template: Filter for activities that are templates, or specifically not if false
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageBareActivityResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_activities_using_get_with_http_info(**kwargs)
        else:
            (data) = self.get_activities_using_get_with_http_info(**kwargs)
            return data

    def get_activities_using_get_with_http_info(self, **kwargs):
        """
        List activity definitions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_activities_using_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool filter_template: Filter for activities that are templates, or specifically not if false
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageBareActivityResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_template', 'size', 'page', 'order']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_activities_using_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/activities'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'filter_template' in params:
            query_params['filter_template'] = params['filter_template']
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
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageBareActivityResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_activity_using_get(self, id, **kwargs):
        """
        Get a single activity
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_activity_using_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: The id of the activity (required)
        :return: ActivityResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_activity_using_get_with_http_info(id, **kwargs)
        else:
            (data) = self.get_activity_using_get_with_http_info(id, **kwargs)
            return data

    def get_activity_using_get_with_http_info(self, id, **kwargs):
        """
        Get a single activity
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_activity_using_get_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: The id of the activity (required)
        :return: ActivityResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_activity_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_activity_using_get`")


        collection_formats = {}

        resource_path = '/activities/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ActivityResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_results_using_post(self, activity_occurrence_id, **kwargs):
        """
        Sets the status of an activity occurrence to FINISHED and logs metrics
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_results_using_post(activity_occurrence_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int activity_occurrence_id: The id of the activity occurrence (required)
        :param ActivityOccurrenceResults activity_occurrence_results: The activity occurrence object
        :return: ActivityOccurrenceResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_results_using_post_with_http_info(activity_occurrence_id, **kwargs)
        else:
            (data) = self.post_results_using_post_with_http_info(activity_occurrence_id, **kwargs)
            return data

    def post_results_using_post_with_http_info(self, activity_occurrence_id, **kwargs):
        """
        Sets the status of an activity occurrence to FINISHED and logs metrics
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_results_using_post_with_http_info(activity_occurrence_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int activity_occurrence_id: The id of the activity occurrence (required)
        :param ActivityOccurrenceResults activity_occurrence_results: The activity occurrence object
        :return: ActivityOccurrenceResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activity_occurrence_id', 'activity_occurrence_results']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_results_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activity_occurrence_id' is set
        if ('activity_occurrence_id' not in params) or (params['activity_occurrence_id'] is None):
            raise ValueError("Missing the required parameter `activity_occurrence_id` when calling `post_results_using_post`")


        collection_formats = {}

        resource_path = '/activity-occurrences/{activity_occurrence_id}/results'.replace('{format}', 'json')
        path_params = {}
        if 'activity_occurrence_id' in params:
            path_params['activity_occurrence_id'] = params['activity_occurrence_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'activity_occurrence_results' in params:
            body_params = params['activity_occurrence_results']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ActivityOccurrenceResults',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_activity_using_put(self, id, **kwargs):
        """
        Update an activity
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_activity_using_put(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: The id of the activity (required)
        :param ActivityResource activity_resource: The activity resource object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_activity_using_put_with_http_info(id, **kwargs)
        else:
            (data) = self.update_activity_using_put_with_http_info(id, **kwargs)
            return data

    def update_activity_using_put_with_http_info(self, id, **kwargs):
        """
        Update an activity
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_activity_using_put_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: The id of the activity (required)
        :param ActivityResource activity_resource: The activity resource object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'activity_resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_activity_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_activity_using_put`")


        collection_formats = {}

        resource_path = '/activities/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'activity_resource' in params:
            body_params = params['activity_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

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
