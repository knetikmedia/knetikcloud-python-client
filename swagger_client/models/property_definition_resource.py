# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PropertyDefinitionResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, required=None, type=None):
        """
        PropertyDefinitionResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'required': 'bool',
            'type': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'required': 'required',
            'type': 'type'
        }

        self._name = name
        self._required = required
        self._type = type

    @property
    def name(self):
        """
        Gets the name of this PropertyDefinitionResource.
        The name of the property

        :return: The name of this PropertyDefinitionResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PropertyDefinitionResource.
        The name of the property

        :param name: The name of this PropertyDefinitionResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def required(self):
        """
        Gets the required of this PropertyDefinitionResource.
        Whether the property is required

        :return: The required of this PropertyDefinitionResource.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this PropertyDefinitionResource.
        Whether the property is required

        :param required: The required of this PropertyDefinitionResource.
        :type: bool
        """
        if required is None:
            raise ValueError("Invalid value for `required`, must not be `None`")

        self._required = required

    @property
    def type(self):
        """
        Gets the type of this PropertyDefinitionResource.
        The type of the property. Used for polymorphic type recognition and thus must match an expected type with additional properties.

        :return: The type of this PropertyDefinitionResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PropertyDefinitionResource.
        The type of the property. Used for polymorphic type recognition and thus must match an expected type with additional properties.

        :param type: The type of this PropertyDefinitionResource.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
