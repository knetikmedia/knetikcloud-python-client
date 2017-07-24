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


class FinalizeBillingAgreementRequest(object):
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
        'new_default': 'bool',
        'payer_id': 'str',
        'token': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'invoice_id': 'invoice_id',
        'new_default': 'new_default',
        'payer_id': 'payer_id',
        'token': 'token',
        'user_id': 'user_id'
    }

    def __init__(self, invoice_id=None, new_default=None, payer_id=None, token=None, user_id=None):
        """
        FinalizeBillingAgreementRequest - a model defined in Swagger
        """

        self._invoice_id = None
        self._new_default = None
        self._payer_id = None
        self._token = None
        self._user_id = None

        if invoice_id is not None:
          self.invoice_id = invoice_id
        if new_default is not None:
          self.new_default = new_default
        if payer_id is not None:
          self.payer_id = payer_id
        self.token = token
        if user_id is not None:
          self.user_id = user_id

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this FinalizeBillingAgreementRequest.
        The ID of the invoice being paid along with the creation of this agreement

        :return: The invoice_id of this FinalizeBillingAgreementRequest.
        :rtype: int
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this FinalizeBillingAgreementRequest.
        The ID of the invoice being paid along with the creation of this agreement

        :param invoice_id: The invoice_id of this FinalizeBillingAgreementRequest.
        :type: int
        """

        self._invoice_id = invoice_id

    @property
    def new_default(self):
        """
        Gets the new_default of this FinalizeBillingAgreementRequest.
        Whether the new payment method created should be the user's default

        :return: The new_default of this FinalizeBillingAgreementRequest.
        :rtype: bool
        """
        return self._new_default

    @new_default.setter
    def new_default(self, new_default):
        """
        Sets the new_default of this FinalizeBillingAgreementRequest.
        Whether the new payment method created should be the user's default

        :param new_default: The new_default of this FinalizeBillingAgreementRequest.
        :type: bool
        """

        self._new_default = new_default

    @property
    def payer_id(self):
        """
        Gets the payer_id of this FinalizeBillingAgreementRequest.
        The payer ID from PayPal (passed as a parameter in the return URL). Only required if an invoice ID was included

        :return: The payer_id of this FinalizeBillingAgreementRequest.
        :rtype: str
        """
        return self._payer_id

    @payer_id.setter
    def payer_id(self, payer_id):
        """
        Sets the payer_id of this FinalizeBillingAgreementRequest.
        The payer ID from PayPal (passed as a parameter in the return URL). Only required if an invoice ID was included

        :param payer_id: The payer_id of this FinalizeBillingAgreementRequest.
        :type: str
        """

        self._payer_id = payer_id

    @property
    def token(self):
        """
        Gets the token of this FinalizeBillingAgreementRequest.
        The token from PayPal (passed as a parameter in the return URL)

        :return: The token of this FinalizeBillingAgreementRequest.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this FinalizeBillingAgreementRequest.
        The token from PayPal (passed as a parameter in the return URL)

        :param token: The token of this FinalizeBillingAgreementRequest.
        :type: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")

        self._token = token

    @property
    def user_id(self):
        """
        Gets the user_id of this FinalizeBillingAgreementRequest.
        The ID of the user. Defaults to the logged in user

        :return: The user_id of this FinalizeBillingAgreementRequest.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this FinalizeBillingAgreementRequest.
        The ID of the user. Defaults to the logged in user

        :param user_id: The user_id of this FinalizeBillingAgreementRequest.
        :type: int
        """

        self._user_id = user_id

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
        if not isinstance(other, FinalizeBillingAgreementRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
