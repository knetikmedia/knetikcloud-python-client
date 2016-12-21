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


class PollAnswerResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, count=None, key=None, text=None):
        """
        PollAnswerResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'count': 'int',
            'key': 'str',
            'text': 'str'
        }

        self.attribute_map = {
            'count': 'count',
            'key': 'key',
            'text': 'text'
        }

        self._count = count
        self._key = key
        self._text = text

    @property
    def count(self):
        """
        Gets the count of this PollAnswerResource.
        The number of uesrs that selected this answer

        :return: The count of this PollAnswerResource.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this PollAnswerResource.
        The number of uesrs that selected this answer

        :param count: The count of this PollAnswerResource.
        :type: int
        """

        self._count = count

    @property
    def key(self):
        """
        Gets the key of this PollAnswerResource.
        The key to the answer (for code reference)

        :return: The key of this PollAnswerResource.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this PollAnswerResource.
        The key to the answer (for code reference)

        :param key: The key of this PollAnswerResource.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def text(self):
        """
        Gets the text of this PollAnswerResource.
        The text of the answer (for user display)

        :return: The text of this PollAnswerResource.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this PollAnswerResource.
        The text of the answer (for user display)

        :param text: The text of this PollAnswerResource.
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")

        self._text = text

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
