# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Timezone(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code=None, id=None, name=None, offset=None):
        """
        Timezone - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'str',
            'id': 'int',
            'name': 'str',
            'offset': 'float'
        }

        self.attribute_map = {
            'code': 'code',
            'id': 'id',
            'name': 'name',
            'offset': 'offset'
        }

        self._code = code
        self._id = id
        self._name = name
        self._offset = offset

    @property
    def code(self):
        """
        Gets the code of this Timezone.

        :return: The code of this Timezone.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Timezone.

        :param code: The code of this Timezone.
        :type: str
        """

        self._code = code

    @property
    def id(self):
        """
        Gets the id of this Timezone.

        :return: The id of this Timezone.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Timezone.

        :param id: The id of this Timezone.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Timezone.

        :return: The name of this Timezone.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Timezone.

        :param name: The name of this Timezone.
        :type: str
        """

        self._name = name

    @property
    def offset(self):
        """
        Gets the offset of this Timezone.

        :return: The offset of this Timezone.
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this Timezone.

        :param offset: The offset of this Timezone.
        :type: float
        """

        self._offset = offset

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
        if not isinstance(other, Timezone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
