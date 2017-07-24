# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com.

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WalletTotalResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'currency_code': 'str',
        'total': 'float'
    }

    attribute_map = {
        'currency_code': 'currency_code',
        'total': 'total'
    }

    def __init__(self, currency_code=None, total=None):
        """
        WalletTotalResponse - a model defined in Swagger
        """

        self._currency_code = None
        self._total = None

        if currency_code is not None:
          self.currency_code = currency_code
        if total is not None:
          self.total = total

    @property
    def currency_code(self):
        """
        Gets the currency_code of this WalletTotalResponse.
        The currency code

        :return: The currency_code of this WalletTotalResponse.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this WalletTotalResponse.
        The currency code

        :param currency_code: The currency_code of this WalletTotalResponse.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def total(self):
        """
        Gets the total of this WalletTotalResponse.
        The sum of all wallets in the system for this currency

        :return: The total of this WalletTotalResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this WalletTotalResponse.
        The sum of all wallets in the system for this currency

        :param total: The total of this WalletTotalResponse.
        :type: float
        """

        self._total = total

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
        if not isinstance(other, WalletTotalResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
