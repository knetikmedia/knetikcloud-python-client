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


class ContributionResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, artist=None, media=None, role=None):
        """
        ContributionResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'artist': 'SimpleReferenceResourcelong',
            'media': 'SimpleReferenceResourcelong',
            'role': 'str'
        }

        self.attribute_map = {
            'artist': 'artist',
            'media': 'media',
            'role': 'role'
        }

        self._artist = artist
        self._media = media
        self._role = role

    @property
    def artist(self):
        """
        Gets the artist of this ContributionResource.
        A reference to the contributing artist

        :return: The artist of this ContributionResource.
        :rtype: SimpleReferenceResourcelong
        """
        return self._artist

    @artist.setter
    def artist(self, artist):
        """
        Sets the artist of this ContributionResource.
        A reference to the contributing artist

        :param artist: The artist of this ContributionResource.
        :type: SimpleReferenceResourcelong
        """
        if artist is None:
            raise ValueError("Invalid value for `artist`, must not be `None`")

        self._artist = artist

    @property
    def media(self):
        """
        Gets the media of this ContributionResource.
        A reference to the media being contributed to

        :return: The media of this ContributionResource.
        :rtype: SimpleReferenceResourcelong
        """
        return self._media

    @media.setter
    def media(self, media):
        """
        Sets the media of this ContributionResource.
        A reference to the media being contributed to

        :param media: The media of this ContributionResource.
        :type: SimpleReferenceResourcelong
        """
        if media is None:
            raise ValueError("Invalid value for `media`, must not be `None`")

        self._media = media

    @property
    def role(self):
        """
        Gets the role of this ContributionResource.
        The nature of the contribution (role of the artist as in 'producer', 'performer', etc)

        :return: The role of this ContributionResource.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this ContributionResource.
        The nature of the contribution (role of the artist as in 'producer', 'performer', etc)

        :param role: The role of this ContributionResource.
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")

        self._role = role

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
