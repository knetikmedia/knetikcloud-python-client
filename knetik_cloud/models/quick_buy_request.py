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


class QuickBuyRequest(object):
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
        'sku': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'sku': 'sku',
        'user_id': 'user_id'
    }

    def __init__(self, sku=None, user_id=None):
        """
        QuickBuyRequest - a model defined in Swagger
        """

        self._sku = None
        self._user_id = None
        self.discriminator = None

        self.sku = sku
        if user_id is not None:
          self.user_id = user_id

    @property
    def sku(self):
        """
        Gets the sku of this QuickBuyRequest.
        SKU of item being purchased

        :return: The sku of this QuickBuyRequest.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this QuickBuyRequest.
        SKU of item being purchased

        :param sku: The sku of this QuickBuyRequest.
        :type: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")

        self._sku = sku

    @property
    def user_id(self):
        """
        Gets the user_id of this QuickBuyRequest.
        ID of the user making the purchase. If null, currently logged in user will be used.

        :return: The user_id of this QuickBuyRequest.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this QuickBuyRequest.
        ID of the user making the purchase. If null, currently logged in user will be used.

        :param user_id: The user_id of this QuickBuyRequest.
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
        if not isinstance(other, QuickBuyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
