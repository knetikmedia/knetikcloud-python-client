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


class StoreSalesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_catalog_sale(self, **kwargs):
        """
        Create a sale
        <b>Permissions Needed:</b> SALES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_catalog_sale(async=True)
        >>> result = thread.get()

        :param async bool
        :param CatalogSale catalog_sale: The catalog sale object
        :return: CatalogSale
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_catalog_sale_with_http_info(**kwargs)
        else:
            (data) = self.create_catalog_sale_with_http_info(**kwargs)
            return data

    def create_catalog_sale_with_http_info(self, **kwargs):
        """
        Create a sale
        <b>Permissions Needed:</b> SALES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_catalog_sale_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param CatalogSale catalog_sale: The catalog sale object
        :return: CatalogSale
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['catalog_sale']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_catalog_sale" % key
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
        if 'catalog_sale' in params:
            body_params = params['catalog_sale']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/store/sales', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CatalogSale',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_catalog_sale(self, id, **kwargs):
        """
        Delete a sale
        <b>Permissions Needed:</b> SALES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_catalog_sale(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the sale (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_catalog_sale_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_catalog_sale_with_http_info(id, **kwargs)
            return data

    def delete_catalog_sale_with_http_info(self, id, **kwargs):
        """
        Delete a sale
        <b>Permissions Needed:</b> SALES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_catalog_sale_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the sale (required)
        :return: None
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
                    " to method delete_catalog_sale" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_catalog_sale`")


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

        return self.api_client.call_api('/store/sales/{id}', 'DELETE',
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

    def get_catalog_sale(self, id, **kwargs):
        """
        Get a single sale
        <b>Permissions Needed:</b> SALES_USER or SALES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_catalog_sale(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the sale (required)
        :return: CatalogSale
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_catalog_sale_with_http_info(id, **kwargs)
        else:
            (data) = self.get_catalog_sale_with_http_info(id, **kwargs)
            return data

    def get_catalog_sale_with_http_info(self, id, **kwargs):
        """
        Get a single sale
        <b>Permissions Needed:</b> SALES_USER or SALES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_catalog_sale_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the sale (required)
        :return: CatalogSale
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
                    " to method get_catalog_sale" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_catalog_sale`")


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

        return self.api_client.call_api('/store/sales/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CatalogSale',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_catalog_sales(self, **kwargs):
        """
        List and search sales
        <b>Permissions Needed:</b> SALES_USER or SALES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_catalog_sales(async=True)
        >>> result = thread.get()

        :param async bool
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceCatalogSale
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_catalog_sales_with_http_info(**kwargs)
        else:
            (data) = self.get_catalog_sales_with_http_info(**kwargs)
            return data

    def get_catalog_sales_with_http_info(self, **kwargs):
        """
        List and search sales
        <b>Permissions Needed:</b> SALES_USER or SALES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_catalog_sales_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceCatalogSale
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['size', 'page', 'order']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_catalog_sales" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
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

        return self.api_client.call_api('/store/sales', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceCatalogSale',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_catalog_sale(self, id, **kwargs):
        """
        Update a sale
        <b>Permissions Needed:</b> SALES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_catalog_sale(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the sale (required)
        :param CatalogSale catalog_sale: The catalog sale object
        :return: CatalogSale
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_catalog_sale_with_http_info(id, **kwargs)
        else:
            (data) = self.update_catalog_sale_with_http_info(id, **kwargs)
            return data

    def update_catalog_sale_with_http_info(self, id, **kwargs):
        """
        Update a sale
        <b>Permissions Needed:</b> SALES_ADMIN
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_catalog_sale_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the sale (required)
        :param CatalogSale catalog_sale: The catalog sale object
        :return: CatalogSale
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'catalog_sale']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_catalog_sale" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_catalog_sale`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'catalog_sale' in params:
            body_params = params['catalog_sale']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/store/sales/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CatalogSale',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
