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


class PaymentsTransactionsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_transaction(self, id, **kwargs):
        """
        Get the details for a single transaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_transaction(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: id (required)
        :return: TransactionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_transaction_with_http_info(id, **kwargs)
        else:
            (data) = self.get_transaction_with_http_info(id, **kwargs)
            return data

    def get_transaction_with_http_info(self, id, **kwargs):
        """
        Get the details for a single transaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_transaction_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: id (required)
        :return: TransactionResource
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
                    " to method get_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_transaction`")


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

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/transactions/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TransactionResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_transactions(self, **kwargs):
        """
        List and search transactions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_transactions(async=True)
        >>> result = thread.get()

        :param async bool
        :param int filter_invoice: Filter for transactions from a specific invoice
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceTransactionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_transactions_with_http_info(**kwargs)
        else:
            (data) = self.get_transactions_with_http_info(**kwargs)
            return data

    def get_transactions_with_http_info(self, **kwargs):
        """
        List and search transactions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_transactions_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int filter_invoice: Filter for transactions from a specific invoice
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceTransactionResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter_invoice', 'size', 'page', 'order']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transactions" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter_invoice' in params:
            query_params.append(('filter_invoice', params['filter_invoice']))
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

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/transactions', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceTransactionResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def refund_transaction(self, id, **kwargs):
        """
        Refund a payment transaction, in full or in part
        Will not allow for refunding more than the full amount even with multiple partial refunds. Money is refunded to the payment method used to make the original payment. Payment method must support refunds.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.refund_transaction(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the transaction to refund (required)
        :param RefundRequest request: Request containing refund details
        :return: RefundResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.refund_transaction_with_http_info(id, **kwargs)
        else:
            (data) = self.refund_transaction_with_http_info(id, **kwargs)
            return data

    def refund_transaction_with_http_info(self, id, **kwargs):
        """
        Refund a payment transaction, in full or in part
        Will not allow for refunding more than the full amount even with multiple partial refunds. Money is refunded to the payment method used to make the original payment. Payment method must support refunds.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.refund_transaction_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the transaction to refund (required)
        :param RefundRequest request: Request containing refund details
        :return: RefundResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'request']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refund_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `refund_transaction`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/transactions/{id}/refunds', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RefundResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
