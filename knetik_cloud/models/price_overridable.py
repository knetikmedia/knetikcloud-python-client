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


class PriceOverridable(object):
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
        'max_price': 'float',
        'min_price': 'float'
    }

    attribute_map = {
        'max_price': 'max_price',
        'min_price': 'min_price'
    }

    def __init__(self, max_price=None, min_price=None):
        """
        PriceOverridable - a model defined in Swagger
        """

        self._max_price = None
        self._min_price = None
        self.discriminator = None

        if max_price is not None:
          self.max_price = max_price
        if min_price is not None:
          self.min_price = min_price

    @property
    def max_price(self):
        """
        Gets the max_price of this PriceOverridable.
        The maximum price allowed

        :return: The max_price of this PriceOverridable.
        :rtype: float
        """
        return self._max_price

    @max_price.setter
    def max_price(self, max_price):
        """
        Sets the max_price of this PriceOverridable.
        The maximum price allowed

        :param max_price: The max_price of this PriceOverridable.
        :type: float
        """

        self._max_price = max_price

    @property
    def min_price(self):
        """
        Gets the min_price of this PriceOverridable.
        The minimum price allowed

        :return: The min_price of this PriceOverridable.
        :rtype: float
        """
        return self._min_price

    @min_price.setter
    def min_price(self, min_price):
        """
        Sets the min_price of this PriceOverridable.
        The minimum price allowed

        :param min_price: The min_price of this PriceOverridable.
        :type: float
        """

        self._min_price = min_price

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
        if not isinstance(other, PriceOverridable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
