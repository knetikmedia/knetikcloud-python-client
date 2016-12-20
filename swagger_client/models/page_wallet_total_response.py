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


class PageWalletTotalResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, content=None, first=None, last=None, number=None, number_of_elements=None, size=None, sort=None, total_elements=None, total_pages=None):
        """
        PageWalletTotalResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content': 'list[WalletTotalResponse]',
            'first': 'bool',
            'last': 'bool',
            'number': 'int',
            'number_of_elements': 'int',
            'size': 'int',
            'sort': 'Sort',
            'total_elements': 'int',
            'total_pages': 'int'
        }

        self.attribute_map = {
            'content': 'content',
            'first': 'first',
            'last': 'last',
            'number': 'number',
            'number_of_elements': 'number_of_elements',
            'size': 'size',
            'sort': 'sort',
            'total_elements': 'total_elements',
            'total_pages': 'total_pages'
        }

        self._content = content
        self._first = first
        self._last = last
        self._number = number
        self._number_of_elements = number_of_elements
        self._size = size
        self._sort = sort
        self._total_elements = total_elements
        self._total_pages = total_pages

    @property
    def content(self):
        """
        Gets the content of this PageWalletTotalResponse.

        :return: The content of this PageWalletTotalResponse.
        :rtype: list[WalletTotalResponse]
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this PageWalletTotalResponse.

        :param content: The content of this PageWalletTotalResponse.
        :type: list[WalletTotalResponse]
        """

        self._content = content

    @property
    def first(self):
        """
        Gets the first of this PageWalletTotalResponse.

        :return: The first of this PageWalletTotalResponse.
        :rtype: bool
        """
        return self._first

    @first.setter
    def first(self, first):
        """
        Sets the first of this PageWalletTotalResponse.

        :param first: The first of this PageWalletTotalResponse.
        :type: bool
        """

        self._first = first

    @property
    def last(self):
        """
        Gets the last of this PageWalletTotalResponse.

        :return: The last of this PageWalletTotalResponse.
        :rtype: bool
        """
        return self._last

    @last.setter
    def last(self, last):
        """
        Sets the last of this PageWalletTotalResponse.

        :param last: The last of this PageWalletTotalResponse.
        :type: bool
        """

        self._last = last

    @property
    def number(self):
        """
        Gets the number of this PageWalletTotalResponse.

        :return: The number of this PageWalletTotalResponse.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this PageWalletTotalResponse.

        :param number: The number of this PageWalletTotalResponse.
        :type: int
        """

        self._number = number

    @property
    def number_of_elements(self):
        """
        Gets the number_of_elements of this PageWalletTotalResponse.

        :return: The number_of_elements of this PageWalletTotalResponse.
        :rtype: int
        """
        return self._number_of_elements

    @number_of_elements.setter
    def number_of_elements(self, number_of_elements):
        """
        Sets the number_of_elements of this PageWalletTotalResponse.

        :param number_of_elements: The number_of_elements of this PageWalletTotalResponse.
        :type: int
        """

        self._number_of_elements = number_of_elements

    @property
    def size(self):
        """
        Gets the size of this PageWalletTotalResponse.

        :return: The size of this PageWalletTotalResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this PageWalletTotalResponse.

        :param size: The size of this PageWalletTotalResponse.
        :type: int
        """

        self._size = size

    @property
    def sort(self):
        """
        Gets the sort of this PageWalletTotalResponse.

        :return: The sort of this PageWalletTotalResponse.
        :rtype: Sort
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this PageWalletTotalResponse.

        :param sort: The sort of this PageWalletTotalResponse.
        :type: Sort
        """

        self._sort = sort

    @property
    def total_elements(self):
        """
        Gets the total_elements of this PageWalletTotalResponse.

        :return: The total_elements of this PageWalletTotalResponse.
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """
        Sets the total_elements of this PageWalletTotalResponse.

        :param total_elements: The total_elements of this PageWalletTotalResponse.
        :type: int
        """

        self._total_elements = total_elements

    @property
    def total_pages(self):
        """
        Gets the total_pages of this PageWalletTotalResponse.

        :return: The total_pages of this PageWalletTotalResponse.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """
        Sets the total_pages of this PageWalletTotalResponse.

        :param total_pages: The total_pages of this PageWalletTotalResponse.
        :type: int
        """

        self._total_pages = total_pages

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
