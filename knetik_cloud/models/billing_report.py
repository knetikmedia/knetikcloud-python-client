# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BillingReport(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, id=None, last_known_failures=None, statistics=None):
        """
        BillingReport - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'int',
            'id': 'str',
            'last_known_failures': 'list[str]',
            'statistics': 'dict(str, int)'
        }

        self.attribute_map = {
            'created': 'created',
            'id': 'id',
            'last_known_failures': 'last_known_failures',
            'statistics': 'statistics'
        }

        self._created = created
        self._id = id
        self._last_known_failures = last_known_failures
        self._statistics = statistics

    @property
    def created(self):
        """
        Gets the created of this BillingReport.

        :return: The created of this BillingReport.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this BillingReport.

        :param created: The created of this BillingReport.
        :type: int
        """

        self._created = created

    @property
    def id(self):
        """
        Gets the id of this BillingReport.

        :return: The id of this BillingReport.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BillingReport.

        :param id: The id of this BillingReport.
        :type: str
        """

        self._id = id

    @property
    def last_known_failures(self):
        """
        Gets the last_known_failures of this BillingReport.

        :return: The last_known_failures of this BillingReport.
        :rtype: list[str]
        """
        return self._last_known_failures

    @last_known_failures.setter
    def last_known_failures(self, last_known_failures):
        """
        Sets the last_known_failures of this BillingReport.

        :param last_known_failures: The last_known_failures of this BillingReport.
        :type: list[str]
        """

        self._last_known_failures = last_known_failures

    @property
    def statistics(self):
        """
        Gets the statistics of this BillingReport.

        :return: The statistics of this BillingReport.
        :rtype: dict(str, int)
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """
        Sets the statistics of this BillingReport.

        :param statistics: The statistics of this BillingReport.
        :type: dict(str, int)
        """

        self._statistics = statistics

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
        if not isinstance(other, BillingReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
