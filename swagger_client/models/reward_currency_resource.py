# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RewardCurrencyResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, currency_code=None, currency_name=None, max_rank=None, min_rank=None, percent=None, value=None):
        """
        RewardCurrencyResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'currency_code': 'str',
            'currency_name': 'str',
            'max_rank': 'int',
            'min_rank': 'int',
            'percent': 'bool',
            'value': 'float'
        }

        self.attribute_map = {
            'currency_code': 'currency_code',
            'currency_name': 'currency_name',
            'max_rank': 'max_rank',
            'min_rank': 'min_rank',
            'percent': 'percent',
            'value': 'value'
        }

        self._currency_code = currency_code
        self._currency_name = currency_name
        self._max_rank = max_rank
        self._min_rank = min_rank
        self._percent = percent
        self._value = value

    @property
    def currency_code(self):
        """
        Gets the currency_code of this RewardCurrencyResource.
        The code of the currency type to give

        :return: The currency_code of this RewardCurrencyResource.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this RewardCurrencyResource.
        The code of the currency type to give

        :param currency_code: The currency_code of this RewardCurrencyResource.
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")

        self._currency_code = currency_code

    @property
    def currency_name(self):
        """
        Gets the currency_name of this RewardCurrencyResource.
        The name of the currency reward to give.  Set by currency_code)

        :return: The currency_name of this RewardCurrencyResource.
        :rtype: str
        """
        return self._currency_name

    @currency_name.setter
    def currency_name(self, currency_name):
        """
        Sets the currency_name of this RewardCurrencyResource.
        The name of the currency reward to give.  Set by currency_code)

        :param currency_name: The currency_name of this RewardCurrencyResource.
        :type: str
        """

        self._currency_name = currency_name

    @property
    def max_rank(self):
        """
        Gets the max_rank of this RewardCurrencyResource.
        The highest number (worst) rank to give the reward to. Must be greater than or equal to minRank

        :return: The max_rank of this RewardCurrencyResource.
        :rtype: int
        """
        return self._max_rank

    @max_rank.setter
    def max_rank(self, max_rank):
        """
        Sets the max_rank of this RewardCurrencyResource.
        The highest number (worst) rank to give the reward to. Must be greater than or equal to minRank

        :param max_rank: The max_rank of this RewardCurrencyResource.
        :type: int
        """
        if max_rank is None:
            raise ValueError("Invalid value for `max_rank`, must not be `None`")

        self._max_rank = max_rank

    @property
    def min_rank(self):
        """
        Gets the min_rank of this RewardCurrencyResource.
        The lowest number (best) rank to give the reward to. Must be greater than zero

        :return: The min_rank of this RewardCurrencyResource.
        :rtype: int
        """
        return self._min_rank

    @min_rank.setter
    def min_rank(self, min_rank):
        """
        Sets the min_rank of this RewardCurrencyResource.
        The lowest number (best) rank to give the reward to. Must be greater than zero

        :param min_rank: The min_rank of this RewardCurrencyResource.
        :type: int
        """
        if min_rank is None:
            raise ValueError("Invalid value for `min_rank`, must not be `None`")

        self._min_rank = min_rank

    @property
    def percent(self):
        """
        Gets the percent of this RewardCurrencyResource.
        True if the value is actually a percentage of the intake

        :return: The percent of this RewardCurrencyResource.
        :rtype: bool
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """
        Sets the percent of this RewardCurrencyResource.
        True if the value is actually a percentage of the intake

        :param percent: The percent of this RewardCurrencyResource.
        :type: bool
        """
        if percent is None:
            raise ValueError("Invalid value for `percent`, must not be `None`")

        self._percent = percent

    @property
    def value(self):
        """
        Gets the value of this RewardCurrencyResource.
        The amount of currency to give. For percentage values, 0.5 is 50%

        :return: The value of this RewardCurrencyResource.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this RewardCurrencyResource.
        The amount of currency to give. For percentage values, 0.5 is 50%

        :param value: The value of this RewardCurrencyResource.
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value

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
