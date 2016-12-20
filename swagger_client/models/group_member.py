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


class GroupMember(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, group=None, secondary=None, status=None, user=None):
        """
        GroupMember - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'group': 'Group',
            'secondary': 'bool',
            'status': 'str',
            'user': 'User'
        }

        self.attribute_map = {
            'group': 'group',
            'secondary': 'secondary',
            'status': 'status',
            'user': 'user'
        }

        self._group = group
        self._secondary = secondary
        self._status = status
        self._user = user

    @property
    def group(self):
        """
        Gets the group of this GroupMember.

        :return: The group of this GroupMember.
        :rtype: Group
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this GroupMember.

        :param group: The group of this GroupMember.
        :type: Group
        """

        self._group = group

    @property
    def secondary(self):
        """
        Gets the secondary of this GroupMember.

        :return: The secondary of this GroupMember.
        :rtype: bool
        """
        return self._secondary

    @secondary.setter
    def secondary(self, secondary):
        """
        Sets the secondary of this GroupMember.

        :param secondary: The secondary of this GroupMember.
        :type: bool
        """

        self._secondary = secondary

    @property
    def status(self):
        """
        Gets the status of this GroupMember.

        :return: The status of this GroupMember.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this GroupMember.

        :param status: The status of this GroupMember.
        :type: str
        """
        allowed_values = ["moderator", "member"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def user(self):
        """
        Gets the user of this GroupMember.

        :return: The user of this GroupMember.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this GroupMember.

        :param user: The user of this GroupMember.
        :type: User
        """

        self._user = user

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
