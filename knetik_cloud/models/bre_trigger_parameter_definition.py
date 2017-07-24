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


class BreTriggerParameterDefinition(object):
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
        'name': 'str',
        'optional': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'optional': 'optional',
        'type': 'type'
    }

    def __init__(self, name=None, optional=None, type=None):
        """
        BreTriggerParameterDefinition - a model defined in Swagger
        """

        self._name = None
        self._optional = None
        self._type = None

        self.name = name
        if optional is not None:
          self.optional = optional
        self.type = type

    @property
    def name(self):
        """
        Gets the name of this BreTriggerParameterDefinition.
        The name of the parameter. This is used as the unique identifier of this parameter

        :return: The name of this BreTriggerParameterDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BreTriggerParameterDefinition.
        The name of the parameter. This is used as the unique identifier of this parameter

        :param name: The name of this BreTriggerParameterDefinition.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def optional(self):
        """
        Gets the optional of this BreTriggerParameterDefinition.
        Whether this parameter can be left off when firing the event. Default false

        :return: The optional of this BreTriggerParameterDefinition.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """
        Sets the optional of this BreTriggerParameterDefinition.
        Whether this parameter can be left off when firing the event. Default false

        :param optional: The optional of this BreTriggerParameterDefinition.
        :type: bool
        """

        self._optional = optional

    @property
    def type(self):
        """
        Gets the type of this BreTriggerParameterDefinition.
        The variable type of this parameter. See Bre Variables endpoint for list

        :return: The type of this BreTriggerParameterDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BreTriggerParameterDefinition.
        The variable type of this parameter. See Bre Variables endpoint for list

        :param type: The type of this BreTriggerParameterDefinition.
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
        if not isinstance(other, BreTriggerParameterDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other