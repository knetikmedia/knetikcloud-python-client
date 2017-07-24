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


class PayBySavedMethodRequest(object):
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
        'payment_method': 'int'
    }

    attribute_map = {
        'payment_method': 'payment_method'
    }

    def __init__(self, payment_method=None):
        """
        PayBySavedMethodRequest - a model defined in Swagger
        """

        self._payment_method = None

        self.payment_method = payment_method

    @property
    def payment_method(self):
        """
        Gets the payment_method of this PayBySavedMethodRequest.
        The id of the payment method to use. Must belong to the caller, be public or have PAYMENTS_ADMIN permission

        :return: The payment_method of this PayBySavedMethodRequest.
        :rtype: int
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """
        Sets the payment_method of this PayBySavedMethodRequest.
        The id of the payment method to use. Must belong to the caller, be public or have PAYMENTS_ADMIN permission

        :param payment_method: The payment_method of this PayBySavedMethodRequest.
        :type: int
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")

        self._payment_method = payment_method

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
        if not isinstance(other, PayBySavedMethodRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
