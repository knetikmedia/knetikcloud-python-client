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


class MediaModerationApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_flag(self, **kwargs):
        """
        Add a flag
        <b>Permissions Needed:</b> ANY
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_flag(async=True)
        >>> result = thread.get()

        :param async bool
        :param FlagResource flag_resource: The flag resource object
        :return: FlagResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_flag_with_http_info(**kwargs)
        else:
            (data) = self.add_flag_with_http_info(**kwargs)
            return data

    def add_flag_with_http_info(self, **kwargs):
        """
        Add a flag
        <b>Permissions Needed:</b> ANY
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_flag_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param FlagResource flag_resource: The flag resource object
        :return: FlagResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['flag_resource']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_flag" % key
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
        if 'flag_resource' in params:
            body_params = params['flag_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/moderation/flags', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FlagResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_flag(self, **kwargs):
        """
        Delete a flag
        <b>Permissions Needed:</b> MODERATION_ADMIN or owner
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_flag(async=True)
        >>> result = thread.get()

        :param async bool
        :param str context_name: The name of the context
        :param str context_id: The id of the context
        :param int user_id: The id of the user
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_flag_with_http_info(**kwargs)
        else:
            (data) = self.delete_flag_with_http_info(**kwargs)
            return data

    def delete_flag_with_http_info(self, **kwargs):
        """
        Delete a flag
        <b>Permissions Needed:</b> MODERATION_ADMIN or owner
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_flag_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str context_name: The name of the context
        :param str context_id: The id of the context
        :param int user_id: The id of the user
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['context_name', 'context_id', 'user_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_flag" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'context_name' in params:
            query_params.append(('context_name', params['context_name']))
        if 'context_id' in params:
            query_params.append(('context_id', params['context_id']))
        if 'user_id' in params:
            query_params.append(('user_id', params['user_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/moderation/flags', 'DELETE',
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

    def get_flags(self, **kwargs):
        """
        Returns a page of flags
        <b>Permissions Needed:</b> MODERATION_ADMIN or owner
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_flags(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter_context: Filter by flag context
        :param str filter_context_id: Filter by flag context ID
        :param int filter_user_id: Filter by user ID
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageResourceFlagResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_flags_with_http_info(**kwargs)
        else:
            (data) = self.get_flags_with_http_info(**kwargs)
            return data

    def get_flags_with_http_info(self, **kwargs):
        """
        Returns a page of flags
        <b>Permissions Needed:</b> MODERATION_ADMIN or owner
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_flags_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str filter_context: Filter by flag context
        :param str filter_context_id: Filter by flag context ID
        :param int filter_user_id: Filter by user ID
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageResourceFlagResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_context', 'filter_context_id', 'filter_user_id', 'size', 'page']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_flags" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter_context' in params:
            query_params.append(('filter_context', params['filter_context']))
        if 'filter_context_id' in params:
            query_params.append(('filter_context_id', params['filter_context_id']))
        if 'filter_user_id' in params:
            query_params.append(('filter_user_id', params['filter_user_id']))
        if 'size' in params:
            query_params.append(('size', params['size']))
        if 'page' in params:
            query_params.append(('page', params['page']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/moderation/flags', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceFlagResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_moderation_report(self, id, **kwargs):
        """
        Get a flag report
        <b>Permissions Needed:</b> MODERATION_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_moderation_report(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The flag report id (required)
        :return: FlagReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_moderation_report_with_http_info(id, **kwargs)
        else:
            (data) = self.get_moderation_report_with_http_info(id, **kwargs)
            return data

    def get_moderation_report_with_http_info(self, id, **kwargs):
        """
        Get a flag report
        <b>Permissions Needed:</b> MODERATION_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_moderation_report_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The flag report id (required)
        :return: FlagReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_moderation_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_moderation_report`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

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

        return self.api_client.call_api('/moderation/reports/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FlagReportResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_moderation_reports(self, **kwargs):
        """
        Returns a page of flag reports
        Context can be either a free-form string or a pre-defined context name. <br><br><b>Permissions Needed:</b> MODERATION_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_moderation_reports(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool exclude_resolved: Ignore resolved context
        :param str filter_context: Filter by moderation context
        :param str filter_context_id: Filter by moderation context ID
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceFlagReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_moderation_reports_with_http_info(**kwargs)
        else:
            (data) = self.get_moderation_reports_with_http_info(**kwargs)
            return data

    def get_moderation_reports_with_http_info(self, **kwargs):
        """
        Returns a page of flag reports
        Context can be either a free-form string or a pre-defined context name. <br><br><b>Permissions Needed:</b> MODERATION_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_moderation_reports_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool exclude_resolved: Ignore resolved context
        :param str filter_context: Filter by moderation context
        :param str filter_context_id: Filter by moderation context ID
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceFlagReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['exclude_resolved', 'filter_context', 'filter_context_id', 'size', 'page', 'order']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_moderation_reports" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'exclude_resolved' in params:
            query_params.append(('exclude_resolved', params['exclude_resolved']))
        if 'filter_context' in params:
            query_params.append(('filter_context', params['filter_context']))
        if 'filter_context_id' in params:
            query_params.append(('filter_context_id', params['filter_context_id']))
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

        return self.api_client.call_api('/moderation/reports', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceFlagReportResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_moderation_report(self, id, **kwargs):
        """
        Update a flag report
        Lets you set the resolution of a report. Resolution types is {banned,ignore} in case of 'banned' you will need to pass the reason. <br><br><b>Permissions Needed:</b> MODERATION_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_moderation_report(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The flag report id (required)
        :param FlagReportResource flag_report_resource: The new flag report
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_moderation_report_with_http_info(id, **kwargs)
        else:
            (data) = self.update_moderation_report_with_http_info(id, **kwargs)
            return data

    def update_moderation_report_with_http_info(self, id, **kwargs):
        """
        Update a flag report
        Lets you set the resolution of a report. Resolution types is {banned,ignore} in case of 'banned' you will need to pass the reason. <br><br><b>Permissions Needed:</b> MODERATION_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_moderation_report_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The flag report id (required)
        :param FlagReportResource flag_report_resource: The new flag report
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'flag_report_resource']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_moderation_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_moderation_report`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'flag_report_resource' in params:
            body_params = params['flag_report_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/moderation/reports/{id}', 'PUT',
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
