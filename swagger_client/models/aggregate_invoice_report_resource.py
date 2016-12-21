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


class AggregateInvoiceReportResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, count=None, date=None, revenue=None, user_count=None):
        """
        AggregateInvoiceReportResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'count': 'int',
            'date': 'str',
            'revenue': 'float',
            'user_count': 'int'
        }

        self.attribute_map = {
            'count': 'count',
            'date': 'date',
            'revenue': 'revenue',
            'user_count': 'user_count'
        }

        self._count = count
        self._date = date
        self._revenue = revenue
        self._user_count = user_count

    @property
    def count(self):
        """
        Gets the count of this AggregateInvoiceReportResource.

        :return: The count of this AggregateInvoiceReportResource.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this AggregateInvoiceReportResource.

        :param count: The count of this AggregateInvoiceReportResource.
        :type: int
        """

        self._count = count

    @property
    def date(self):
        """
        Gets the date of this AggregateInvoiceReportResource.

        :return: The date of this AggregateInvoiceReportResource.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this AggregateInvoiceReportResource.

        :param date: The date of this AggregateInvoiceReportResource.
        :type: str
        """

        self._date = date

    @property
    def revenue(self):
        """
        Gets the revenue of this AggregateInvoiceReportResource.

        :return: The revenue of this AggregateInvoiceReportResource.
        :rtype: float
        """
        return self._revenue

    @revenue.setter
    def revenue(self, revenue):
        """
        Sets the revenue of this AggregateInvoiceReportResource.

        :param revenue: The revenue of this AggregateInvoiceReportResource.
        :type: float
        """

        self._revenue = revenue

    @property
    def user_count(self):
        """
        Gets the user_count of this AggregateInvoiceReportResource.

        :return: The user_count of this AggregateInvoiceReportResource.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """
        Sets the user_count of this AggregateInvoiceReportResource.

        :param user_count: The user_count of this AggregateInvoiceReportResource.
        :type: int
        """

        self._user_count = user_count

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