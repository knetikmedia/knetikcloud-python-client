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


class CartShippingOption(object):
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
        'description': 'str',
        'name': 'str',
        'original_price': 'float',
        'price': 'float',
        'shipping_item_id': 'int',
        'sku': 'str',
        'taxable': 'bool',
        'vendor_id': 'int',
        'vendor_name': 'str'
    }

    attribute_map = {
        'currency_code': 'currency_code',
        'description': 'description',
        'name': 'name',
        'original_price': 'original_price',
        'price': 'price',
        'shipping_item_id': 'shipping_item_id',
        'sku': 'sku',
        'taxable': 'taxable',
        'vendor_id': 'vendor_id',
        'vendor_name': 'vendor_name'
    }

    def __init__(self, currency_code=None, description=None, name=None, original_price=None, price=None, shipping_item_id=None, sku=None, taxable=None, vendor_id=None, vendor_name=None):
        """
        CartShippingOption - a model defined in Swagger
        """

        self._currency_code = None
        self._description = None
        self._name = None
        self._original_price = None
        self._price = None
        self._shipping_item_id = None
        self._sku = None
        self._taxable = None
        self._vendor_id = None
        self._vendor_name = None
        self.discriminator = None

        if currency_code is not None:
          self.currency_code = currency_code
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if original_price is not None:
          self.original_price = original_price
        if price is not None:
          self.price = price
        if shipping_item_id is not None:
          self.shipping_item_id = shipping_item_id
        if sku is not None:
          self.sku = sku
        if taxable is not None:
          self.taxable = taxable
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if vendor_name is not None:
          self.vendor_name = vendor_name

    @property
    def currency_code(self):
        """
        Gets the currency_code of this CartShippingOption.

        :return: The currency_code of this CartShippingOption.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this CartShippingOption.

        :param currency_code: The currency_code of this CartShippingOption.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def description(self):
        """
        Gets the description of this CartShippingOption.

        :return: The description of this CartShippingOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CartShippingOption.

        :param description: The description of this CartShippingOption.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this CartShippingOption.

        :return: The name of this CartShippingOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CartShippingOption.

        :param name: The name of this CartShippingOption.
        :type: str
        """

        self._name = name

    @property
    def original_price(self):
        """
        Gets the original_price of this CartShippingOption.

        :return: The original_price of this CartShippingOption.
        :rtype: float
        """
        return self._original_price

    @original_price.setter
    def original_price(self, original_price):
        """
        Sets the original_price of this CartShippingOption.

        :param original_price: The original_price of this CartShippingOption.
        :type: float
        """

        self._original_price = original_price

    @property
    def price(self):
        """
        Gets the price of this CartShippingOption.

        :return: The price of this CartShippingOption.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this CartShippingOption.

        :param price: The price of this CartShippingOption.
        :type: float
        """

        self._price = price

    @property
    def shipping_item_id(self):
        """
        Gets the shipping_item_id of this CartShippingOption.

        :return: The shipping_item_id of this CartShippingOption.
        :rtype: int
        """
        return self._shipping_item_id

    @shipping_item_id.setter
    def shipping_item_id(self, shipping_item_id):
        """
        Sets the shipping_item_id of this CartShippingOption.

        :param shipping_item_id: The shipping_item_id of this CartShippingOption.
        :type: int
        """

        self._shipping_item_id = shipping_item_id

    @property
    def sku(self):
        """
        Gets the sku of this CartShippingOption.

        :return: The sku of this CartShippingOption.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this CartShippingOption.

        :param sku: The sku of this CartShippingOption.
        :type: str
        """

        self._sku = sku

    @property
    def taxable(self):
        """
        Gets the taxable of this CartShippingOption.

        :return: The taxable of this CartShippingOption.
        :rtype: bool
        """
        return self._taxable

    @taxable.setter
    def taxable(self, taxable):
        """
        Sets the taxable of this CartShippingOption.

        :param taxable: The taxable of this CartShippingOption.
        :type: bool
        """

        self._taxable = taxable

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this CartShippingOption.

        :return: The vendor_id of this CartShippingOption.
        :rtype: int
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this CartShippingOption.

        :param vendor_id: The vendor_id of this CartShippingOption.
        :type: int
        """

        self._vendor_id = vendor_id

    @property
    def vendor_name(self):
        """
        Gets the vendor_name of this CartShippingOption.

        :return: The vendor_name of this CartShippingOption.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """
        Sets the vendor_name of this CartShippingOption.

        :param vendor_name: The vendor_name of this CartShippingOption.
        :type: str
        """

        self._vendor_name = vendor_name

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
        if not isinstance(other, CartShippingOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
