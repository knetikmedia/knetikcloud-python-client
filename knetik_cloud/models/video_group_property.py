# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VideoGroupProperty(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, files=None):
        """
        VideoGroupProperty - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'files': 'list[FileProperty]'
        }

        self.attribute_map = {
            'type': 'type',
            'files': 'files'
        }

        self._type = type
        self._files = files

    @property
    def type(self):
        """
        Gets the type of this VideoGroupProperty.
        The type of the property. Used for polymorphic type recognition and thus must match an expected type with additional properties.

        :return: The type of this VideoGroupProperty.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VideoGroupProperty.
        The type of the property. Used for polymorphic type recognition and thus must match an expected type with additional properties.

        :param type: The type of this VideoGroupProperty.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def files(self):
        """
        Gets the files of this VideoGroupProperty.
        The list of files

        :return: The files of this VideoGroupProperty.
        :rtype: list[FileProperty]
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this VideoGroupProperty.
        The list of files

        :param files: The files of this VideoGroupProperty.
        :type: list[FileProperty]
        """

        self._files = files

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
        if not isinstance(other, VideoGroupProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
