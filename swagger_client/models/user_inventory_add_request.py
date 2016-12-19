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


class UserInventoryAddRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, note=None, overrides=None, skip_invoice=None, sku=None):
        """
        UserInventoryAddRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'note': 'str',
            'overrides': 'list[str]',
            'skip_invoice': 'bool',
            'sku': 'str'
        }

        self.attribute_map = {
            'note': 'note',
            'overrides': 'overrides',
            'skip_invoice': 'skip_invoice',
            'sku': 'sku'
        }

        self._note = note
        self._overrides = overrides
        self._skip_invoice = skip_invoice
        self._sku = sku

    @property
    def note(self):
        """
        Gets the note of this UserInventoryAddRequest.
        A note to be passed to the invoice or transaction

        :return: The note of this UserInventoryAddRequest.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this UserInventoryAddRequest.
        A note to be passed to the invoice or transaction

        :param note: The note of this UserInventoryAddRequest.
        :type: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")

        self._note = note

    @property
    def overrides(self):
        """
        Gets the overrides of this UserInventoryAddRequest.
        A list of behaviors to ignore explicitely.  Ex: 'limited_gettable'

        :return: The overrides of this UserInventoryAddRequest.
        :rtype: list[str]
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """
        Sets the overrides of this UserInventoryAddRequest.
        A list of behaviors to ignore explicitely.  Ex: 'limited_gettable'

        :param overrides: The overrides of this UserInventoryAddRequest.
        :type: list[str]
        """

        self._overrides = overrides

    @property
    def skip_invoice(self):
        """
        Gets the skip_invoice of this UserInventoryAddRequest.
        If set to true will cause the endpoint to skip creation of cart and invoice to track the inventory change

        :return: The skip_invoice of this UserInventoryAddRequest.
        :rtype: bool
        """
        return self._skip_invoice

    @skip_invoice.setter
    def skip_invoice(self, skip_invoice):
        """
        Sets the skip_invoice of this UserInventoryAddRequest.
        If set to true will cause the endpoint to skip creation of cart and invoice to track the inventory change

        :param skip_invoice: The skip_invoice of this UserInventoryAddRequest.
        :type: bool
        """
        if skip_invoice is None:
            raise ValueError("Invalid value for `skip_invoice`, must not be `None`")

        self._skip_invoice = skip_invoice

    @property
    def sku(self):
        """
        Gets the sku of this UserInventoryAddRequest.
        The specific SKU of the item to be added to the inventory

        :return: The sku of this UserInventoryAddRequest.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this UserInventoryAddRequest.
        The specific SKU of the item to be added to the inventory

        :param sku: The sku of this UserInventoryAddRequest.
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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
