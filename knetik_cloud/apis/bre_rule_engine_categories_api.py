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


class BRERuleEngineCategoriesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_bre_category_template(self, **kwargs):
        """
        Create a BRE category template
        Templates define a type of BRE category and the properties they have
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_bre_category_template(async=True)
        >>> result = thread.get()

        :param async bool
        :param TemplateResource template: The category template to create
        :return: TemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_bre_category_template_with_http_info(**kwargs)
        else:
            (data) = self.create_bre_category_template_with_http_info(**kwargs)
            return data

    def create_bre_category_template_with_http_info(self, **kwargs):
        """
        Create a BRE category template
        Templates define a type of BRE category and the properties they have
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_bre_category_template_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param TemplateResource template: The category template to create
        :return: TemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['template']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_bre_category_template" % key
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
        if 'template' in params:
            body_params = params['template']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/bre/categories/templates', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TemplateResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_bre_category_template(self, id, **kwargs):
        """
        Delete a BRE category template
        If cascade = 'detach', it will force delete the template even if it's attached to other objects
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_bre_category_template(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :param str cascade: The value needed to delete used templates
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_bre_category_template_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_bre_category_template_with_http_info(id, **kwargs)
            return data

    def delete_bre_category_template_with_http_info(self, id, **kwargs):
        """
        Delete a BRE category template
        If cascade = 'detach', it will force delete the template even if it's attached to other objects
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_bre_category_template_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :param str cascade: The value needed to delete used templates
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cascade']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bre_category_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_bre_category_template`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []
        if 'cascade' in params:
            query_params.append(('cascade', params['cascade']))

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

        return self.api_client.call_api('/bre/categories/templates/{id}', 'DELETE',
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

    def get_bre_categories(self, **kwargs):
        """
        List categories
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_bre_categories(async=True)
        >>> result = thread.get()

        :param async bool
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageResourceBreCategoryResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_bre_categories_with_http_info(**kwargs)
        else:
            (data) = self.get_bre_categories_with_http_info(**kwargs)
            return data

    def get_bre_categories_with_http_info(self, **kwargs):
        """
        List categories
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_bre_categories_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :return: PageResourceBreCategoryResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['size', 'page']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bre_categories" % key
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

        return self.api_client.call_api('/bre/categories', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceBreCategoryResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_bre_category(self, name, **kwargs):
        """
        Get a single category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_bre_category(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The category name (required)
        :return: BreCategoryResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_bre_category_with_http_info(name, **kwargs)
        else:
            (data) = self.get_bre_category_with_http_info(name, **kwargs)
            return data

    def get_bre_category_with_http_info(self, name, **kwargs):
        """
        Get a single category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_bre_category_with_http_info(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The category name (required)
        :return: BreCategoryResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bre_category" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_bre_category`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

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

        return self.api_client.call_api('/bre/categories/{name}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BreCategoryResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_bre_category_template(self, id, **kwargs):
        """
        Get a single BRE category template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_bre_category_template(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :return: TemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_bre_category_template_with_http_info(id, **kwargs)
        else:
            (data) = self.get_bre_category_template_with_http_info(id, **kwargs)
            return data

    def get_bre_category_template_with_http_info(self, id, **kwargs):
        """
        Get a single BRE category template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_bre_category_template_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :return: TemplateResource
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
                    " to method get_bre_category_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_bre_category_template`")


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

        return self.api_client.call_api('/bre/categories/templates/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TemplateResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_bre_category_templates(self, **kwargs):
        """
        List and search BRE category templates
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_bre_category_templates(async=True)
        >>> result = thread.get()

        :param async bool
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceTemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_bre_category_templates_with_http_info(**kwargs)
        else:
            (data) = self.get_bre_category_templates_with_http_info(**kwargs)
            return data

    def get_bre_category_templates_with_http_info(self, **kwargs):
        """
        List and search BRE category templates
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_bre_category_templates_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceTemplateResource
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
                    " to method get_bre_category_templates" % key
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

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/bre/categories/templates', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceTemplateResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_bre_category(self, name, **kwargs):
        """
        Update a category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_bre_category(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The category name (required)
        :param BreCategoryResource category: The updated BRE category information
        :return: BreCategoryResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_bre_category_with_http_info(name, **kwargs)
        else:
            (data) = self.update_bre_category_with_http_info(name, **kwargs)
            return data

    def update_bre_category_with_http_info(self, name, **kwargs):
        """
        Update a category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_bre_category_with_http_info(name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str name: The category name (required)
        :param BreCategoryResource category: The updated BRE category information
        :return: BreCategoryResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'category']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_bre_category" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `update_bre_category`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'category' in params:
            body_params = params['category']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/bre/categories/{name}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BreCategoryResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_bre_category_template(self, id, **kwargs):
        """
        Update a BRE category template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_bre_category_template(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :param TemplateResource template: The updated category template definition
        :return: TemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_bre_category_template_with_http_info(id, **kwargs)
        else:
            (data) = self.update_bre_category_template_with_http_info(id, **kwargs)
            return data

    def update_bre_category_template_with_http_info(self, id, **kwargs):
        """
        Update a BRE category template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_bre_category_template_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :param TemplateResource template: The updated category template definition
        :return: TemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'template']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_bre_category_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_bre_category_template`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'template' in params:
            body_params = params['template']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/bre/categories/templates/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TemplateResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
