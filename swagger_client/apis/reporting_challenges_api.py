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


class ReportingChallengesApi(object):
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

    def get_challenge_event_leaderboard(self, **kwargs):
        """
        Retrieve a challenge event leaderboard details
        Lists all leaderboard entries with additional user details
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_challenge_event_leaderboard(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int filter_event: A sepecific challenge event id
        :return: PageResourceChallengeEventParticipantResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_challenge_event_leaderboard_with_http_info(**kwargs)
        else:
            (data) = self.get_challenge_event_leaderboard_with_http_info(**kwargs)
            return data

    def get_challenge_event_leaderboard_with_http_info(self, **kwargs):
        """
        Retrieve a challenge event leaderboard details
        Lists all leaderboard entries with additional user details
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_challenge_event_leaderboard_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int filter_event: A sepecific challenge event id
        :return: PageResourceChallengeEventParticipantResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_event']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_challenge_event_leaderboard" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/reporting/events/leaderboard'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'filter_event' in params:
            query_params['filter_event'] = params['filter_event']

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
                                        response_type='PageResourceChallengeEventParticipantResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_challenge_event_participants(self, **kwargs):
        """
        Retrieve a challenge event participant details
        Lists all user submitted scores sorted by value, including those that do not apear in the leaderboard due to value or aggregation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_challenge_event_participants(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int filter_event: A sepecific challenge event id
        :return: PageResourceChallengeEventParticipantResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_challenge_event_participants_with_http_info(**kwargs)
        else:
            (data) = self.get_challenge_event_participants_with_http_info(**kwargs)
            return data

    def get_challenge_event_participants_with_http_info(self, **kwargs):
        """
        Retrieve a challenge event participant details
        Lists all user submitted scores sorted by value, including those that do not apear in the leaderboard due to value or aggregation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_challenge_event_participants_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int filter_event: A sepecific challenge event id
        :return: PageResourceChallengeEventParticipantResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_event']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_challenge_event_participants" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/reporting/events/participants'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'filter_event' in params:
            query_params['filter_event'] = params['filter_event']

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
                                        response_type='PageResourceChallengeEventParticipantResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
