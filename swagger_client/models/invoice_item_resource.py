# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InvoiceItemResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, affiliate_id=None, bundle_sku=None, current_fulfillment_status=None, id=None, invoice_id=None, item_id=None, item_name=None, original_total_price=None, original_unit_price=None, qty=None, sale_name=None, sku=None, sku_description=None, system_price=None, total_price=None, type_hint=None, unit_price=None):
        """
        InvoiceItemResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'affiliate_id': 'int',
            'bundle_sku': 'str',
            'current_fulfillment_status': 'str',
            'id': 'int',
            'invoice_id': 'int',
            'item_id': 'int',
            'item_name': 'str',
            'original_total_price': 'float',
            'original_unit_price': 'float',
            'qty': 'int',
            'sale_name': 'str',
            'sku': 'str',
            'sku_description': 'str',
            'system_price': 'float',
            'total_price': 'float',
            'type_hint': 'str',
            'unit_price': 'float'
        }

        self.attribute_map = {
            'affiliate_id': 'affiliate_id',
            'bundle_sku': 'bundle_sku',
            'current_fulfillment_status': 'current_fulfillment_status',
            'id': 'id',
            'invoice_id': 'invoice_id',
            'item_id': 'item_id',
            'item_name': 'item_name',
            'original_total_price': 'original_total_price',
            'original_unit_price': 'original_unit_price',
            'qty': 'qty',
            'sale_name': 'sale_name',
            'sku': 'sku',
            'sku_description': 'sku_description',
            'system_price': 'system_price',
            'total_price': 'total_price',
            'type_hint': 'type_hint',
            'unit_price': 'unit_price'
        }

        self._affiliate_id = affiliate_id
        self._bundle_sku = bundle_sku
        self._current_fulfillment_status = current_fulfillment_status
        self._id = id
        self._invoice_id = invoice_id
        self._item_id = item_id
        self._item_name = item_name
        self._original_total_price = original_total_price
        self._original_unit_price = original_unit_price
        self._qty = qty
        self._sale_name = sale_name
        self._sku = sku
        self._sku_description = sku_description
        self._system_price = system_price
        self._total_price = total_price
        self._type_hint = type_hint
        self._unit_price = unit_price

    @property
    def affiliate_id(self):
        """
        Gets the affiliate_id of this InvoiceItemResource.

        :return: The affiliate_id of this InvoiceItemResource.
        :rtype: int
        """
        return self._affiliate_id

    @affiliate_id.setter
    def affiliate_id(self, affiliate_id):
        """
        Sets the affiliate_id of this InvoiceItemResource.

        :param affiliate_id: The affiliate_id of this InvoiceItemResource.
        :type: int
        """

        self._affiliate_id = affiliate_id

    @property
    def bundle_sku(self):
        """
        Gets the bundle_sku of this InvoiceItemResource.

        :return: The bundle_sku of this InvoiceItemResource.
        :rtype: str
        """
        return self._bundle_sku

    @bundle_sku.setter
    def bundle_sku(self, bundle_sku):
        """
        Sets the bundle_sku of this InvoiceItemResource.

        :param bundle_sku: The bundle_sku of this InvoiceItemResource.
        :type: str
        """

        self._bundle_sku = bundle_sku

    @property
    def current_fulfillment_status(self):
        """
        Gets the current_fulfillment_status of this InvoiceItemResource.

        :return: The current_fulfillment_status of this InvoiceItemResource.
        :rtype: str
        """
        return self._current_fulfillment_status

    @current_fulfillment_status.setter
    def current_fulfillment_status(self, current_fulfillment_status):
        """
        Sets the current_fulfillment_status of this InvoiceItemResource.

        :param current_fulfillment_status: The current_fulfillment_status of this InvoiceItemResource.
        :type: str
        """

        self._current_fulfillment_status = current_fulfillment_status

    @property
    def id(self):
        """
        Gets the id of this InvoiceItemResource.

        :return: The id of this InvoiceItemResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InvoiceItemResource.

        :param id: The id of this InvoiceItemResource.
        :type: int
        """

        self._id = id

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this InvoiceItemResource.

        :return: The invoice_id of this InvoiceItemResource.
        :rtype: int
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this InvoiceItemResource.

        :param invoice_id: The invoice_id of this InvoiceItemResource.
        :type: int
        """

        self._invoice_id = invoice_id

    @property
    def item_id(self):
        """
        Gets the item_id of this InvoiceItemResource.

        :return: The item_id of this InvoiceItemResource.
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        Sets the item_id of this InvoiceItemResource.

        :param item_id: The item_id of this InvoiceItemResource.
        :type: int
        """

        self._item_id = item_id

    @property
    def item_name(self):
        """
        Gets the item_name of this InvoiceItemResource.

        :return: The item_name of this InvoiceItemResource.
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        """
        Sets the item_name of this InvoiceItemResource.

        :param item_name: The item_name of this InvoiceItemResource.
        :type: str
        """

        self._item_name = item_name

    @property
    def original_total_price(self):
        """
        Gets the original_total_price of this InvoiceItemResource.

        :return: The original_total_price of this InvoiceItemResource.
        :rtype: float
        """
        return self._original_total_price

    @original_total_price.setter
    def original_total_price(self, original_total_price):
        """
        Sets the original_total_price of this InvoiceItemResource.

        :param original_total_price: The original_total_price of this InvoiceItemResource.
        :type: float
        """

        self._original_total_price = original_total_price

    @property
    def original_unit_price(self):
        """
        Gets the original_unit_price of this InvoiceItemResource.

        :return: The original_unit_price of this InvoiceItemResource.
        :rtype: float
        """
        return self._original_unit_price

    @original_unit_price.setter
    def original_unit_price(self, original_unit_price):
        """
        Sets the original_unit_price of this InvoiceItemResource.

        :param original_unit_price: The original_unit_price of this InvoiceItemResource.
        :type: float
        """

        self._original_unit_price = original_unit_price

    @property
    def qty(self):
        """
        Gets the qty of this InvoiceItemResource.

        :return: The qty of this InvoiceItemResource.
        :rtype: int
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """
        Sets the qty of this InvoiceItemResource.

        :param qty: The qty of this InvoiceItemResource.
        :type: int
        """

        self._qty = qty

    @property
    def sale_name(self):
        """
        Gets the sale_name of this InvoiceItemResource.

        :return: The sale_name of this InvoiceItemResource.
        :rtype: str
        """
        return self._sale_name

    @sale_name.setter
    def sale_name(self, sale_name):
        """
        Sets the sale_name of this InvoiceItemResource.

        :param sale_name: The sale_name of this InvoiceItemResource.
        :type: str
        """

        self._sale_name = sale_name

    @property
    def sku(self):
        """
        Gets the sku of this InvoiceItemResource.

        :return: The sku of this InvoiceItemResource.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this InvoiceItemResource.

        :param sku: The sku of this InvoiceItemResource.
        :type: str
        """

        self._sku = sku

    @property
    def sku_description(self):
        """
        Gets the sku_description of this InvoiceItemResource.

        :return: The sku_description of this InvoiceItemResource.
        :rtype: str
        """
        return self._sku_description

    @sku_description.setter
    def sku_description(self, sku_description):
        """
        Sets the sku_description of this InvoiceItemResource.

        :param sku_description: The sku_description of this InvoiceItemResource.
        :type: str
        """

        self._sku_description = sku_description

    @property
    def system_price(self):
        """
        Gets the system_price of this InvoiceItemResource.

        :return: The system_price of this InvoiceItemResource.
        :rtype: float
        """
        return self._system_price

    @system_price.setter
    def system_price(self, system_price):
        """
        Sets the system_price of this InvoiceItemResource.

        :param system_price: The system_price of this InvoiceItemResource.
        :type: float
        """

        self._system_price = system_price

    @property
    def total_price(self):
        """
        Gets the total_price of this InvoiceItemResource.

        :return: The total_price of this InvoiceItemResource.
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """
        Sets the total_price of this InvoiceItemResource.

        :param total_price: The total_price of this InvoiceItemResource.
        :type: float
        """

        self._total_price = total_price

    @property
    def type_hint(self):
        """
        Gets the type_hint of this InvoiceItemResource.

        :return: The type_hint of this InvoiceItemResource.
        :rtype: str
        """
        return self._type_hint

    @type_hint.setter
    def type_hint(self, type_hint):
        """
        Sets the type_hint of this InvoiceItemResource.

        :param type_hint: The type_hint of this InvoiceItemResource.
        :type: str
        """

        self._type_hint = type_hint

    @property
    def unit_price(self):
        """
        Gets the unit_price of this InvoiceItemResource.

        :return: The unit_price of this InvoiceItemResource.
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """
        Sets the unit_price of this InvoiceItemResource.

        :param unit_price: The unit_price of this InvoiceItemResource.
        :type: float
        """

        self._unit_price = unit_price

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
