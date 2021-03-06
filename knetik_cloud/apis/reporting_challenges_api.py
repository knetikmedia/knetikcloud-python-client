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


class ReportingChallengesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_challenge_event_leaderboard(self, **kwargs):
        """
        Retrieve a challenge event leaderboard details
        Lists all leaderboard entries with additional user details. <br><br><b>Permissions Needed:</b> REPORTING_CHALLENGES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_challenge_event_leaderboard(async=True)
        >>> result = thread.get()

        :param async bool
        :param int filter_event: A sepecific challenge event id
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceChallengeEventParticipantResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_challenge_event_leaderboard_with_http_info(**kwargs)
        else:
            (data) = self.get_challenge_event_leaderboard_with_http_info(**kwargs)
            return data

    def get_challenge_event_leaderboard_with_http_info(self, **kwargs):
        """
        Retrieve a challenge event leaderboard details
        Lists all leaderboard entries with additional user details. <br><br><b>Permissions Needed:</b> REPORTING_CHALLENGES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_challenge_event_leaderboard_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int filter_event: A sepecific challenge event id
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceChallengeEventParticipantResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_event', 'size', 'page', 'order']
        all_params.append('async')
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

        path_params = {}

        query_params = []
        if 'filter_event' in params:
            query_params.append(('filter_event', params['filter_event']))
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

        return self.api_client.call_api('/reporting/events/leaderboard', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceChallengeEventParticipantResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_challenge_event_participants(self, **kwargs):
        """
        Retrieve a challenge event participant details
        Lists all user submitted scores sorted by value, including those that do not apear in the leaderboard due to value or aggregation. <br><br><b>Permissions Needed:</b> REPORTING_CHALLENGES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_challenge_event_participants(async=True)
        >>> result = thread.get()

        :param async bool
        :param int filter_event: A sepecific challenge event id
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceChallengeEventParticipantResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_challenge_event_participants_with_http_info(**kwargs)
        else:
            (data) = self.get_challenge_event_participants_with_http_info(**kwargs)
            return data

    def get_challenge_event_participants_with_http_info(self, **kwargs):
        """
        Retrieve a challenge event participant details
        Lists all user submitted scores sorted by value, including those that do not apear in the leaderboard due to value or aggregation. <br><br><b>Permissions Needed:</b> REPORTING_CHALLENGES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_challenge_event_participants_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int filter_event: A sepecific challenge event id
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceChallengeEventParticipantResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_event', 'size', 'page', 'order']
        all_params.append('async')
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

        path_params = {}

        query_params = []
        if 'filter_event' in params:
            query_params.append(('filter_event', params['filter_event']))
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

        return self.api_client.call_api('/reporting/events/participants', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceChallengeEventParticipantResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
