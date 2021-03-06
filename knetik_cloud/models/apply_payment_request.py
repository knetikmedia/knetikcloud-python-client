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


class ApplyPaymentRequest(object):
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
        'receipt': 'str',
        'transaction_id': 'str'
    }

    attribute_map = {
        'invoice_id': 'invoice_id',
        'receipt': 'receipt',
        'transaction_id': 'transaction_id'
    }

    def __init__(self, invoice_id=None, receipt=None, transaction_id=None):
        """
        ApplyPaymentRequest - a model defined in Swagger
        """

        self._invoice_id = None
        self._receipt = None
        self._transaction_id = None
        self.discriminator = None

        self.invoice_id = invoice_id
        self.receipt = receipt
        self.transaction_id = transaction_id

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this ApplyPaymentRequest.
        The id of the local invoice being paid.

        :return: The invoice_id of this ApplyPaymentRequest.
        :rtype: int
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this ApplyPaymentRequest.
        The id of the local invoice being paid.

        :param invoice_id: The invoice_id of this ApplyPaymentRequest.
        :type: int
        """
        if invoice_id is None:
            raise ValueError("Invalid value for `invoice_id`, must not be `None`")

        self._invoice_id = invoice_id

    @property
    def receipt(self):
        """
        Gets the receipt of this ApplyPaymentRequest.
        The encoded receipt string from Apple's services.

        :return: The receipt of this ApplyPaymentRequest.
        :rtype: str
        """
        return self._receipt

    @receipt.setter
    def receipt(self, receipt):
        """
        Sets the receipt of this ApplyPaymentRequest.
        The encoded receipt string from Apple's services.

        :param receipt: The receipt of this ApplyPaymentRequest.
        :type: str
        """
        if receipt is None:
            raise ValueError("Invalid value for `receipt`, must not be `None`")

        self._receipt = receipt

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this ApplyPaymentRequest.
        The id of the specific transaction from Apple's services.

        :return: The transaction_id of this ApplyPaymentRequest.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this ApplyPaymentRequest.
        The id of the specific transaction from Apple's services.

        :param transaction_id: The transaction_id of this ApplyPaymentRequest.
        :type: str
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")

        self._transaction_id = transaction_id

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
        if not isinstance(other, ApplyPaymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
