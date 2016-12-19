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


class SelectedSettingResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, key=None, key_name=None, value=None, value_name=None):
        """
        SelectedSettingResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'key': 'str',
            'key_name': 'str',
            'value': 'str',
            'value_name': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'key_name': 'key_name',
            'value': 'value',
            'value_name': 'value_name'
        }

        self._key = key
        self._key_name = key_name
        self._value = value
        self._value_name = value_name

    @property
    def key(self):
        """
        Gets the key of this SelectedSettingResource.
        The unique ID for the setting

        :return: The key of this SelectedSettingResource.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this SelectedSettingResource.
        The unique ID for the setting

        :param key: The key of this SelectedSettingResource.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def key_name(self):
        """
        Gets the key_name of this SelectedSettingResource.
        The textual name of the setting

        :return: The key_name of this SelectedSettingResource.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """
        Sets the key_name of this SelectedSettingResource.
        The textual name of the setting

        :param key_name: The key_name of this SelectedSettingResource.
        :type: str
        """
        if key_name is None:
            raise ValueError("Invalid value for `key_name`, must not be `None`")

        self._key_name = key_name

    @property
    def value(self):
        """
        Gets the value of this SelectedSettingResource.
        The unique ID for the option

        :return: The value of this SelectedSettingResource.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SelectedSettingResource.
        The unique ID for the option

        :param value: The value of this SelectedSettingResource.
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value

    @property
    def value_name(self):
        """
        Gets the value_name of this SelectedSettingResource.
        The textual name of the option

        :return: The value_name of this SelectedSettingResource.
        :rtype: str
        """
        return self._value_name

    @value_name.setter
    def value_name(self, value_name):
        """
        Sets the value_name of this SelectedSettingResource.
        The textual name of the option

        :param value_name: The value_name of this SelectedSettingResource.
        :type: str
        """
        if value_name is None:
            raise ValueError("Invalid value for `value_name`, must not be `None`")

        self._value_name = value_name

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
