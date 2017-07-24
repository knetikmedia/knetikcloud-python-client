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


class VariableTypeResource(object):
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
        'base': 'str',
        'enumerable': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'base': 'base',
        'enumerable': 'enumerable',
        'name': 'name'
    }

    def __init__(self, base=None, enumerable=None, name=None):
        """
        VariableTypeResource - a model defined in Swagger
        """

        self._base = None
        self._enumerable = None
        self._name = None

        self.base = base
        if enumerable is not None:
          self.enumerable = enumerable
        self.name = name

    @property
    def base(self):
        """
        Gets the base of this VariableTypeResource.
        The base class of the type

        :return: The base of this VariableTypeResource.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """
        Sets the base of this VariableTypeResource.
        The base class of the type

        :param base: The base of this VariableTypeResource.
        :type: str
        """
        if base is None:
            raise ValueError("Invalid value for `base`, must not be `None`")
        allowed_values = ["NUMBER", "INTEGER", "STRING", "DATE", "BOOLEAN"]
        if base not in allowed_values:
            raise ValueError(
                "Invalid value for `base` ({0}), must be one of {1}"
                .format(base, allowed_values)
            )

        self._base = base

    @property
    def enumerable(self):
        """
        Gets the enumerable of this VariableTypeResource.
        Whether the type comes from a set of valid values that the system can provided (such as users)

        :return: The enumerable of this VariableTypeResource.
        :rtype: bool
        """
        return self._enumerable

    @enumerable.setter
    def enumerable(self, enumerable):
        """
        Sets the enumerable of this VariableTypeResource.
        Whether the type comes from a set of valid values that the system can provided (such as users)

        :param enumerable: The enumerable of this VariableTypeResource.
        :type: bool
        """

        self._enumerable = enumerable

    @property
    def name(self):
        """
        Gets the name of this VariableTypeResource.
        The name of the variable type. Used as the unique id

        :return: The name of this VariableTypeResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VariableTypeResource.
        The name of the variable type. Used as the unique id

        :param name: The name of this VariableTypeResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, VariableTypeResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
