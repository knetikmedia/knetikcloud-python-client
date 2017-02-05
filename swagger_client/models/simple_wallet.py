# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SimpleWallet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, balance=None, code=None, currency_name=None, id=None, user_id=None):
        """
        SimpleWallet - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'balance': 'float',
            'code': 'str',
            'currency_name': 'str',
            'id': 'int',
            'user_id': 'int'
        }

        self.attribute_map = {
            'balance': 'balance',
            'code': 'code',
            'currency_name': 'currency_name',
            'id': 'id',
            'user_id': 'user_id'
        }

        self._balance = balance
        self._code = code
        self._currency_name = currency_name
        self._id = id
        self._user_id = user_id

    @property
    def balance(self):
        """
        Gets the balance of this SimpleWallet.
        The current balance of the wallet

        :return: The balance of this SimpleWallet.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """
        Sets the balance of this SimpleWallet.
        The current balance of the wallet

        :param balance: The balance of this SimpleWallet.
        :type: float
        """

        self._balance = balance

    @property
    def code(self):
        """
        Gets the code of this SimpleWallet.
        The ISO currency code for the wallet

        :return: The code of this SimpleWallet.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this SimpleWallet.
        The ISO currency code for the wallet

        :param code: The code of this SimpleWallet.
        :type: str
        """

        self._code = code

    @property
    def currency_name(self):
        """
        Gets the currency_name of this SimpleWallet.
        The name of the currency stored in the wallet

        :return: The currency_name of this SimpleWallet.
        :rtype: str
        """
        return self._currency_name

    @currency_name.setter
    def currency_name(self, currency_name):
        """
        Sets the currency_name of this SimpleWallet.
        The name of the currency stored in the wallet

        :param currency_name: The currency_name of this SimpleWallet.
        :type: str
        """

        self._currency_name = currency_name

    @property
    def id(self):
        """
        Gets the id of this SimpleWallet.
        The unique ID of the wallet

        :return: The id of this SimpleWallet.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SimpleWallet.
        The unique ID of the wallet

        :param id: The id of this SimpleWallet.
        :type: int
        """

        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this SimpleWallet.
        The ID of the user to whom the wallet belongs

        :return: The user_id of this SimpleWallet.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this SimpleWallet.
        The ID of the user to whom the wallet belongs

        :param user_id: The user_id of this SimpleWallet.
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
        if not isinstance(other, SimpleWallet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
