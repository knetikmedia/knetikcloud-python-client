# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StoreListRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ignore_location=None, in_stock_only=None, limit=None, page=None, use_catalog=None):
        """
        StoreListRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ignore_location': 'bool',
            'in_stock_only': 'bool',
            'limit': 'int',
            'page': 'int',
            'use_catalog': 'bool'
        }

        self.attribute_map = {
            'ignore_location': 'ignore_location',
            'in_stock_only': 'in_stock_only',
            'limit': 'limit',
            'page': 'page',
            'use_catalog': 'use_catalog'
        }

        self._ignore_location = ignore_location
        self._in_stock_only = in_stock_only
        self._limit = limit
        self._page = page
        self._use_catalog = use_catalog

    @property
    def ignore_location(self):
        """
        Gets the ignore_location of this StoreListRequest.
        Whether the location is ignored

        :return: The ignore_location of this StoreListRequest.
        :rtype: bool
        """
        return self._ignore_location

    @ignore_location.setter
    def ignore_location(self, ignore_location):
        """
        Sets the ignore_location of this StoreListRequest.
        Whether the location is ignored

        :param ignore_location: The ignore_location of this StoreListRequest.
        :type: bool
        """

        self._ignore_location = ignore_location

    @property
    def in_stock_only(self):
        """
        Gets the in_stock_only of this StoreListRequest.
        Whether the item is in stock

        :return: The in_stock_only of this StoreListRequest.
        :rtype: bool
        """
        return self._in_stock_only

    @in_stock_only.setter
    def in_stock_only(self, in_stock_only):
        """
        Sets the in_stock_only of this StoreListRequest.
        Whether the item is in stock

        :param in_stock_only: The in_stock_only of this StoreListRequest.
        :type: bool
        """

        self._in_stock_only = in_stock_only

    @property
    def limit(self):
        """
        Gets the limit of this StoreListRequest.
        The amount of items returned

        :return: The limit of this StoreListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this StoreListRequest.
        The amount of items returned

        :param limit: The limit of this StoreListRequest.
        :type: int
        """

        self._limit = limit

    @property
    def page(self):
        """
        Gets the page of this StoreListRequest.
        The page of the request

        :return: The page of this StoreListRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """
        Sets the page of this StoreListRequest.
        The page of the request

        :param page: The page of this StoreListRequest.
        :type: int
        """

        self._page = page

    @property
    def use_catalog(self):
        """
        Gets the use_catalog of this StoreListRequest.
        Whether the catalog is used

        :return: The use_catalog of this StoreListRequest.
        :rtype: bool
        """
        return self._use_catalog

    @use_catalog.setter
    def use_catalog(self, use_catalog):
        """
        Sets the use_catalog of this StoreListRequest.
        Whether the catalog is used

        :param use_catalog: The use_catalog of this StoreListRequest.
        :type: bool
        """

        self._use_catalog = use_catalog

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
