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


class MapResource(object):
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
        'map': 'dict(str, ExpressionResource)',
        'type': 'str'
    }

    attribute_map = {
        'map': 'map',
        'type': 'type'
    }

    def __init__(self, map=None, type=None):
        """
        MapResource - a model defined in Swagger
        """

        self._map = None
        self._type = None

        if map is not None:
          self.map = map
        if type is not None:
          self.type = type

    @property
    def map(self):
        """
        Gets the map of this MapResource.

        :return: The map of this MapResource.
        :rtype: dict(str, ExpressionResource)
        """
        return self._map

    @map.setter
    def map(self, map):
        """
        Sets the map of this MapResource.

        :param map: The map of this MapResource.
        :type: dict(str, ExpressionResource)
        """

        self._map = map

    @property
    def type(self):
        """
        Gets the type of this MapResource.

        :return: The type of this MapResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MapResource.

        :param type: The type of this MapResource.
        :type: str
        """

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
        if not isinstance(other, MapResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other