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

from ..configuration import Configuration
from ..api_client import ApiClient


class PaymentsApi(object):
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

    def create_payment_method(self, user_id, **kwargs):
        """
        Create a new payment method for a user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_payment_method(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user for whom the payment method is being created (required)
        :param PaymentMethodResource payment_method: Payment method being created
        :return: PaymentMethodResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_payment_method_with_http_info(user_id, **kwargs)
        else:
            (data) = self.create_payment_method_with_http_info(user_id, **kwargs)
            return data

    def create_payment_method_with_http_info(self, user_id, **kwargs):
        """
        Create a new payment method for a user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_payment_method_with_http_info(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user for whom the payment method is being created (required)
        :param PaymentMethodResource payment_method: Payment method being created
        :return: PaymentMethodResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'payment_method']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_payment_method" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `create_payment_method`")


        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_method' in params:
            body_params = params['payment_method']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/users/{user_id}/payment-methods', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PaymentMethodResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_payment_method(self, user_id, id, **kwargs):
        """
        Delete an existing payment method for a user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_payment_method(user_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user for whom the payment method is being updated (required)
        :param int id: ID of the payment method being deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_payment_method_with_http_info(user_id, id, **kwargs)
        else:
            (data) = self.delete_payment_method_with_http_info(user_id, id, **kwargs)
            return data

    def delete_payment_method_with_http_info(self, user_id, id, **kwargs):
        """
        Delete an existing payment method for a user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_payment_method_with_http_info(user_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user for whom the payment method is being updated (required)
        :param int id: ID of the payment method being deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_payment_method" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `delete_payment_method`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_payment_method`")


        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']
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
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/users/{user_id}/payment-methods/{id}', 'DELETE',
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

    def get_payment_method(self, user_id, id, **kwargs):
        """
        Get a single payment method for a user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_payment_method(user_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user for whom the payment method is being retrieved (required)
        :param int id: ID of the payment method being retrieved (required)
        :return: PaymentMethodResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_payment_method_with_http_info(user_id, id, **kwargs)
        else:
            (data) = self.get_payment_method_with_http_info(user_id, id, **kwargs)
            return data

    def get_payment_method_with_http_info(self, user_id, id, **kwargs):
        """
        Get a single payment method for a user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_payment_method_with_http_info(user_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user for whom the payment method is being retrieved (required)
        :param int id: ID of the payment method being retrieved (required)
        :return: PaymentMethodResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment_method" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_payment_method`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_payment_method`")


        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']
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
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/users/{user_id}/payment-methods/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PaymentMethodResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_payment_methods(self, user_id, **kwargs):
        """
        Get all payment methods for a user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_payment_methods(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user for whom the payment methods are being retrieved (required)
        :param str filter_name: Filter for payment methods whose name starts with a given string
        :param str filter_payment_type: Filter for payment methods with a specific payment type
        :param int filter_payment_method_type_id: Filter for payment methods with a specific payment method type by id
        :param str filter_payment_method_type_name: Filter for payment methods whose payment method type name starts with a given string
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: list[PaymentMethodResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_payment_methods_with_http_info(user_id, **kwargs)
        else:
            (data) = self.get_payment_methods_with_http_info(user_id, **kwargs)
            return data

    def get_payment_methods_with_http_info(self, user_id, **kwargs):
        """
        Get all payment methods for a user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_payment_methods_with_http_info(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user for whom the payment methods are being retrieved (required)
        :param str filter_name: Filter for payment methods whose name starts with a given string
        :param str filter_payment_type: Filter for payment methods with a specific payment type
        :param int filter_payment_method_type_id: Filter for payment methods with a specific payment method type by id
        :param str filter_payment_method_type_name: Filter for payment methods whose payment method type name starts with a given string
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: list[PaymentMethodResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'filter_name', 'filter_payment_type', 'filter_payment_method_type_id', 'filter_payment_method_type_name', 'size', 'page', 'order']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment_methods" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_payment_methods`")


        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']

        query_params = []
        if 'filter_name' in params:
            query_params.append(('filter_name', params['filter_name']))
        if 'filter_payment_type' in params:
            query_params.append(('filter_payment_type', params['filter_payment_type']))
        if 'filter_payment_method_type_id' in params:
            query_params.append(('filter_payment_method_type_id', params['filter_payment_method_type_id']))
        if 'filter_payment_method_type_name' in params:
            query_params.append(('filter_payment_method_type_name', params['filter_payment_method_type_name']))
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
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/users/{user_id}/payment-methods', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[PaymentMethodResource]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def payment_authorization(self, **kwargs):
        """
        Authorize payment of an invoice for later capture
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.payment_authorization(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PaymentAuthorizationResource request: Payment authorization request
        :return: PaymentAuthorizationResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.payment_authorization_with_http_info(**kwargs)
        else:
            (data) = self.payment_authorization_with_http_info(**kwargs)
            return data

    def payment_authorization_with_http_info(self, **kwargs):
        """
        Authorize payment of an invoice for later capture
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.payment_authorization_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PaymentAuthorizationResource request: Payment authorization request
        :return: PaymentAuthorizationResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method payment_authorization" % key
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
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/payment/authorizations', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PaymentAuthorizationResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def payment_capture(self, id, **kwargs):
        """
        Capture an existing invoice payment authorization
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.payment_capture(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of the payment authorization to capture (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.payment_capture_with_http_info(id, **kwargs)
        else:
            (data) = self.payment_capture_with_http_info(id, **kwargs)
            return data

    def payment_capture_with_http_info(self, id, **kwargs):
        """
        Capture an existing invoice payment authorization
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.payment_capture_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of the payment authorization to capture (required)
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
                    " to method payment_capture" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `payment_capture`")


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
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/payment/authorizations/{id}/capture', 'POST',
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

    def update_payment_method(self, user_id, id, **kwargs):
        """
        Update an existing payment method for a user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_payment_method(user_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user for whom the payment method is being updated (required)
        :param int id: ID of the payment method being updated (required)
        :param PaymentMethodResource payment_method: The updated payment method data
        :return: PaymentMethodResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_payment_method_with_http_info(user_id, id, **kwargs)
        else:
            (data) = self.update_payment_method_with_http_info(user_id, id, **kwargs)
            return data

    def update_payment_method_with_http_info(self, user_id, id, **kwargs):
        """
        Update an existing payment method for a user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_payment_method_with_http_info(user_id, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: ID of the user for whom the payment method is being updated (required)
        :param int id: ID of the payment method being updated (required)
        :param PaymentMethodResource payment_method: The updated payment method data
        :return: PaymentMethodResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'id', 'payment_method']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_payment_method" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `update_payment_method`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_payment_method`")


        collection_formats = {}

        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_method' in params:
            body_params = params['payment_method']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/users/{user_id}/payment-methods/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PaymentMethodResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
