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


class StoreShippingApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_shipping_item(self, **kwargs):
        """
        Create a shipping item
        A shipping item represents a shipping option and cost. SKUs have to be unique in the entire store.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_shipping_item(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool cascade: Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values.
        :param ShippingItem shipping_item: The shipping item object
        :return: ShippingItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_shipping_item_with_http_info(**kwargs)
        else:
            (data) = self.create_shipping_item_with_http_info(**kwargs)
            return data

    def create_shipping_item_with_http_info(self, **kwargs):
        """
        Create a shipping item
        A shipping item represents a shipping option and cost. SKUs have to be unique in the entire store.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_shipping_item_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool cascade: Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values.
        :param ShippingItem shipping_item: The shipping item object
        :return: ShippingItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cascade', 'shipping_item']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_shipping_item" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cascade' in params:
            query_params.append(('cascade', params['cascade']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'shipping_item' in params:
            body_params = params['shipping_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/store/shipping', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ShippingItem',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_shipping_template(self, **kwargs):
        """
        Create a shipping template
        Shipping Templates define a type of shipping and the properties they have.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_shipping_template(async=True)
        >>> result = thread.get()

        :param async bool
        :param ItemTemplateResource shipping_template_resource: The new shipping template
        :return: ItemTemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_shipping_template_with_http_info(**kwargs)
        else:
            (data) = self.create_shipping_template_with_http_info(**kwargs)
            return data

    def create_shipping_template_with_http_info(self, **kwargs):
        """
        Create a shipping template
        Shipping Templates define a type of shipping and the properties they have.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_shipping_template_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param ItemTemplateResource shipping_template_resource: The new shipping template
        :return: ItemTemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shipping_template_resource']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_shipping_template" % key
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
        if 'shipping_template_resource' in params:
            body_params = params['shipping_template_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/store/shipping/templates', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ItemTemplateResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_shipping_item(self, id, **kwargs):
        """
        Delete a shipping item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_shipping_item(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the shipping item (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_shipping_item_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_shipping_item_with_http_info(id, **kwargs)
            return data

    def delete_shipping_item_with_http_info(self, id, **kwargs):
        """
        Delete a shipping item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_shipping_item_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the shipping item (required)
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
                    " to method delete_shipping_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_shipping_item`")


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

        return self.api_client.call_api('/store/shipping/{id}', 'DELETE',
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

    def delete_shipping_template(self, id, **kwargs):
        """
        Delete a shipping template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_shipping_template(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :param str cascade: force deleting the template if it's attached to other objects, cascade = detach
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_shipping_template_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_shipping_template_with_http_info(id, **kwargs)
            return data

    def delete_shipping_template_with_http_info(self, id, **kwargs):
        """
        Delete a shipping template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_shipping_template_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :param str cascade: force deleting the template if it's attached to other objects, cascade = detach
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
                    " to method delete_shipping_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_shipping_template`")


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
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/store/shipping/templates/{id}', 'DELETE',
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

    def get_shipping_item(self, id, **kwargs):
        """
        Get a single shipping item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_shipping_item(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the shipping item (required)
        :return: ShippingItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_shipping_item_with_http_info(id, **kwargs)
        else:
            (data) = self.get_shipping_item_with_http_info(id, **kwargs)
            return data

    def get_shipping_item_with_http_info(self, id, **kwargs):
        """
        Get a single shipping item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_shipping_item_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the shipping item (required)
        :return: ShippingItem
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
                    " to method get_shipping_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_shipping_item`")


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

        return self.api_client.call_api('/store/shipping/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ShippingItem',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_shipping_template(self, id, **kwargs):
        """
        Get a single shipping template
        Shipping Templates define a type of shipping and the properties they have.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_shipping_template(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :return: ItemTemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_shipping_template_with_http_info(id, **kwargs)
        else:
            (data) = self.get_shipping_template_with_http_info(id, **kwargs)
            return data

    def get_shipping_template_with_http_info(self, id, **kwargs):
        """
        Get a single shipping template
        Shipping Templates define a type of shipping and the properties they have.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_shipping_template_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :return: ItemTemplateResource
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
                    " to method get_shipping_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_shipping_template`")


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

        return self.api_client.call_api('/store/shipping/templates/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ItemTemplateResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_shipping_templates(self, **kwargs):
        """
        List and search shipping templates
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_shipping_templates(async=True)
        >>> result = thread.get()

        :param async bool
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceItemTemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_shipping_templates_with_http_info(**kwargs)
        else:
            (data) = self.get_shipping_templates_with_http_info(**kwargs)
            return data

    def get_shipping_templates_with_http_info(self, **kwargs):
        """
        List and search shipping templates
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_shipping_templates_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int size: The number of objects returned per page
        :param int page: The number of the page returned, starting with 1
        :param str order: A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC]
        :return: PageResourceItemTemplateResource
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
                    " to method get_shipping_templates" % key
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
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/store/shipping/templates', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PageResourceItemTemplateResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_shipping_item(self, id, **kwargs):
        """
        Update a shipping item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_shipping_item(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the shipping item (required)
        :param bool cascade: Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values.
        :param ShippingItem shipping_item: The shipping item object
        :return: ShippingItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_shipping_item_with_http_info(id, **kwargs)
        else:
            (data) = self.update_shipping_item_with_http_info(id, **kwargs)
            return data

    def update_shipping_item_with_http_info(self, id, **kwargs):
        """
        Update a shipping item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_shipping_item_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the shipping item (required)
        :param bool cascade: Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values.
        :param ShippingItem shipping_item: The shipping item object
        :return: ShippingItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cascade', 'shipping_item']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_shipping_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_shipping_item`")


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
        if 'shipping_item' in params:
            body_params = params['shipping_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/store/shipping/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ShippingItem',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_shipping_template(self, id, **kwargs):
        """
        Update a shipping template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_shipping_template(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :param ItemTemplateResource shipping_template_resource: The shipping template resource object
        :return: ItemTemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_shipping_template_with_http_info(id, **kwargs)
        else:
            (data) = self.update_shipping_template_with_http_info(id, **kwargs)
            return data

    def update_shipping_template_with_http_info(self, id, **kwargs):
        """
        Update a shipping template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_shipping_template_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :param ItemTemplateResource shipping_template_resource: The shipping template resource object
        :return: ItemTemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'shipping_template_resource']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_shipping_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_shipping_template`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'shipping_template_resource' in params:
            body_params = params['shipping_template_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/store/shipping/templates/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ItemTemplateResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
