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


class ReportingRevenueApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_item_revenue(self, currency_code, **kwargs):
        """
        Get item revenue info
        Get basic info about revenue from sales of items and bundles (not subscriptions, shipping, etc), summed up within a time range. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_item_revenue(currency_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_code: The code for a currency to get sales data for (required)
        :param int start_date: The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time
        :param int end_date: The end of the time range to aggregate, unix timestamp in seconds. Default is end of time
        :return: RevenueReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_item_revenue_with_http_info(currency_code, **kwargs)
        else:
            (data) = self.get_item_revenue_with_http_info(currency_code, **kwargs)
            return data

    def get_item_revenue_with_http_info(self, currency_code, **kwargs):
        """
        Get item revenue info
        Get basic info about revenue from sales of items and bundles (not subscriptions, shipping, etc), summed up within a time range. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_item_revenue_with_http_info(currency_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_code: The code for a currency to get sales data for (required)
        :param int start_date: The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time
        :param int end_date: The end of the time range to aggregate, unix timestamp in seconds. Default is end of time
        :return: RevenueReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency_code', 'start_date', 'end_date']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_item_revenue" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'currency_code' is set
        if ('currency_code' not in params) or (params['currency_code'] is None):
            raise ValueError("Missing the required parameter `currency_code` when calling `get_item_revenue`")


        collection_formats = {}

        path_params = {}
        if 'currency_code' in params:
            path_params['currency_code'] = params['currency_code']

        query_params = []
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/reporting/revenue/item-sales/{currency_code}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RevenueReportResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_refund_revenue(self, currency_code, **kwargs):
        """
        Get refund revenue info
        Get basic info about revenue loss from refunds (for all item types), summed up within a time range. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_refund_revenue(currency_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_code: The code for a currency to get refund data for (required)
        :param int start_date: The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time
        :param int end_date: The end of the time range to aggregate, unix timestamp in seconds. Default is end of time
        :return: RevenueReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_refund_revenue_with_http_info(currency_code, **kwargs)
        else:
            (data) = self.get_refund_revenue_with_http_info(currency_code, **kwargs)
            return data

    def get_refund_revenue_with_http_info(self, currency_code, **kwargs):
        """
        Get refund revenue info
        Get basic info about revenue loss from refunds (for all item types), summed up within a time range. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_refund_revenue_with_http_info(currency_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_code: The code for a currency to get refund data for (required)
        :param int start_date: The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time
        :param int end_date: The end of the time range to aggregate, unix timestamp in seconds. Default is end of time
        :return: RevenueReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency_code', 'start_date', 'end_date']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_refund_revenue" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'currency_code' is set
        if ('currency_code' not in params) or (params['currency_code'] is None):
            raise ValueError("Missing the required parameter `currency_code` when calling `get_refund_revenue`")


        collection_formats = {}

        path_params = {}
        if 'currency_code' in params:
            path_params['currency_code'] = params['currency_code']

        query_params = []
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/reporting/revenue/refunds/{currency_code}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RevenueReportResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_revenue_by_country(self, currency_code, **kwargs):
        """
        Get revenue info by country
        Get basic info about revenue from sales of all types, summed up within a time range and split out by country. Sorted for largest revenue at the top. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_revenue_by_country(currency_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_code: The code for a currency to get sales data for (required)
        :param int start_date: The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time
        :param int end_date: The end of the time range to aggregate, unix timestamp in seconds. Default is end of time
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageResourceRevenueCountryReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_revenue_by_country_with_http_info(currency_code, **kwargs)
        else:
            (data) = self.get_revenue_by_country_with_http_info(currency_code, **kwargs)
            return data

    def get_revenue_by_country_with_http_info(self, currency_code, **kwargs):
        """
        Get revenue info by country
        Get basic info about revenue from sales of all types, summed up within a time range and split out by country. Sorted for largest revenue at the top. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_revenue_by_country_with_http_info(currency_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_code: The code for a currency to get sales data for (required)
        :param int start_date: The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time
        :param int end_date: The end of the time range to aggregate, unix timestamp in seconds. Default is end of time
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageResourceRevenueCountryReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency_code', 'start_date', 'end_date', 'size', 'page']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_revenue_by_country" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'currency_code' is set
        if ('currency_code' not in params) or (params['currency_code'] is None):
            raise ValueError("Missing the required parameter `currency_code` when calling `get_revenue_by_country`")


        collection_formats = {}

        path_params = {}
        if 'currency_code' in params:
            path_params['currency_code'] = params['currency_code']

        query_params = []
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))
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

        return self.api_client.call_api('/reporting/revenue/countries/{currency_code}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceRevenueCountryReportResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_revenue_by_item(self, currency_code, **kwargs):
        """
        Get revenue info by item
        Get basic info about revenue from sales of all types, summed up within a time range and split out by specific item. Sorted for largest revenue at the top. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_revenue_by_item(currency_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_code: The code for a currency to get sales data for (required)
        :param int start_date: The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time
        :param int end_date: The end of the time range to aggregate, unix timestamp in seconds. Default is end of time
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageResourceRevenueProductReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_revenue_by_item_with_http_info(currency_code, **kwargs)
        else:
            (data) = self.get_revenue_by_item_with_http_info(currency_code, **kwargs)
            return data

    def get_revenue_by_item_with_http_info(self, currency_code, **kwargs):
        """
        Get revenue info by item
        Get basic info about revenue from sales of all types, summed up within a time range and split out by specific item. Sorted for largest revenue at the top. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_revenue_by_item_with_http_info(currency_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_code: The code for a currency to get sales data for (required)
        :param int start_date: The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time
        :param int end_date: The end of the time range to aggregate, unix timestamp in seconds. Default is end of time
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageResourceRevenueProductReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency_code', 'start_date', 'end_date', 'size', 'page']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_revenue_by_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'currency_code' is set
        if ('currency_code' not in params) or (params['currency_code'] is None):
            raise ValueError("Missing the required parameter `currency_code` when calling `get_revenue_by_item`")


        collection_formats = {}

        path_params = {}
        if 'currency_code' in params:
            path_params['currency_code'] = params['currency_code']

        query_params = []
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))
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

        return self.api_client.call_api('/reporting/revenue/products/{currency_code}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceRevenueProductReportResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_subscription_revenue(self, currency_code, **kwargs):
        """
        Get subscription revenue info
        Get basic info about revenue from sales of new subscriptions as well as recurring payemnts, summed up within a time range. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_subscription_revenue(currency_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_code: The code for a currency to get sales data for (required)
        :param int start_date: The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time
        :param int end_date: The end of the time range to aggregate, unix timestamp in seconds. Default is end of time
        :return: RevenueReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_subscription_revenue_with_http_info(currency_code, **kwargs)
        else:
            (data) = self.get_subscription_revenue_with_http_info(currency_code, **kwargs)
            return data

    def get_subscription_revenue_with_http_info(self, currency_code, **kwargs):
        """
        Get subscription revenue info
        Get basic info about revenue from sales of new subscriptions as well as recurring payemnts, summed up within a time range. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_subscription_revenue_with_http_info(currency_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_code: The code for a currency to get sales data for (required)
        :param int start_date: The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time
        :param int end_date: The end of the time range to aggregate, unix timestamp in seconds. Default is end of time
        :return: RevenueReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency_code', 'start_date', 'end_date']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscription_revenue" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'currency_code' is set
        if ('currency_code' not in params) or (params['currency_code'] is None):
            raise ValueError("Missing the required parameter `currency_code` when calling `get_subscription_revenue`")


        collection_formats = {}

        path_params = {}
        if 'currency_code' in params:
            path_params['currency_code'] = params['currency_code']

        query_params = []
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/reporting/revenue/subscription-sales/{currency_code}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RevenueReportResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
