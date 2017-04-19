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


class ClientResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, access_token_validity_seconds=None, client_key=None, grant_types=None, id=None, is_public=None, locked=None, name=None, redirect_uris=None, refresh_token_validity_seconds=None, secret=None):
        """
        ClientResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_token_validity_seconds': 'int',
            'client_key': 'str',
            'grant_types': 'list[str]',
            'id': 'int',
            'is_public': 'bool',
            'locked': 'bool',
            'name': 'str',
            'redirect_uris': 'list[str]',
            'refresh_token_validity_seconds': 'int',
            'secret': 'str'
        }

        self.attribute_map = {
            'access_token_validity_seconds': 'access_token_validity_seconds',
            'client_key': 'client_key',
            'grant_types': 'grant_types',
            'id': 'id',
            'is_public': 'is_public',
            'locked': 'locked',
            'name': 'name',
            'redirect_uris': 'redirect_uris',
            'refresh_token_validity_seconds': 'refresh_token_validity_seconds',
            'secret': 'secret'
        }

        self._access_token_validity_seconds = access_token_validity_seconds
        self._client_key = client_key
        self._grant_types = grant_types
        self._id = id
        self._is_public = is_public
        self._locked = locked
        self._name = name
        self._redirect_uris = redirect_uris
        self._refresh_token_validity_seconds = refresh_token_validity_seconds
        self._secret = secret

    @property
    def access_token_validity_seconds(self):
        """
        Gets the access_token_validity_seconds of this ClientResource.
        The expiration time of an initial oauth token in seconds

        :return: The access_token_validity_seconds of this ClientResource.
        :rtype: int
        """
        return self._access_token_validity_seconds

    @access_token_validity_seconds.setter
    def access_token_validity_seconds(self, access_token_validity_seconds):
        """
        Sets the access_token_validity_seconds of this ClientResource.
        The expiration time of an initial oauth token in seconds

        :param access_token_validity_seconds: The access_token_validity_seconds of this ClientResource.
        :type: int
        """

        self._access_token_validity_seconds = access_token_validity_seconds

    @property
    def client_key(self):
        """
        Gets the client_key of this ClientResource.
        The client_id field of the oauth token request

        :return: The client_key of this ClientResource.
        :rtype: str
        """
        return self._client_key

    @client_key.setter
    def client_key(self, client_key):
        """
        Sets the client_key of this ClientResource.
        The client_id field of the oauth token request

        :param client_key: The client_key of this ClientResource.
        :type: str
        """
        if client_key is None:
            raise ValueError("Invalid value for `client_key`, must not be `None`")

        self._client_key = client_key

    @property
    def grant_types(self):
        """
        Gets the grant_types of this ClientResource.
        The oauth grant type as in: password (username/password auth), client_credentials (server-to-server, private clients), refresh_token (to allow clients to refresh their initial token), facebook, google, etc) See documentation for a complete list. use dedicated endpoint PUT /grant-types to edit this list

        :return: The grant_types of this ClientResource.
        :rtype: list[str]
        """
        return self._grant_types

    @grant_types.setter
    def grant_types(self, grant_types):
        """
        Sets the grant_types of this ClientResource.
        The oauth grant type as in: password (username/password auth), client_credentials (server-to-server, private clients), refresh_token (to allow clients to refresh their initial token), facebook, google, etc) See documentation for a complete list. use dedicated endpoint PUT /grant-types to edit this list

        :param grant_types: The grant_types of this ClientResource.
        :type: list[str]
        """

        self._grant_types = grant_types

    @property
    def id(self):
        """
        Gets the id of this ClientResource.
        Generated unique ID for the client

        :return: The id of this ClientResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ClientResource.
        Generated unique ID for the client

        :param id: The id of this ClientResource.
        :type: int
        """

        self._id = id

    @property
    def is_public(self):
        """
        Gets the is_public of this ClientResource.
        Set to true if the client is public i.e the secret key can be secured

        :return: The is_public of this ClientResource.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """
        Sets the is_public of this ClientResource.
        Set to true if the client is public i.e the secret key can be secured

        :param is_public: The is_public of this ClientResource.
        :type: bool
        """

        self._is_public = is_public

    @property
    def locked(self):
        """
        Gets the locked of this ClientResource.
        Used to flag system clients that are not meant to be tinkered with

        :return: The locked of this ClientResource.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """
        Sets the locked of this ClientResource.
        Used to flag system clients that are not meant to be tinkered with

        :param locked: The locked of this ClientResource.
        :type: bool
        """

        self._locked = locked

    @property
    def name(self):
        """
        Gets the name of this ClientResource.
        The friendly name of the client

        :return: The name of this ClientResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ClientResource.
        The friendly name of the client

        :param name: The name of this ClientResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def redirect_uris(self):
        """
        Gets the redirect_uris of this ClientResource.
        A redirection URL to use when granting access to third-parties (seldomly used)

        :return: The redirect_uris of this ClientResource.
        :rtype: list[str]
        """
        return self._redirect_uris

    @redirect_uris.setter
    def redirect_uris(self, redirect_uris):
        """
        Sets the redirect_uris of this ClientResource.
        A redirection URL to use when granting access to third-parties (seldomly used)

        :param redirect_uris: The redirect_uris of this ClientResource.
        :type: list[str]
        """

        self._redirect_uris = redirect_uris

    @property
    def refresh_token_validity_seconds(self):
        """
        Gets the refresh_token_validity_seconds of this ClientResource.
        The expiration time of a refresh oauth token in seconds

        :return: The refresh_token_validity_seconds of this ClientResource.
        :rtype: int
        """
        return self._refresh_token_validity_seconds

    @refresh_token_validity_seconds.setter
    def refresh_token_validity_seconds(self, refresh_token_validity_seconds):
        """
        Sets the refresh_token_validity_seconds of this ClientResource.
        The expiration time of a refresh oauth token in seconds

        :param refresh_token_validity_seconds: The refresh_token_validity_seconds of this ClientResource.
        :type: int
        """

        self._refresh_token_validity_seconds = refresh_token_validity_seconds

    @property
    def secret(self):
        """
        Gets the secret of this ClientResource.
        The client-secret field of the oauth request when creating a private client

        :return: The secret of this ClientResource.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """
        Sets the secret of this ClientResource.
        The client-secret field of the oauth request when creating a private client

        :param secret: The secret of this ClientResource.
        :type: str
        """
        if secret is None:
            raise ValueError("Invalid value for `secret`, must not be `None`")

        self._secret = secret

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
        if not isinstance(other, ClientResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
