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


class StripePaymentRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, invoice_id=None, token=None):
        """
        StripePaymentRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'invoice_id': 'int',
            'token': 'str'
        }

        self.attribute_map = {
            'invoice_id': 'invoice_id',
            'token': 'token'
        }

        self._invoice_id = invoice_id
        self._token = token

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this StripePaymentRequest.
        The id of the invoice to pay

        :return: The invoice_id of this StripePaymentRequest.
        :rtype: int
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this StripePaymentRequest.
        The id of the invoice to pay

        :param invoice_id: The invoice_id of this StripePaymentRequest.
        :type: int
        """
        if invoice_id is None:
            raise ValueError("Invalid value for `invoice_id`, must not be `None`")

        self._invoice_id = invoice_id

    @property
    def token(self):
        """
        Gets the token of this StripePaymentRequest.
        A token from Stripe to identify payment info to be tied to the customer

        :return: The token of this StripePaymentRequest.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this StripePaymentRequest.
        A token from Stripe to identify payment info to be tied to the customer

        :param token: The token of this StripePaymentRequest.
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")

        self._token = token

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