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


class AvailableSettingResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, advanced_option=None, default_value=None, description=None, key=None, name=None, options=None):
        """
        AvailableSettingResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'advanced_option': 'bool',
            'default_value': 'str',
            'description': 'str',
            'key': 'str',
            'name': 'str',
            'options': 'list[SettingOption]'
        }

        self.attribute_map = {
            'advanced_option': 'advanced_option',
            'default_value': 'default_value',
            'description': 'description',
            'key': 'key',
            'name': 'name',
            'options': 'options'
        }

        self._advanced_option = advanced_option
        self._default_value = default_value
        self._description = description
        self._key = key
        self._name = name
        self._options = options

    @property
    def advanced_option(self):
        """
        Gets the advanced_option of this AvailableSettingResource.
        Whether the setting is advanced. Default: false

        :return: The advanced_option of this AvailableSettingResource.
        :rtype: bool
        """
        return self._advanced_option

    @advanced_option.setter
    def advanced_option(self, advanced_option):
        """
        Sets the advanced_option of this AvailableSettingResource.
        Whether the setting is advanced. Default: false

        :param advanced_option: The advanced_option of this AvailableSettingResource.
        :type: bool
        """

        self._advanced_option = advanced_option

    @property
    def default_value(self):
        """
        Gets the default_value of this AvailableSettingResource.
        The value of the default option (must be in options array)

        :return: The default_value of this AvailableSettingResource.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this AvailableSettingResource.
        The value of the default option (must be in options array)

        :param default_value: The default_value of this AvailableSettingResource.
        :type: str
        """
        if default_value is None:
            raise ValueError("Invalid value for `default_value`, must not be `None`")

        self._default_value = default_value

    @property
    def description(self):
        """
        Gets the description of this AvailableSettingResource.
        The description of the setting

        :return: The description of this AvailableSettingResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AvailableSettingResource.
        The description of the setting

        :param description: The description of this AvailableSettingResource.
        :type: str
        """

        self._description = description

    @property
    def key(self):
        """
        Gets the key of this AvailableSettingResource.
        The unique ID for the setting

        :return: The key of this AvailableSettingResource.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this AvailableSettingResource.
        The unique ID for the setting

        :param key: The key of this AvailableSettingResource.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def name(self):
        """
        Gets the name of this AvailableSettingResource.
        The textual name of the setting

        :return: The name of this AvailableSettingResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AvailableSettingResource.
        The textual name of the setting

        :param name: The name of this AvailableSettingResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def options(self):
        """
        Gets the options of this AvailableSettingResource.
        The set of options available for this setting

        :return: The options of this AvailableSettingResource.
        :rtype: list[SettingOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this AvailableSettingResource.
        The set of options available for this setting

        :param options: The options of this AvailableSettingResource.
        :type: list[SettingOption]
        """
        if options is None:
            raise ValueError("Invalid value for `options`, must not be `None`")

        self._options = options

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
