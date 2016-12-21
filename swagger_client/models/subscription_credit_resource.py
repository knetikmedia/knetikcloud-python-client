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


class SubscriptionCreditResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, amount=None, created_date=None, id=None, inventory_id=None, reason=None):
        """
        SubscriptionCreditResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'amount': 'float',
            'created_date': 'int',
            'id': 'int',
            'inventory_id': 'int',
            'reason': 'str'
        }

        self.attribute_map = {
            'amount': 'amount',
            'created_date': 'created_date',
            'id': 'id',
            'inventory_id': 'inventory_id',
            'reason': 'reason'
        }

        self._amount = amount
        self._created_date = created_date
        self._id = id
        self._inventory_id = inventory_id
        self._reason = reason

    @property
    def amount(self):
        """
        Gets the amount of this SubscriptionCreditResource.
        The amount of the credit, negative for debt

        :return: The amount of this SubscriptionCreditResource.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this SubscriptionCreditResource.
        The amount of the credit, negative for debt

        :param amount: The amount of this SubscriptionCreditResource.
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")

        self._amount = amount

    @property
    def created_date(self):
        """
        Gets the created_date of this SubscriptionCreditResource.
        The date this credit was added, unix timestamp in seconds

        :return: The created_date of this SubscriptionCreditResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this SubscriptionCreditResource.
        The date this credit was added, unix timestamp in seconds

        :param created_date: The created_date of this SubscriptionCreditResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def id(self):
        """
        Gets the id of this SubscriptionCreditResource.
        The id of the credit record

        :return: The id of this SubscriptionCreditResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SubscriptionCreditResource.
        The id of the credit record

        :param id: The id of this SubscriptionCreditResource.
        :type: int
        """

        self._id = id

    @property
    def inventory_id(self):
        """
        Gets the inventory_id of this SubscriptionCreditResource.
        The id of the subscription inventory entry

        :return: The inventory_id of this SubscriptionCreditResource.
        :rtype: int
        """
        return self._inventory_id

    @inventory_id.setter
    def inventory_id(self, inventory_id):
        """
        Sets the inventory_id of this SubscriptionCreditResource.
        The id of the subscription inventory entry

        :param inventory_id: The inventory_id of this SubscriptionCreditResource.
        :type: int
        """

        self._inventory_id = inventory_id

    @property
    def reason(self):
        """
        Gets the reason of this SubscriptionCreditResource.
        The reason for the subscription credit

        :return: The reason of this SubscriptionCreditResource.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this SubscriptionCreditResource.
        The reason for the subscription credit

        :param reason: The reason of this SubscriptionCreditResource.
        :type: str
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")

        self._reason = reason

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