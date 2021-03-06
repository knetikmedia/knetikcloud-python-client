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


class LocationsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_countries(self, **kwargs):
        """
        Get a list of countries
        <b>Permissions Needed:</b> ANY
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_countries(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[CountryResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_countries_with_http_info(**kwargs)
        else:
            (data) = self.get_countries_with_http_info(**kwargs)
            return data

    def get_countries_with_http_info(self, **kwargs):
        """
        Get a list of countries
        <b>Permissions Needed:</b> ANY
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_countries_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[CountryResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_countries" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/location/countries', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[CountryResource]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_country_by_geo_location(self, **kwargs):
        """
        Get the iso3 code of your country
        Determined by geo ip location. <br><br><b>Permissions Needed:</b> ANY
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_country_by_geo_location(async=True)
        >>> result = thread.get()

        :param async bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_country_by_geo_location_with_http_info(**kwargs)
        else:
            (data) = self.get_country_by_geo_location_with_http_info(**kwargs)
            return data

    def get_country_by_geo_location_with_http_info(self, **kwargs):
        """
        Get the iso3 code of your country
        Determined by geo ip location. <br><br><b>Permissions Needed:</b> ANY
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_country_by_geo_location_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_country_by_geo_location" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/location/geolocation/country', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_country_states(self, country_code_iso3, **kwargs):
        """
        Get a list of a country's states
        <b>Permissions Needed:</b> ANY
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_country_states(country_code_iso3, async=True)
        >>> result = thread.get()

        :param async bool
        :param str country_code_iso3: The iso3 code of the country (required)
        :return: list[StateResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_country_states_with_http_info(country_code_iso3, **kwargs)
        else:
            (data) = self.get_country_states_with_http_info(country_code_iso3, **kwargs)
            return data

    def get_country_states_with_http_info(self, country_code_iso3, **kwargs):
        """
        Get a list of a country's states
        <b>Permissions Needed:</b> ANY
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_country_states_with_http_info(country_code_iso3, async=True)
        >>> result = thread.get()

        :param async bool
        :param str country_code_iso3: The iso3 code of the country (required)
        :return: list[StateResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code_iso3']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_country_states" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country_code_iso3' is set
        if ('country_code_iso3' not in params) or (params['country_code_iso3'] is None):
            raise ValueError("Missing the required parameter `country_code_iso3` when calling `get_country_states`")


        collection_formats = {}

        path_params = {}
        if 'country_code_iso3' in params:
            path_params['country_code_iso3'] = params['country_code_iso3']

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

        return self.api_client.call_api('/location/countries/{country_code_iso3}/states', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[StateResource]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_currency_by_geo_location(self, **kwargs):
        """
        Get the currency information of your country
        Determined by geo ip location, currency to country mapping and a fallback setting. <br><br><b>Permissions Needed:</b> ANY
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_currency_by_geo_location(async=True)
        >>> result = thread.get()

        :param async bool
        :return: CurrencyResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_currency_by_geo_location_with_http_info(**kwargs)
        else:
            (data) = self.get_currency_by_geo_location_with_http_info(**kwargs)
            return data

    def get_currency_by_geo_location_with_http_info(self, **kwargs):
        """
        Get the currency information of your country
        Determined by geo ip location, currency to country mapping and a fallback setting. <br><br><b>Permissions Needed:</b> ANY
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_currency_by_geo_location_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: CurrencyResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_currency_by_geo_location" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2_client_credentials_grant', 'oauth2_password_grant']

        return self.api_client.call_api('/location/geolocation/currency', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CurrencyResource',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
