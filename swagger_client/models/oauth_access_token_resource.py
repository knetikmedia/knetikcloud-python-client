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


class OauthAccessTokenResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, client_id=None, token=None, username=None):
        """
        OauthAccessTokenResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'client_id': 'str',
            'token': 'str',
            'username': 'str'
        }

        self.attribute_map = {
            'client_id': 'client_id',
            'token': 'token',
            'username': 'username'
        }

        self._client_id = client_id
        self._token = token
        self._username = username

    @property
    def client_id(self):
        """
        Gets the client_id of this OauthAccessTokenResource.
        The key of the client assosciated with the token

        :return: The client_id of this OauthAccessTokenResource.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this OauthAccessTokenResource.
        The key of the client assosciated with the token

        :param client_id: The client_id of this OauthAccessTokenResource.
        :type: str
        """

        self._client_id = client_id

    @property
    def token(self):
        """
        Gets the token of this OauthAccessTokenResource.
        The token.  Not shown in list view

        :return: The token of this OauthAccessTokenResource.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this OauthAccessTokenResource.
        The token.  Not shown in list view

        :param token: The token of this OauthAccessTokenResource.
        :type: str
        """

        self._token = token

    @property
    def username(self):
        """
        Gets the username of this OauthAccessTokenResource.
        The username of the user associated with the token

        :return: The username of this OauthAccessTokenResource.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this OauthAccessTokenResource.
        The username of the user associated with the token

        :param username: The username of this OauthAccessTokenResource.
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
