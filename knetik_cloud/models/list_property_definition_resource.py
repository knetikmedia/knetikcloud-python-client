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


class ListPropertyDefinitionResource(object):
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
        'max_count': 'int',
        'min_count': 'int',
        'value_definition': 'PropertyDefinitionResource'
    }

    attribute_map = {
        'max_count': 'max_count',
        'min_count': 'min_count',
        'value_definition': 'value_definition'
    }

    def __init__(self, max_count=None, min_count=None, value_definition=None):
        """
        ListPropertyDefinitionResource - a model defined in Swagger
        """

        self._max_count = None
        self._min_count = None
        self._value_definition = None
        self.discriminator = None

        if max_count is not None:
          self.max_count = max_count
        if min_count is not None:
          self.min_count = min_count
        if value_definition is not None:
          self.value_definition = value_definition

    @property
    def max_count(self):
        """
        Gets the max_count of this ListPropertyDefinitionResource.
        If provided, the maximum number of files in the group

        :return: The max_count of this ListPropertyDefinitionResource.
        :rtype: int
        """
        return self._max_count

    @max_count.setter
    def max_count(self, max_count):
        """
        Sets the max_count of this ListPropertyDefinitionResource.
        If provided, the maximum number of files in the group

        :param max_count: The max_count of this ListPropertyDefinitionResource.
        :type: int
        """

        self._max_count = max_count

    @property
    def min_count(self):
        """
        Gets the min_count of this ListPropertyDefinitionResource.
        If provided, the minimum number of files in the group

        :return: The min_count of this ListPropertyDefinitionResource.
        :rtype: int
        """
        return self._min_count

    @min_count.setter
    def min_count(self, min_count):
        """
        Sets the min_count of this ListPropertyDefinitionResource.
        If provided, the minimum number of files in the group

        :param min_count: The min_count of this ListPropertyDefinitionResource.
        :type: int
        """

        self._min_count = min_count

    @property
    def value_definition(self):
        """
        Gets the value_definition of this ListPropertyDefinitionResource.
        If provided, a property definition for validating values within list

        :return: The value_definition of this ListPropertyDefinitionResource.
        :rtype: PropertyDefinitionResource
        """
        return self._value_definition

    @value_definition.setter
    def value_definition(self, value_definition):
        """
        Sets the value_definition of this ListPropertyDefinitionResource.
        If provided, a property definition for validating values within list

        :param value_definition: The value_definition of this ListPropertyDefinitionResource.
        :type: PropertyDefinitionResource
        """

        self._value_definition = value_definition

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
        if not isinstance(other, ListPropertyDefinitionResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
