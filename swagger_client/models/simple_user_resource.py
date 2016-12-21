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


class SimpleUserResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, avatar_url=None, display_name=None, id=None, username=None):
        """
        SimpleUserResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'avatar_url': 'str',
            'display_name': 'str',
            'id': 'int',
            'username': 'str'
        }

        self.attribute_map = {
            'avatar_url': 'avatar_url',
            'display_name': 'display_name',
            'id': 'id',
            'username': 'username'
        }

        self._avatar_url = avatar_url
        self._display_name = display_name
        self._id = id
        self._username = username

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this SimpleUserResource.
        The url of the user's avatar image

        :return: The avatar_url of this SimpleUserResource.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this SimpleUserResource.
        The url of the user's avatar image

        :param avatar_url: The avatar_url of this SimpleUserResource.
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def display_name(self):
        """
        Gets the display_name of this SimpleUserResource.
        The public username of the user

        :return: The display_name of this SimpleUserResource.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SimpleUserResource.
        The public username of the user

        :param display_name: The display_name of this SimpleUserResource.
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this SimpleUserResource.
        The id of the user

        :return: The id of this SimpleUserResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SimpleUserResource.
        The id of the user

        :param id: The id of this SimpleUserResource.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def username(self):
        """
        Gets the username of this SimpleUserResource.
        The username of the user

        :return: The username of this SimpleUserResource.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this SimpleUserResource.
        The username of the user

        :param username: The username of this SimpleUserResource.
        :type: str
        """

        self._username = username

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
