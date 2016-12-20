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


class Config(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, public_read=None, value=None):
        """
        Config - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'public_read': 'bool',
            'value': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'public_read': 'public_read',
            'value': 'value'
        }

        self._name = name
        self._public_read = public_read
        self._value = value

    @property
    def name(self):
        """
        Gets the name of this Config.
        The name of the config

        :return: The name of this Config.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Config.
        The name of the config

        :param name: The name of this Config.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def public_read(self):
        """
        Gets the public_read of this Config.
        Whether the config is public for viewing. True means that it can be publicly viewed by all. Default: false

        :return: The public_read of this Config.
        :rtype: bool
        """
        return self._public_read

    @public_read.setter
    def public_read(self, public_read):
        """
        Sets the public_read of this Config.
        Whether the config is public for viewing. True means that it can be publicly viewed by all. Default: false

        :param public_read: The public_read of this Config.
        :type: bool
        """

        self._public_read = public_read

    @property
    def value(self):
        """
        Gets the value of this Config.
        The value of the config

        :return: The value of this Config.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Config.
        The value of the config

        :param value: The value of this Config.
        :type: str
        """

        self._value = value

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
