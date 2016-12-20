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


class Currency(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active=None, code=None, date_created=None, date_updated=None, factor=None, icon=None, id=None, name=None, type=None, virtual=None):
        """
        Currency - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active': 'bool',
            'code': 'str',
            'date_created': 'int',
            'date_updated': 'int',
            'factor': 'float',
            'icon': 'str',
            'id': 'int',
            'name': 'str',
            'type': 'str',
            'virtual': 'bool'
        }

        self.attribute_map = {
            'active': 'active',
            'code': 'code',
            'date_created': 'date_created',
            'date_updated': 'date_updated',
            'factor': 'factor',
            'icon': 'icon',
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'virtual': 'virtual'
        }

        self._active = active
        self._code = code
        self._date_created = date_created
        self._date_updated = date_updated
        self._factor = factor
        self._icon = icon
        self._id = id
        self._name = name
        self._type = type
        self._virtual = virtual

    @property
    def active(self):
        """
        Gets the active of this Currency.

        :return: The active of this Currency.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Currency.

        :param active: The active of this Currency.
        :type: bool
        """

        self._active = active

    @property
    def code(self):
        """
        Gets the code of this Currency.

        :return: The code of this Currency.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Currency.

        :param code: The code of this Currency.
        :type: str
        """

        self._code = code

    @property
    def date_created(self):
        """
        Gets the date_created of this Currency.

        :return: The date_created of this Currency.
        :rtype: int
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this Currency.

        :param date_created: The date_created of this Currency.
        :type: int
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """
        Gets the date_updated of this Currency.

        :return: The date_updated of this Currency.
        :rtype: int
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """
        Sets the date_updated of this Currency.

        :param date_updated: The date_updated of this Currency.
        :type: int
        """

        self._date_updated = date_updated

    @property
    def factor(self):
        """
        Gets the factor of this Currency.

        :return: The factor of this Currency.
        :rtype: float
        """
        return self._factor

    @factor.setter
    def factor(self, factor):
        """
        Sets the factor of this Currency.

        :param factor: The factor of this Currency.
        :type: float
        """

        self._factor = factor

    @property
    def icon(self):
        """
        Gets the icon of this Currency.

        :return: The icon of this Currency.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """
        Sets the icon of this Currency.

        :param icon: The icon of this Currency.
        :type: str
        """

        self._icon = icon

    @property
    def id(self):
        """
        Gets the id of this Currency.

        :return: The id of this Currency.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Currency.

        :param id: The id of this Currency.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Currency.

        :return: The name of this Currency.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Currency.

        :param name: The name of this Currency.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Currency.

        :return: The type of this Currency.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Currency.

        :param type: The type of this Currency.
        :type: str
        """
        allowed_values = ["real", "virtual"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def virtual(self):
        """
        Gets the virtual of this Currency.

        :return: The virtual of this Currency.
        :rtype: bool
        """
        return self._virtual

    @virtual.setter
    def virtual(self, virtual):
        """
        Sets the virtual of this Currency.

        :param virtual: The virtual of this Currency.
        :type: bool
        """

        self._virtual = virtual

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
