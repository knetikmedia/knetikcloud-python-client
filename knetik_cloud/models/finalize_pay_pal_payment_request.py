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


class FinalizePayPalPaymentRequest(object):
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
        'invoice_id': 'int',
        'payer_id': 'str',
        'token': 'str'
    }

    attribute_map = {
        'invoice_id': 'invoice_id',
        'payer_id': 'payer_id',
        'token': 'token'
    }

    def __init__(self, invoice_id=None, payer_id=None, token=None):
        """
        FinalizePayPalPaymentRequest - a model defined in Swagger
        """

        self._invoice_id = None
        self._payer_id = None
        self._token = None

        self.invoice_id = invoice_id
        self.payer_id = payer_id
        self.token = token

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this FinalizePayPalPaymentRequest.
        The ID of the invoice that is being paid. Must match the invoice sent in originally

        :return: The invoice_id of this FinalizePayPalPaymentRequest.
        :rtype: int
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this FinalizePayPalPaymentRequest.
        The ID of the invoice that is being paid. Must match the invoice sent in originally

        :param invoice_id: The invoice_id of this FinalizePayPalPaymentRequest.
        :type: int
        """
        if invoice_id is None:
            raise ValueError("Invalid value for `invoice_id`, must not be `None`")

        self._invoice_id = invoice_id

    @property
    def payer_id(self):
        """
        Gets the payer_id of this FinalizePayPalPaymentRequest.
        The ID of the payer that PayPal returned with the user at the return URL

        :return: The payer_id of this FinalizePayPalPaymentRequest.
        :rtype: str
        """
        return self._payer_id

    @payer_id.setter
    def payer_id(self, payer_id):
        """
        Sets the payer_id of this FinalizePayPalPaymentRequest.
        The ID of the payer that PayPal returned with the user at the return URL

        :param payer_id: The payer_id of this FinalizePayPalPaymentRequest.
        :type: str
        """
        if payer_id is None:
            raise ValueError("Invalid value for `payer_id`, must not be `None`")

        self._payer_id = payer_id

    @property
    def token(self):
        """
        Gets the token of this FinalizePayPalPaymentRequest.
        The token that PayPal returned with the user in the return URL

        :return: The token of this FinalizePayPalPaymentRequest.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this FinalizePayPalPaymentRequest.
        The token that PayPal returned with the user in the return URL

        :param token: The token of this FinalizePayPalPaymentRequest.
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
        if not isinstance(other, FinalizePayPalPaymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
