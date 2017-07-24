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


class WalletAlterRequest(object):
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
        'delta': 'float',
        'invoice_id': 'int',
        'reason': 'str',
        'type': 'str'
    }

    attribute_map = {
        'delta': 'delta',
        'invoice_id': 'invoice_id',
        'reason': 'reason',
        'type': 'type'
    }

    def __init__(self, delta=None, invoice_id=None, reason=None, type=None):
        """
        WalletAlterRequest - a model defined in Swagger
        """

        self._delta = None
        self._invoice_id = None
        self._reason = None
        self._type = None

        self.delta = delta
        if invoice_id is not None:
          self.invoice_id = invoice_id
        self.reason = reason
        if type is not None:
          self.type = type

    @property
    def delta(self):
        """
        Gets the delta of this WalletAlterRequest.
        The amount of currency to add/remove. positive to add, negative to remove

        :return: The delta of this WalletAlterRequest.
        :rtype: float
        """
        return self._delta

    @delta.setter
    def delta(self, delta):
        """
        Sets the delta of this WalletAlterRequest.
        The amount of currency to add/remove. positive to add, negative to remove

        :param delta: The delta of this WalletAlterRequest.
        :type: float
        """
        if delta is None:
            raise ValueError("Invalid value for `delta`, must not be `None`")

        self._delta = delta

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this WalletAlterRequest.
        The id of an invoice to attribute the transaction to

        :return: The invoice_id of this WalletAlterRequest.
        :rtype: int
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this WalletAlterRequest.
        The id of an invoice to attribute the transaction to

        :param invoice_id: The invoice_id of this WalletAlterRequest.
        :type: int
        """

        self._invoice_id = invoice_id

    @property
    def reason(self):
        """
        Gets the reason of this WalletAlterRequest.
        The admin entered or system generated reason

        :return: The reason of this WalletAlterRequest.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this WalletAlterRequest.
        The admin entered or system generated reason

        :param reason: The reason of this WalletAlterRequest.
        :type: str
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")

        self._reason = reason

    @property
    def type(self):
        """
        Gets the type of this WalletAlterRequest.
        The transaction type to allow for search/etc

        :return: The type of this WalletAlterRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WalletAlterRequest.
        The transaction type to allow for search/etc

        :param type: The type of this WalletAlterRequest.
        :type: str
        """

        self._type = type

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
        if not isinstance(other, WalletAlterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other