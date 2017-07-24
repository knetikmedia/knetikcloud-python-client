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


class XsollaPaymentRequest(object):
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
        'return_url': 'str'
    }

    attribute_map = {
        'invoice_id': 'invoice_id',
        'return_url': 'return_url'
    }

    def __init__(self, invoice_id=None, return_url=None):
        """
        XsollaPaymentRequest - a model defined in Swagger
        """

        self._invoice_id = None
        self._return_url = None

        self.invoice_id = invoice_id
        self.return_url = return_url

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this XsollaPaymentRequest.
        The id of an invoice to pay

        :return: The invoice_id of this XsollaPaymentRequest.
        :rtype: int
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this XsollaPaymentRequest.
        The id of an invoice to pay

        :param invoice_id: The invoice_id of this XsollaPaymentRequest.
        :type: int
        """
        if invoice_id is None:
            raise ValueError("Invalid value for `invoice_id`, must not be `None`")

        self._invoice_id = invoice_id

    @property
    def return_url(self):
        """
        Gets the return_url of this XsollaPaymentRequest.
        The endpoint URL xsolla should forward the user to after they pay

        :return: The return_url of this XsollaPaymentRequest.
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """
        Sets the return_url of this XsollaPaymentRequest.
        The endpoint URL xsolla should forward the user to after they pay

        :param return_url: The return_url of this XsollaPaymentRequest.
        :type: str
        """
        if return_url is None:
            raise ValueError("Invalid value for `return_url`, must not be `None`")

        self._return_url = return_url

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
        if not isinstance(other, XsollaPaymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other