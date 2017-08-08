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


class BundledSku(object):
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
        'price_override': 'float',
        'quantity': 'int',
        'sku': 'str'
    }

    attribute_map = {
        'price_override': 'price_override',
        'quantity': 'quantity',
        'sku': 'sku'
    }

    def __init__(self, price_override=None, quantity=None, sku=None):
        """
        BundledSku - a model defined in Swagger
        """

        self._price_override = None
        self._quantity = None
        self._sku = None
        self.discriminator = None

        if price_override is not None:
          self.price_override = price_override
        self.quantity = quantity
        self.sku = sku

    @property
    def price_override(self):
        """
        Gets the price_override of this BundledSku.
        The amount this item will cost inside the bundle instead of its regular price

        :return: The price_override of this BundledSku.
        :rtype: float
        """
        return self._price_override

    @price_override.setter
    def price_override(self, price_override):
        """
        Sets the price_override of this BundledSku.
        The amount this item will cost inside the bundle instead of its regular price

        :param price_override: The price_override of this BundledSku.
        :type: float
        """

        self._price_override = price_override

    @property
    def quantity(self):
        """
        Gets the quantity of this BundledSku.
        The quantity of this item within the bundle

        :return: The quantity of this BundledSku.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this BundledSku.
        The quantity of this item within the bundle

        :param quantity: The quantity of this BundledSku.
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity

    @property
    def sku(self):
        """
        Gets the sku of this BundledSku.
        The stock keeping unit (SKU) for an item included in the bundle

        :return: The sku of this BundledSku.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this BundledSku.
        The stock keeping unit (SKU) for an item included in the bundle

        :param sku: The sku of this BundledSku.
        :type: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")

        self._sku = sku

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
        if not isinstance(other, BundledSku):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
