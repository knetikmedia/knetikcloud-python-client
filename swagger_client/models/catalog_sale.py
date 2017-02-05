# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CatalogSale(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, currency_code=None, discount_type=None, discount_value=None, id=None, item=None, long_description=None, name=None, sale_end_date=None, sale_start_date=None, short_description=None, tag=None, vendor=None):
        """
        CatalogSale - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'currency_code': 'str',
            'discount_type': 'str',
            'discount_value': 'float',
            'id': 'int',
            'item': 'int',
            'long_description': 'str',
            'name': 'str',
            'sale_end_date': 'int',
            'sale_start_date': 'int',
            'short_description': 'str',
            'tag': 'str',
            'vendor': 'int'
        }

        self.attribute_map = {
            'currency_code': 'currency_code',
            'discount_type': 'discount_type',
            'discount_value': 'discount_value',
            'id': 'id',
            'item': 'item',
            'long_description': 'long_description',
            'name': 'name',
            'sale_end_date': 'sale_end_date',
            'sale_start_date': 'sale_start_date',
            'short_description': 'short_description',
            'tag': 'tag',
            'vendor': 'vendor'
        }

        self._currency_code = currency_code
        self._discount_type = discount_type
        self._discount_value = discount_value
        self._id = id
        self._item = item
        self._long_description = long_description
        self._name = name
        self._sale_end_date = sale_end_date
        self._sale_start_date = sale_start_date
        self._short_description = short_description
        self._tag = tag
        self._vendor = vendor

    @property
    def currency_code(self):
        """
        Gets the currency_code of this CatalogSale.
        The iso3 code for the currency for this discountValue.  The sku purchased will have to match for it this sale to apply

        :return: The currency_code of this CatalogSale.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this CatalogSale.
        The iso3 code for the currency for this discountValue.  The sku purchased will have to match for it this sale to apply

        :param currency_code: The currency_code of this CatalogSale.
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")

        self._currency_code = currency_code

    @property
    def discount_type(self):
        """
        Gets the discount_type of this CatalogSale.
        The way in which the price is reduced. 'value' means subtracting directly, 'percentage' means subtracting by the price times the discountValue (1.0 == 100%)

        :return: The discount_type of this CatalogSale.
        :rtype: str
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """
        Sets the discount_type of this CatalogSale.
        The way in which the price is reduced. 'value' means subtracting directly, 'percentage' means subtracting by the price times the discountValue (1.0 == 100%)

        :param discount_type: The discount_type of this CatalogSale.
        :type: str
        """
        allowed_values = ["value", "percentage"]
        if discount_type not in allowed_values:
            raise ValueError(
                "Invalid value for `discount_type` ({0}), must be one of {1}"
                .format(discount_type, allowed_values)
            )

        self._discount_type = discount_type

    @property
    def discount_value(self):
        """
        Gets the discount_value of this CatalogSale.
        The amount deducted from the price, in the same currencyCode as the item

        :return: The discount_value of this CatalogSale.
        :rtype: float
        """
        return self._discount_value

    @discount_value.setter
    def discount_value(self, discount_value):
        """
        Sets the discount_value of this CatalogSale.
        The amount deducted from the price, in the same currencyCode as the item

        :param discount_value: The discount_value of this CatalogSale.
        :type: float
        """

        self._discount_value = discount_value

    @property
    def id(self):
        """
        Gets the id of this CatalogSale.
        The id of the sale

        :return: The id of this CatalogSale.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CatalogSale.
        The id of the sale

        :param id: The id of this CatalogSale.
        :type: int
        """

        self._id = id

    @property
    def item(self):
        """
        Gets the item of this CatalogSale.
        The id of the item this sale applies to.  Leave null to use other filters

        :return: The item of this CatalogSale.
        :rtype: int
        """
        return self._item

    @item.setter
    def item(self, item):
        """
        Sets the item of this CatalogSale.
        The id of the item this sale applies to.  Leave null to use other filters

        :param item: The item of this CatalogSale.
        :type: int
        """

        self._item = item

    @property
    def long_description(self):
        """
        Gets the long_description of this CatalogSale.
        The long description of the sale

        :return: The long_description of this CatalogSale.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this CatalogSale.
        The long description of the sale

        :param long_description: The long_description of this CatalogSale.
        :type: str
        """

        self._long_description = long_description

    @property
    def name(self):
        """
        Gets the name of this CatalogSale.
        The name of the sale.  Max 40 characters

        :return: The name of this CatalogSale.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CatalogSale.
        The name of the sale.  Max 40 characters

        :param name: The name of this CatalogSale.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def sale_end_date(self):
        """
        Gets the sale_end_date of this CatalogSale.
        The date the sale ends, null for never.  Unix timestamp in seconds

        :return: The sale_end_date of this CatalogSale.
        :rtype: int
        """
        return self._sale_end_date

    @sale_end_date.setter
    def sale_end_date(self, sale_end_date):
        """
        Sets the sale_end_date of this CatalogSale.
        The date the sale ends, null for never.  Unix timestamp in seconds

        :param sale_end_date: The sale_end_date of this CatalogSale.
        :type: int
        """

        self._sale_end_date = sale_end_date

    @property
    def sale_start_date(self):
        """
        Gets the sale_start_date of this CatalogSale.
        The date the sale begins.  Unix timestamp in seconds

        :return: The sale_start_date of this CatalogSale.
        :rtype: int
        """
        return self._sale_start_date

    @sale_start_date.setter
    def sale_start_date(self, sale_start_date):
        """
        Sets the sale_start_date of this CatalogSale.
        The date the sale begins.  Unix timestamp in seconds

        :param sale_start_date: The sale_start_date of this CatalogSale.
        :type: int
        """
        if sale_start_date is None:
            raise ValueError("Invalid value for `sale_start_date`, must not be `None`")

        self._sale_start_date = sale_start_date

    @property
    def short_description(self):
        """
        Gets the short_description of this CatalogSale.
        The short description of the sale.  Max 140 characters

        :return: The short_description of this CatalogSale.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this CatalogSale.
        The short description of the sale.  Max 140 characters

        :param short_description: The short_description of this CatalogSale.
        :type: str
        """

        self._short_description = short_description

    @property
    def tag(self):
        """
        Gets the tag of this CatalogSale.
        The tag this sale applies to.  Leave null to skip this filter (applies to all tags)

        :return: The tag of this CatalogSale.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this CatalogSale.
        The tag this sale applies to.  Leave null to skip this filter (applies to all tags)

        :param tag: The tag of this CatalogSale.
        :type: str
        """

        self._tag = tag

    @property
    def vendor(self):
        """
        Gets the vendor of this CatalogSale.
        The id of the vendor this sale applies to.  Leave null to skip this filter (applies to all vendors)

        :return: The vendor of this CatalogSale.
        :rtype: int
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this CatalogSale.
        The id of the vendor this sale applies to.  Leave null to skip this filter (applies to all vendors)

        :param vendor: The vendor of this CatalogSale.
        :type: int
        """

        self._vendor = vendor

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
        if not isinstance(other, CatalogSale):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
