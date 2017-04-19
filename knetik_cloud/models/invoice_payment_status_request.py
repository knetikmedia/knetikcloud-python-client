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


class InvoicePaymentStatusRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, payment_method_id=None, status=None):
        """
        InvoicePaymentStatusRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'payment_method_id': 'int',
            'status': 'str'
        }

        self.attribute_map = {
            'payment_method_id': 'payment_method_id',
            'status': 'status'
        }

        self._payment_method_id = payment_method_id
        self._status = status

    @property
    def payment_method_id(self):
        """
        Gets the payment_method_id of this InvoicePaymentStatusRequest.
        If included, will set the payment method used on the invoice

        :return: The payment_method_id of this InvoicePaymentStatusRequest.
        :rtype: int
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """
        Sets the payment_method_id of this InvoicePaymentStatusRequest.
        If included, will set the payment method used on the invoice

        :param payment_method_id: The payment_method_id of this InvoicePaymentStatusRequest.
        :type: int
        """

        self._payment_method_id = payment_method_id

    @property
    def status(self):
        """
        Gets the status of this InvoicePaymentStatusRequest.
        The new status for the invoice. Additional options may be available based on configuration.  Allowable values: 'new', 'paid', 'hold', 'canceled', 'payment failed', 'partial refund', 'refund'

        :return: The status of this InvoicePaymentStatusRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InvoicePaymentStatusRequest.
        The new status for the invoice. Additional options may be available based on configuration.  Allowable values: 'new', 'paid', 'hold', 'canceled', 'payment failed', 'partial refund', 'refund'

        :param status: The status of this InvoicePaymentStatusRequest.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

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
        if not isinstance(other, InvoicePaymentStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
