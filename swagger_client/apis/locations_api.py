# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com

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


class LocationsApi(object):
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

    def get_cities(self, country_code_iso3, state_code, **kwargs):
        """
        Get a list of a state's cities
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_cities(country_code_iso3, state_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str country_code_iso3: The iso3 code of the country (required)
        :param str state_code: The code of the state (required)
        :return: list[CityResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_cities_with_http_info(country_code_iso3, state_code, **kwargs)
        else:
            (data) = self.get_cities_with_http_info(country_code_iso3, state_code, **kwargs)
            return data

    def get_cities_with_http_info(self, country_code_iso3, state_code, **kwargs):
        """
        Get a list of a state's cities
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_cities_with_http_info(country_code_iso3, state_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str country_code_iso3: The iso3 code of the country (required)
        :param str state_code: The code of the state (required)
        :return: list[CityResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code_iso3', 'state_code']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cities" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country_code_iso3' is set
        if ('country_code_iso3' not in params) or (params['country_code_iso3'] is None):
            raise ValueError("Missing the required parameter `country_code_iso3` when calling `get_cities`")
        # verify the required parameter 'state_code' is set
        if ('state_code' not in params) or (params['state_code'] is None):
            raise ValueError("Missing the required parameter `state_code` when calling `get_cities`")


        collection_formats = {}

        resource_path = '/location/countries/{country_code_iso3}/states/{state_code}/cities'.replace('{format}', 'json')
        path_params = {}
        if 'country_code_iso3' in params:
            path_params['country_code_iso3'] = params['country_code_iso3']
        if 'state_code' in params:
            path_params['state_code'] = params['state_code']

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
                                        response_type='list[CityResource]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_countries1(self, **kwargs):
        """
        Get a list of countries
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_countries1(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[CountryResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_countries1_with_http_info(**kwargs)
        else:
            (data) = self.get_countries1_with_http_info(**kwargs)
            return data

    def get_countries1_with_http_info(self, **kwargs):
        """
        Get a list of countries
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_countries1_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[CountryResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_countries1" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/location/countries'.replace('{format}', 'json')
        path_params = {}

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
                                        response_type='list[CountryResource]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_countries2(self, country_code_iso3, **kwargs):
        """
        Get a list of a country's states
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_countries2(country_code_iso3, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str country_code_iso3: The iso3 code of the country (required)
        :return: list[StateResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_countries2_with_http_info(country_code_iso3, **kwargs)
        else:
            (data) = self.get_countries2_with_http_info(country_code_iso3, **kwargs)
            return data

    def get_countries2_with_http_info(self, country_code_iso3, **kwargs):
        """
        Get a list of a country's states
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_countries2_with_http_info(country_code_iso3, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str country_code_iso3: The iso3 code of the country (required)
        :return: list[StateResource]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_code_iso3']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_countries2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'country_code_iso3' is set
        if ('country_code_iso3' not in params) or (params['country_code_iso3'] is None):
            raise ValueError("Missing the required parameter `country_code_iso3` when calling `get_countries2`")


        collection_formats = {}

        resource_path = '/location/countries/{country_code_iso3}/states'.replace('{format}', 'json')
        path_params = {}
        if 'country_code_iso3' in params:
            path_params['country_code_iso3'] = params['country_code_iso3']

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
                                        response_type='list[StateResource]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_country_by_geo_location(self, **kwargs):
        """
        Get the iso3 code of your country
        Determined by geo ip location
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_country_by_geo_location(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_country_by_geo_location_with_http_info(**kwargs)
        else:
            (data) = self.get_country_by_geo_location_with_http_info(**kwargs)
            return data

    def get_country_by_geo_location_with_http_info(self, **kwargs):
        """
        Get the iso3 code of your country
        Determined by geo ip location
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_country_by_geo_location_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
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

        resource_path = '/location/geolocation/country'.replace('{format}', 'json')
        path_params = {}

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
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_currency_by_geo_location(self, **kwargs):
        """
        Get the currency information of your country
        Determined by geo ip location, currency to country mapping and a fallback setting
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_currency_by_geo_location(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: CurrencyResource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_currency_by_geo_location_with_http_info(**kwargs)
        else:
            (data) = self.get_currency_by_geo_location_with_http_info(**kwargs)
            return data

    def get_currency_by_geo_location_with_http_info(self, **kwargs):
        """
        Get the currency information of your country
        Determined by geo ip location, currency to country mapping and a fallback setting
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_currency_by_geo_location_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: CurrencyResource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
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

        resource_path = '/location/geolocation/currency'.replace('{format}', 'json')
        path_params = {}

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
                                        response_type='CurrencyResource',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
