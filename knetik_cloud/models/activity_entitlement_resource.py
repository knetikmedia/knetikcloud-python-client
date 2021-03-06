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


class ActivityEntitlementResource(object):
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
        'item_id': 'int',
        'name': 'str',
        'price': 'float',
        'sku': 'str'
    }

    attribute_map = {
        'currency_code': 'currency_code',
        'item_id': 'item_id',
        'name': 'name',
        'price': 'price',
        'sku': 'sku'
    }

    def __init__(self, currency_code=None, item_id=None, name=None, price=None, sku=None):
        """
        ActivityEntitlementResource - a model defined in Swagger
        """

        self._currency_code = None
        self._item_id = None
        self._name = None
        self._price = None
        self._sku = None
        self.discriminator = None

        if currency_code is not None:
          self.currency_code = currency_code
        self.item_id = item_id
        if name is not None:
          self.name = name
        if price is not None:
          self.price = price
        if sku is not None:
          self.sku = sku

    @property
    def currency_code(self):
        """
        Gets the currency_code of this ActivityEntitlementResource.
        The ISO3 currency code the price is in, if available

        :return: The currency_code of this ActivityEntitlementResource.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this ActivityEntitlementResource.
        The ISO3 currency code the price is in, if available

        :param currency_code: The currency_code of this ActivityEntitlementResource.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def item_id(self):
        """
        Gets the item_id of this ActivityEntitlementResource.
        The id of the entitlement item

        :return: The item_id of this ActivityEntitlementResource.
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        Sets the item_id of this ActivityEntitlementResource.
        The id of the entitlement item

        :param item_id: The item_id of this ActivityEntitlementResource.
        :type: int
        """
        if item_id is None:
            raise ValueError("Invalid value for `item_id`, must not be `None`")

        self._item_id = item_id

    @property
    def name(self):
        """
        Gets the name of this ActivityEntitlementResource.
        The name of the entitlement item

        :return: The name of this ActivityEntitlementResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ActivityEntitlementResource.
        The name of the entitlement item

        :param name: The name of this ActivityEntitlementResource.
        :type: str
        """

        self._name = name

    @property
    def price(self):
        """
        Gets the price of this ActivityEntitlementResource.
        The price of the sku, if available

        :return: The price of this ActivityEntitlementResource.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this ActivityEntitlementResource.
        The price of the sku, if available

        :param price: The price of this ActivityEntitlementResource.
        :type: float
        """

        self._price = price

    @property
    def sku(self):
        """
        Gets the sku of this ActivityEntitlementResource.
        The sku id, if available. If multiple are available, then first one is returned

        :return: The sku of this ActivityEntitlementResource.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this ActivityEntitlementResource.
        The sku id, if available. If multiple are available, then first one is returned

        :param sku: The sku of this ActivityEntitlementResource.
        :type: str
        """

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
        if not isinstance(other, ActivityEntitlementResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
