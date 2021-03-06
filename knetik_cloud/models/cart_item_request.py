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


class CartItemRequest(object):
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
        'affiliate_key': 'str',
        'catalog_sku': 'str',
        'price_override': 'float',
        'quantity': 'int'
    }

    attribute_map = {
        'affiliate_key': 'affiliate_key',
        'catalog_sku': 'catalog_sku',
        'price_override': 'price_override',
        'quantity': 'quantity'
    }

    def __init__(self, affiliate_key=None, catalog_sku=None, price_override=None, quantity=None):
        """
        CartItemRequest - a model defined in Swagger
        """

        self._affiliate_key = None
        self._catalog_sku = None
        self._price_override = None
        self._quantity = None
        self.discriminator = None

        if affiliate_key is not None:
          self.affiliate_key = affiliate_key
        self.catalog_sku = catalog_sku
        self.price_override = price_override
        self.quantity = quantity

    @property
    def affiliate_key(self):
        """
        Gets the affiliate_key of this CartItemRequest.
        The affiliate key of the item

        :return: The affiliate_key of this CartItemRequest.
        :rtype: str
        """
        return self._affiliate_key

    @affiliate_key.setter
    def affiliate_key(self, affiliate_key):
        """
        Sets the affiliate_key of this CartItemRequest.
        The affiliate key of the item

        :param affiliate_key: The affiliate_key of this CartItemRequest.
        :type: str
        """

        self._affiliate_key = affiliate_key

    @property
    def catalog_sku(self):
        """
        Gets the catalog_sku of this CartItemRequest.
        The catalog SKU of the item

        :return: The catalog_sku of this CartItemRequest.
        :rtype: str
        """
        return self._catalog_sku

    @catalog_sku.setter
    def catalog_sku(self, catalog_sku):
        """
        Sets the catalog_sku of this CartItemRequest.
        The catalog SKU of the item

        :param catalog_sku: The catalog_sku of this CartItemRequest.
        :type: str
        """
        if catalog_sku is None:
            raise ValueError("Invalid value for `catalog_sku`, must not be `None`")

        self._catalog_sku = catalog_sku

    @property
    def price_override(self):
        """
        Gets the price_override of this CartItemRequest.
        Allows to override the price of an item, if the behavior configuration permits it

        :return: The price_override of this CartItemRequest.
        :rtype: float
        """
        return self._price_override

    @price_override.setter
    def price_override(self, price_override):
        """
        Sets the price_override of this CartItemRequest.
        Allows to override the price of an item, if the behavior configuration permits it

        :param price_override: The price_override of this CartItemRequest.
        :type: float
        """
        if price_override is None:
            raise ValueError("Invalid value for `price_override`, must not be `None`")

        self._price_override = price_override

    @property
    def quantity(self):
        """
        Gets the quantity of this CartItemRequest.
        The quantity of the item

        :return: The quantity of this CartItemRequest.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this CartItemRequest.
        The quantity of the item

        :param quantity: The quantity of this CartItemRequest.
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity

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
        if not isinstance(other, CartItemRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
