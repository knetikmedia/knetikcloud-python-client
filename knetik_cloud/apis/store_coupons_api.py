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


class StoreCouponsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_coupon_item(self, **kwargs):
        """
        Create a coupon item
        SKUs have to be unique in the entire store.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_coupon_item(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool cascade: Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values.
        :param CouponItem coupon_item: The coupon item object
        :return: CouponItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_coupon_item_with_http_info(**kwargs)
        else:
            (data) = self.create_coupon_item_with_http_info(**kwargs)
            return data

    def create_coupon_item_with_http_info(self, **kwargs):
        """
        Create a coupon item
        SKUs have to be unique in the entire store.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_coupon_item_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool cascade: Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values.
        :param CouponItem coupon_item: The coupon item object
        :return: CouponItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cascade', 'coupon_item']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_coupon_item" % key
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
        if 'coupon_item' in params:
            body_params = params['coupon_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/store/coupons', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CouponItem',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_coupon_template(self, **kwargs):
        """
        Create a coupon template
        Coupon Templates define a type of coupon and the properties they have.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_coupon_template(async=True)
        >>> result = thread.get()

        :param async bool
        :param ItemTemplateResource coupon_template_resource: The new coupon template
        :return: ItemTemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_coupon_template_with_http_info(**kwargs)
        else:
            (data) = self.create_coupon_template_with_http_info(**kwargs)
            return data

    def create_coupon_template_with_http_info(self, **kwargs):
        """
        Create a coupon template
        Coupon Templates define a type of coupon and the properties they have.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_coupon_template_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param ItemTemplateResource coupon_template_resource: The new coupon template
        :return: ItemTemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['coupon_template_resource']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_coupon_template" % key
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
        if 'coupon_template_resource' in params:
            body_params = params['coupon_template_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/store/coupons/templates', 'POST',
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

    def delete_coupon_item(self, id, **kwargs):
        """
        Delete a coupon item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_coupon_item(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the coupon (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_coupon_item_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_coupon_item_with_http_info(id, **kwargs)
            return data

    def delete_coupon_item_with_http_info(self, id, **kwargs):
        """
        Delete a coupon item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_coupon_item_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the coupon (required)
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
                    " to method delete_coupon_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_coupon_item`")


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
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/store/coupons/{id}', 'DELETE',
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

    def delete_coupon_template(self, id, **kwargs):
        """
        Delete a coupon template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_coupon_template(id, async=True)
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
            return self.delete_coupon_template_with_http_info(id, **kwargs)
        else:
            (data) = self.delete_coupon_template_with_http_info(id, **kwargs)
            return data

    def delete_coupon_template_with_http_info(self, id, **kwargs):
        """
        Delete a coupon template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_coupon_template_with_http_info(id, async=True)
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
                    " to method delete_coupon_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_coupon_template`")


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
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/store/coupons/templates/{id}', 'DELETE',
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

    def get_coupon_item(self, id, **kwargs):
        """
        Get a single coupon item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_coupon_item(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the coupon (required)
        :return: CouponItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_coupon_item_with_http_info(id, **kwargs)
        else:
            (data) = self.get_coupon_item_with_http_info(id, **kwargs)
            return data

    def get_coupon_item_with_http_info(self, id, **kwargs):
        """
        Get a single coupon item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_coupon_item_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the coupon (required)
        :return: CouponItem
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
                    " to method get_coupon_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_coupon_item`")


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
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/store/coupons/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CouponItem',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_coupon_template(self, id, **kwargs):
        """
        Get a single coupon template
        Coupon Templates define a type of coupon and the properties they have.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_coupon_template(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :return: ItemTemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_coupon_template_with_http_info(id, **kwargs)
        else:
            (data) = self.get_coupon_template_with_http_info(id, **kwargs)
            return data

    def get_coupon_template_with_http_info(self, id, **kwargs):
        """
        Get a single coupon template
        Coupon Templates define a type of coupon and the properties they have.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_coupon_template_with_http_info(id, async=True)
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
                    " to method get_coupon_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_coupon_template`")


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
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/store/coupons/templates/{id}', 'GET',
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

    def get_coupon_templates(self, **kwargs):
        """
        List and search coupon templates
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_coupon_templates(async=True)
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
            return self.get_coupon_templates_with_http_info(**kwargs)
        else:
            (data) = self.get_coupon_templates_with_http_info(**kwargs)
            return data

    def get_coupon_templates_with_http_info(self, **kwargs):
        """
        List and search coupon templates
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_coupon_templates_with_http_info(async=True)
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
                    " to method get_coupon_templates" % key
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
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/store/coupons/templates', 'GET',
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

    def update_coupon_item(self, id, **kwargs):
        """
        Update a coupon item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_coupon_item(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the coupon (required)
        :param bool cascade: Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values.
        :param CouponItem coupon_item: The coupon item object
        :return: CouponItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_coupon_item_with_http_info(id, **kwargs)
        else:
            (data) = self.update_coupon_item_with_http_info(id, **kwargs)
            return data

    def update_coupon_item_with_http_info(self, id, **kwargs):
        """
        Update a coupon item
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_coupon_item_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The id of the coupon (required)
        :param bool cascade: Whether to cascade group changes, such as in the limited gettable behavior. A 400 error will return otherwise if the group is already in use with different values.
        :param CouponItem coupon_item: The coupon item object
        :return: CouponItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cascade', 'coupon_item']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_coupon_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_coupon_item`")


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
        if 'coupon_item' in params:
            body_params = params['coupon_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/store/coupons/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CouponItem',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_coupon_template(self, id, **kwargs):
        """
        Update a coupon template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_coupon_template(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :param ItemTemplateResource coupon_template_resource: The coupon template resource object
        :return: ItemTemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_coupon_template_with_http_info(id, **kwargs)
        else:
            (data) = self.update_coupon_template_with_http_info(id, **kwargs)
            return data

    def update_coupon_template_with_http_info(self, id, **kwargs):
        """
        Update a coupon template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_coupon_template_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str id: The id of the template (required)
        :param ItemTemplateResource coupon_template_resource: The coupon template resource object
        :return: ItemTemplateResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'coupon_template_resource']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_coupon_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_coupon_template`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'coupon_template_resource' in params:
            body_params = params['coupon_template_resource']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/store/coupons/templates/{id}', 'PUT',
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
