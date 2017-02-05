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


class ReactivateSubscriptionRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, inventory_id=None, reactivation_fee=None):
        """
        ReactivateSubscriptionRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'inventory_id': 'int',
            'reactivation_fee': 'bool'
        }

        self.attribute_map = {
            'inventory_id': 'inventory_id',
            'reactivation_fee': 'reactivation_fee'
        }

        self._inventory_id = inventory_id
        self._reactivation_fee = reactivation_fee

    @property
    def inventory_id(self):
        """
        Gets the inventory_id of this ReactivateSubscriptionRequest.
        The inventory to reactivate. Only required if using the deprecated subscriptions service

        :return: The inventory_id of this ReactivateSubscriptionRequest.
        :rtype: int
        """
        return self._inventory_id

    @inventory_id.setter
    def inventory_id(self, inventory_id):
        """
        Sets the inventory_id of this ReactivateSubscriptionRequest.
        The inventory to reactivate. Only required if using the deprecated subscriptions service

        :param inventory_id: The inventory_id of this ReactivateSubscriptionRequest.
        :type: int
        """

        self._inventory_id = inventory_id

    @property
    def reactivation_fee(self):
        """
        Gets the reactivation_fee of this ReactivateSubscriptionRequest.
        Whether to add the additional reactivation fee in addition to the recurring fee

        :return: The reactivation_fee of this ReactivateSubscriptionRequest.
        :rtype: bool
        """
        return self._reactivation_fee

    @reactivation_fee.setter
    def reactivation_fee(self, reactivation_fee):
        """
        Sets the reactivation_fee of this ReactivateSubscriptionRequest.
        Whether to add the additional reactivation fee in addition to the recurring fee

        :param reactivation_fee: The reactivation_fee of this ReactivateSubscriptionRequest.
        :type: bool
        """

        self._reactivation_fee = reactivation_fee

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
        if not isinstance(other, ReactivateSubscriptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
