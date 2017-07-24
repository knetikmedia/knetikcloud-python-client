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


class Sku(object):
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
        'additional_properties': 'dict(str, ModelProperty)',
        'currency_code': 'str',
        'description': 'str',
        'inventory': 'int',
        'min_inventory_threshold': 'int',
        'original_price': 'float',
        'price': 'float',
        'published': 'bool',
        'sale_id': 'int',
        'sale_name': 'str',
        'sku': 'str',
        'start_date': 'int',
        'stop_date': 'int'
    }

    attribute_map = {
        'additional_properties': 'additional_properties',
        'currency_code': 'currency_code',
        'description': 'description',
        'inventory': 'inventory',
        'min_inventory_threshold': 'min_inventory_threshold',
        'original_price': 'original_price',
        'price': 'price',
        'published': 'published',
        'sale_id': 'sale_id',
        'sale_name': 'sale_name',
        'sku': 'sku',
        'start_date': 'start_date',
        'stop_date': 'stop_date'
    }

    def __init__(self, additional_properties=None, currency_code=None, description=None, inventory=None, min_inventory_threshold=None, original_price=None, price=None, published=None, sale_id=None, sale_name=None, sku=None, start_date=None, stop_date=None):
        """
        Sku - a model defined in Swagger
        """

        self._additional_properties = None
        self._currency_code = None
        self._description = None
        self._inventory = None
        self._min_inventory_threshold = None
        self._original_price = None
        self._price = None
        self._published = None
        self._sale_id = None
        self._sale_name = None
        self._sku = None
        self._start_date = None
        self._stop_date = None

        if additional_properties is not None:
          self.additional_properties = additional_properties
        self.currency_code = currency_code
        self.description = description
        if inventory is not None:
          self.inventory = inventory
        if min_inventory_threshold is not None:
          self.min_inventory_threshold = min_inventory_threshold
        self.original_price = original_price
        if price is not None:
          self.price = price
        if published is not None:
          self.published = published
        if sale_id is not None:
          self.sale_id = sale_id
        if sale_name is not None:
          self.sale_name = sale_name
        self.sku = sku
        if start_date is not None:
          self.start_date = start_date
        if stop_date is not None:
          self.stop_date = stop_date

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this Sku.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type, or be an extra not from the template

        :return: The additional_properties of this Sku.
        :rtype: dict(str, ModelProperty)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this Sku.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type, or be an extra not from the template

        :param additional_properties: The additional_properties of this Sku.
        :type: dict(str, ModelProperty)
        """

        self._additional_properties = additional_properties

    @property
    def currency_code(self):
        """
        Gets the currency_code of this Sku.
        The currency code for the SKU, a three letter string (ISO3)

        :return: The currency_code of this Sku.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this Sku.
        The currency code for the SKU, a three letter string (ISO3)

        :param currency_code: The currency_code of this Sku.
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")

        self._currency_code = currency_code

    @property
    def description(self):
        """
        Gets the description of this Sku.
        The friendly name of the SKU as it will appear on invoices and reports. Typically represents the option name like red, large, etc

        :return: The description of this Sku.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Sku.
        The friendly name of the SKU as it will appear on invoices and reports. Typically represents the option name like red, large, etc

        :param description: The description of this Sku.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def inventory(self):
        """
        Gets the inventory of this Sku.
        The number of SKUs currently in stock

        :return: The inventory of this Sku.
        :rtype: int
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """
        Sets the inventory of this Sku.
        The number of SKUs currently in stock

        :param inventory: The inventory of this Sku.
        :type: int
        """

        self._inventory = inventory

    @property
    def min_inventory_threshold(self):
        """
        Gets the min_inventory_threshold of this Sku.
        Alerts vendor when SKU inventory drops below this value

        :return: The min_inventory_threshold of this Sku.
        :rtype: int
        """
        return self._min_inventory_threshold

    @min_inventory_threshold.setter
    def min_inventory_threshold(self, min_inventory_threshold):
        """
        Sets the min_inventory_threshold of this Sku.
        Alerts vendor when SKU inventory drops below this value

        :param min_inventory_threshold: The min_inventory_threshold of this Sku.
        :type: int
        """

        self._min_inventory_threshold = min_inventory_threshold

    @property
    def original_price(self):
        """
        Gets the original_price of this Sku.
        The base price before any sale

        :return: The original_price of this Sku.
        :rtype: float
        """
        return self._original_price

    @original_price.setter
    def original_price(self, original_price):
        """
        Sets the original_price of this Sku.
        The base price before any sale

        :param original_price: The original_price of this Sku.
        :type: float
        """
        if original_price is None:
            raise ValueError("Invalid value for `original_price`, must not be `None`")

        self._original_price = original_price

    @property
    def price(self):
        """
        Gets the price of this Sku.
        The current price of the SKU with sales, if any. Set original_price for the base

        :return: The price of this Sku.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this Sku.
        The current price of the SKU with sales, if any. Set original_price for the base

        :param price: The price of this Sku.
        :type: float
        """

        self._price = price

    @property
    def published(self):
        """
        Gets the published of this Sku.
        Whether or not the SKU is currently published

        :return: The published of this Sku.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """
        Sets the published of this Sku.
        Whether or not the SKU is currently published

        :param published: The published of this Sku.
        :type: bool
        """

        self._published = published

    @property
    def sale_id(self):
        """
        Gets the sale_id of this Sku.
        The id of a sale affecting the price, if any

        :return: The sale_id of this Sku.
        :rtype: int
        """
        return self._sale_id

    @sale_id.setter
    def sale_id(self, sale_id):
        """
        Sets the sale_id of this Sku.
        The id of a sale affecting the price, if any

        :param sale_id: The sale_id of this Sku.
        :type: int
        """

        self._sale_id = sale_id

    @property
    def sale_name(self):
        """
        Gets the sale_name of this Sku.
        The name of a sale affecting the price, if any

        :return: The sale_name of this Sku.
        :rtype: str
        """
        return self._sale_name

    @sale_name.setter
    def sale_name(self, sale_name):
        """
        Sets the sale_name of this Sku.
        The name of a sale affecting the price, if any

        :param sale_name: The sale_name of this Sku.
        :type: str
        """

        self._sale_name = sale_name

    @property
    def sku(self):
        """
        Gets the sku of this Sku.
        The stock keeping unit (SKU), a unique identifier for a given product.  Max 40 characters

        :return: The sku of this Sku.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this Sku.
        The stock keeping unit (SKU), a unique identifier for a given product.  Max 40 characters

        :param sku: The sku of this Sku.
        :type: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")

        self._sku = sku

    @property
    def start_date(self):
        """
        Gets the start_date of this Sku.
        The date the sku becomes available, unix timestamp in seconds.  If set to null, sku will become available immediately

        :return: The start_date of this Sku.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this Sku.
        The date the sku becomes available, unix timestamp in seconds.  If set to null, sku will become available immediately

        :param start_date: The start_date of this Sku.
        :type: int
        """

        self._start_date = start_date

    @property
    def stop_date(self):
        """
        Gets the stop_date of this Sku.
        The date the sku becomes unavailable, unix timestamp in seconds.  If set to null, sku is always available

        :return: The stop_date of this Sku.
        :rtype: int
        """
        return self._stop_date

    @stop_date.setter
    def stop_date(self, stop_date):
        """
        Sets the stop_date of this Sku.
        The date the sku becomes unavailable, unix timestamp in seconds.  If set to null, sku is always available

        :param stop_date: The stop_date of this Sku.
        :type: int
        """

        self._stop_date = stop_date

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
        if not isinstance(other, Sku):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other