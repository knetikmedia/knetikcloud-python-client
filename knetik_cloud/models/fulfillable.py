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


class Fulfillable(object):
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
        'description': 'str',
        'type_hint': 'str',
        'type_name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'type_hint': 'type_hint',
        'type_name': 'type_name'
    }

    def __init__(self, description=None, type_hint=None, type_name=None):
        """
        Fulfillable - a model defined in Swagger
        """

        self._description = None
        self._type_hint = None
        self._type_name = None

        if description is not None:
          self.description = description
        if type_hint is not None:
          self.type_hint = type_hint
        self.type_name = type_name

    @property
    def description(self):
        """
        Gets the description of this Fulfillable.

        :return: The description of this Fulfillable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Fulfillable.

        :param description: The description of this Fulfillable.
        :type: str
        """

        self._description = description

    @property
    def type_hint(self):
        """
        Gets the type_hint of this Fulfillable.
        Used for polymorphic type recognition and thus must match an expected type with additional properties

        :return: The type_hint of this Fulfillable.
        :rtype: str
        """
        return self._type_hint

    @type_hint.setter
    def type_hint(self, type_hint):
        """
        Sets the type_hint of this Fulfillable.
        Used for polymorphic type recognition and thus must match an expected type with additional properties

        :param type_hint: The type_hint of this Fulfillable.
        :type: str
        """

        self._type_hint = type_hint

    @property
    def type_name(self):
        """
        Gets the type_name of this Fulfillable.
        The name of the fulfillment type that describes how the item should be fulfilled.  Examples: inventory, wallet, amazon

        :return: The type_name of this Fulfillable.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """
        Sets the type_name of this Fulfillable.
        The name of the fulfillment type that describes how the item should be fulfilled.  Examples: inventory, wallet, amazon

        :param type_name: The type_name of this Fulfillable.
        :type: str
        """
        if type_name is None:
            raise ValueError("Invalid value for `type_name`, must not be `None`")

        self._type_name = type_name

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
        if not isinstance(other, Fulfillable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
