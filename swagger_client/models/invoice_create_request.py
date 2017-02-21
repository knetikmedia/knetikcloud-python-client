# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InvoiceCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cart_guid=None):
        """
        InvoiceCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cart_guid': 'str'
        }

        self.attribute_map = {
            'cart_guid': 'cart_guid'
        }

        self._cart_guid = cart_guid

    @property
    def cart_guid(self):
        """
        Gets the cart_guid of this InvoiceCreateRequest.
        The guid of a cart to create a new invoice for

        :return: The cart_guid of this InvoiceCreateRequest.
        :rtype: str
        """
        return self._cart_guid

    @cart_guid.setter
    def cart_guid(self, cart_guid):
        """
        Sets the cart_guid of this InvoiceCreateRequest.
        The guid of a cart to create a new invoice for

        :param cart_guid: The cart_guid of this InvoiceCreateRequest.
        :type: str
        """
        if cart_guid is None:
            raise ValueError("Invalid value for `cart_guid`, must not be `None`")

        self._cart_guid = cart_guid

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
        if not isinstance(other, InvoiceCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
