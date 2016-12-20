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


class ContentCommentsApi(object):
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

    def add_comment_using_post(self, **kwargs):
        """
        Add a new comment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_comment_using_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CommentResource comment_resource: The comment to be added
        :return: CommentResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_comment_using_post_with_http_info(**kwargs)
        else:
            (data) = self.add_comment_using_post_with_http_info(**kwargs)
            return data

    def add_comment_using_post_with_http_info(self, **kwargs):
        """
        Add a new comment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_comment_using_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CommentResource comment_resource: The comment to be added
        :return: CommentResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['comment_resource']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_comment_using_post" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/comments'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'comment_resource' in params:
            body_params = params['comment_resource']
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
                                        response_type='CommentResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_comment_using_delete(self, id, **kwargs):
        """
        Delete a comment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_comment_using_delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: The comment id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_comment_using_delete_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_comment_using_delete_with_http_info(id, **kwargs)
            return data

    def delete_comment_using_delete_with_http_info(self, id, **kwargs):
        """
        Delete a comment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_comment_using_delete_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: The comment id (required)
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
                    " to method delete_comment_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_comment_using_delete`")


        collection_formats = {}

        resource_path = '/comments/{id}'.replace('{format}', 'json')
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

    def get_comment_using_get(self, id, **kwargs):
        """
        Returns a comment by comment id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_comment_using_get(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: The comment id (required)
        :return: CommentResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_comment_using_get_with_http_info(id, **kwargs)
        else:
            (data) = self.get_comment_using_get_with_http_info(id, **kwargs)
            return data

    def get_comment_using_get_with_http_info(self, id, **kwargs):
        """
        Returns a comment by comment id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_comment_using_get_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: The comment id (required)
        :return: CommentResource
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
                    " to method get_comment_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_comment_using_get`")


        collection_formats = {}

        resource_path = '/comments/{id}'.replace('{format}', 'json')
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
                                        response_type='CommentResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_comments_using_get(self, context, context_id, **kwargs):
        """
        Returns a page of comments
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_comments_using_get(context, context_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str context: Get comments by context type (required)
        :param int context_id: Get comments by context id (required)
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageCommentResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_comments_using_get_with_http_info(context, context_id, **kwargs)
        else:
            (data) = self.get_comments_using_get_with_http_info(context, context_id, **kwargs)
            return data

    def get_comments_using_get_with_http_info(self, context, context_id, **kwargs):
        """
        Returns a page of comments
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_comments_using_get_with_http_info(context, context_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str context: Get comments by context type (required)
        :param int context_id: Get comments by context id (required)
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageCommentResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['context', 'context_id', 'size', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_comments_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'context' is set
        if ('context' not in params) or (params['context'] is None):
            raise ValueError("Missing the required parameter `context` when calling `get_comments_using_get`")
        # verify the required parameter 'context_id' is set
        if ('context_id' not in params) or (params['context_id'] is None):
            raise ValueError("Missing the required parameter `context_id` when calling `get_comments_using_get`")


        collection_formats = {}

        resource_path = '/comments'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'context' in params:
            query_params['context'] = params['context']
        if 'context_id' in params:
            query_params['context_id'] = params['context_id']
        if 'size' in params:
            query_params['size'] = params['size']
        if 'page' in params:
            query_params['page'] = params['page']

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
                                        response_type='PageCommentResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def search_comments_using_post(self, **kwargs):
        """
        Search the comment index
        The body is an ElasticSearch query json. Please see their <a href='https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html'>documentation</a> for details on the format and search options
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_comments_using_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param object query: The search query
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: CommentSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.search_comments_using_post_with_http_info(**kwargs)
        else:
            (data) = self.search_comments_using_post_with_http_info(**kwargs)
            return data

    def search_comments_using_post_with_http_info(self, **kwargs):
        """
        Search the comment index
        The body is an ElasticSearch query json. Please see their <a href='https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html'>documentation</a> for details on the format and search options
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_comments_using_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param object query: The search query
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: CommentSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query', 'size', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_comments_using_post" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/comments/search'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'size' in params:
            query_params['size'] = params['size']
        if 'page' in params:
            query_params['page'] = params['page']

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

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CommentSearch',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_comment_using_put(self, id, **kwargs):
        """
        Update comment content
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_comment_using_put(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: The comment id (required)
        :param str content: The comment content
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_comment_using_put_with_http_info(id, **kwargs)
        else:
            (data) = self.update_comment_using_put_with_http_info(id, **kwargs)
            return data

    def update_comment_using_put_with_http_info(self, id, **kwargs):
        """
        Update comment content
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_comment_using_put_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: The comment id (required)
        :param str content: The comment content
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'content']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_comment_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_comment_using_put`")


        collection_formats = {}

        resource_path = '/comments/{id}/content'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'content' in params:
            body_params = params['content']
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
