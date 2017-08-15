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


class SearchApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_search_index(self, type, id, **kwargs):
        """
        Add a new object to an index
        Mainly intended for internal use.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_search_index(type, id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: The index type (required)
        :param str id: The ID of the object (required)
        :param object object: The object to add
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_search_index_with_http_info(type, id, **kwargs)
        else:
            (data) = self.add_search_index_with_http_info(type, id, **kwargs)
            return data

    def add_search_index_with_http_info(self, type, id, **kwargs):
        """
        Add a new object to an index
        Mainly intended for internal use.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_search_index_with_http_info(type, id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: The index type (required)
        :param str id: The ID of the object (required)
        :param object object: The object to add
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'id', 'object']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_search_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params) or (params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `add_search_index`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_search_index`")


        collection_formats = {}

        path_params = {}
        if 'type' in params:
            path_params['type'] = params['type']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'object' in params:
            body_params = params['object']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/search/index/{type}/{id}', 'POST',
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

    def add_search_mappings(self, **kwargs):
        """
        Register reference mappings
        Add a new type mapping to connect data from one index to another, or discover an exsting one. Mainly intended for internal use.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_search_mappings(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[SearchReferenceMapping] mappings: The mappings to add
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.add_search_mappings_with_http_info(**kwargs)
        else:
            (data) = self.add_search_mappings_with_http_info(**kwargs)
            return data

    def add_search_mappings_with_http_info(self, **kwargs):
        """
        Register reference mappings
        Add a new type mapping to connect data from one index to another, or discover an exsting one. Mainly intended for internal use.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_search_mappings_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[SearchReferenceMapping] mappings: The mappings to add
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['mappings']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_search_mappings" % key
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
        if 'mappings' in params:
            body_params = params['mappings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/search/mappings', 'POST',
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

    def delete_search_index(self, type, id, **kwargs):
        """
        Delete an object
        Mainly intended for internal use. Requires SEARCH_ADMIN.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_search_index(type, id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: The index type (required)
        :param str id: The ID of the object to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_search_index_with_http_info(type, id, **kwargs)
        else:
            (data) = self.delete_search_index_with_http_info(type, id, **kwargs)
            return data

    def delete_search_index_with_http_info(self, type, id, **kwargs):
        """
        Delete an object
        Mainly intended for internal use. Requires SEARCH_ADMIN.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_search_index_with_http_info(type, id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: The index type (required)
        :param str id: The ID of the object to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_search_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params) or (params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `delete_search_index`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_search_index`")


        collection_formats = {}

        path_params = {}
        if 'type' in params:
            path_params['type'] = params['type']
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

        return self.api_client.call_api('/search/index/{type}/{id}', 'DELETE',
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

    def delete_search_indexes(self, type, **kwargs):
        """
        Delete all objects in an index
        Mainly intended for internal use
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_search_indexes(type, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: The index type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_search_indexes_with_http_info(type, **kwargs)
        else:
            (data) = self.delete_search_indexes_with_http_info(type, **kwargs)
            return data

    def delete_search_indexes_with_http_info(self, type, **kwargs):
        """
        Delete all objects in an index
        Mainly intended for internal use
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_search_indexes_with_http_info(type, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: The index type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_search_indexes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params) or (params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `delete_search_indexes`")


        collection_formats = {}

        path_params = {}
        if 'type' in params:
            path_params['type'] = params['type']

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

        return self.api_client.call_api('/search/index/{type}', 'DELETE',
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

    def search_index(self, type, **kwargs):
        """
        Search an index
        The body is an ElasticSearch query in JSON format. Please see their <a href='https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html'>documentation</a> for details on the format and search options. The searchable object's format depends on on the type. See individual search endpoints on other resources for details on their format.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_index(type, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: The index type (required)
        :param object query: The query to be used for the search
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageResourceMapstringobject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_index_with_http_info(type, **kwargs)
        else:
            (data) = self.search_index_with_http_info(type, **kwargs)
            return data

    def search_index_with_http_info(self, type, **kwargs):
        """
        Search an index
        The body is an ElasticSearch query in JSON format. Please see their <a href='https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html'>documentation</a> for details on the format and search options. The searchable object's format depends on on the type. See individual search endpoints on other resources for details on their format.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_index_with_http_info(type, async=True)
        >>> result = thread.get()

        :param async bool
        :param str type: The index type (required)
        :param object query: The query to be used for the search
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageResourceMapstringobject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'query', 'size', 'page']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params) or (params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `search_index`")


        collection_formats = {}

        path_params = {}
        if 'type' in params:
            path_params['type'] = params['type']

        query_params = []
        if 'size' in params:
            query_params.append(('size', params['size']))
        if 'page' in params:
            query_params.append(('page', params['page']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query' in params:
            body_params = params['query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/search/index/{type}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceMapstringobject',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
