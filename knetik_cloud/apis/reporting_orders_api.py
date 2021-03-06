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


class ReportingOrdersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_invoice_reports(self, currency_code, **kwargs):
        """
        Retrieve invoice counts aggregated by time ranges
        <b>Permissions Needed:</b> REPORTING_ORDERS_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_invoice_reports(currency_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_code: The code for a currency to get sales data for (required)
        :param str granularity: The time duration to aggregate by
        :param str filter_payment_status: A payment status to filter results by, can be a comma separated list
        :param str filter_fulfillment_status: An invoice fulfillment status to filter results by, can be a comma separated list
        :param int start_date: The start of the time range to return, unix timestamp in seconds. Default is beginning of time
        :param int end_date: The end of the time range to return, unix timestamp in seconds. Default is end of time
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned
        :return: PageResourceAggregateInvoiceReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_invoice_reports_with_http_info(currency_code, **kwargs)
        else:
            (data) = self.get_invoice_reports_with_http_info(currency_code, **kwargs)
            return data

    def get_invoice_reports_with_http_info(self, currency_code, **kwargs):
        """
        Retrieve invoice counts aggregated by time ranges
        <b>Permissions Needed:</b> REPORTING_ORDERS_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_invoice_reports_with_http_info(currency_code, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_code: The code for a currency to get sales data for (required)
        :param str granularity: The time duration to aggregate by
        :param str filter_payment_status: A payment status to filter results by, can be a comma separated list
        :param str filter_fulfillment_status: An invoice fulfillment status to filter results by, can be a comma separated list
        :param int start_date: The start of the time range to return, unix timestamp in seconds. Default is beginning of time
        :param int end_date: The end of the time range to return, unix timestamp in seconds. Default is end of time
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned
        :return: PageResourceAggregateInvoiceReportResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency_code', 'granularity', 'filter_payment_status', 'filter_fulfillment_status', 'start_date', 'end_date', 'size', 'page']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_invoice_reports" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'currency_code' is set
        if ('currency_code' not in params) or (params['currency_code'] is None):
            raise ValueError("Missing the required parameter `currency_code` when calling `get_invoice_reports`")


        collection_formats = {}

        path_params = {}
        if 'currency_code' in params:
            path_params['currency_code'] = params['currency_code']

        query_params = []
        if 'granularity' in params:
            query_params.append(('granularity', params['granularity']))
        if 'filter_payment_status' in params:
            query_params.append(('filter_payment_status', params['filter_payment_status']))
        if 'filter_fulfillment_status' in params:
            query_params.append(('filter_fulfillment_status', params['filter_fulfillment_status']))
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

        return self.api_client.call_api('/reporting/orders/count/{currency_code}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceAggregateInvoiceReportResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
