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


class UserAchievementGroupResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, achievements=None, group_name=None, id=None, progress=None, user_id=None):
        """
        UserAchievementGroupResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'achievements': 'list[UserAchievementResource]',
            'group_name': 'str',
            'id': 'str',
            'progress': 'int',
            'user_id': 'int'
        }

        self.attribute_map = {
            'achievements': 'achievements',
            'group_name': 'group_name',
            'id': 'id',
            'progress': 'progress',
            'user_id': 'user_id'
        }

        self._achievements = achievements
        self._group_name = group_name
        self._id = id
        self._progress = progress
        self._user_id = user_id

    @property
    def achievements(self):
        """
        Gets the achievements of this UserAchievementGroupResource.
        The list of achievements associated with the group

        :return: The achievements of this UserAchievementGroupResource.
        :rtype: list[UserAchievementResource]
        """
        return self._achievements

    @achievements.setter
    def achievements(self, achievements):
        """
        Sets the achievements of this UserAchievementGroupResource.
        The list of achievements associated with the group

        :param achievements: The achievements of this UserAchievementGroupResource.
        :type: list[UserAchievementResource]
        """
        if achievements is None:
            raise ValueError("Invalid value for `achievements`, must not be `None`")

        self._achievements = achievements

    @property
    def group_name(self):
        """
        Gets the group_name of this UserAchievementGroupResource.
        The name of the group.  If used by Leveling, this will represent the level name

        :return: The group_name of this UserAchievementGroupResource.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this UserAchievementGroupResource.
        The name of the group.  If used by Leveling, this will represent the level name

        :param group_name: The group_name of this UserAchievementGroupResource.
        :type: str
        """
        if group_name is None:
            raise ValueError("Invalid value for `group_name`, must not be `None`")

        self._group_name = group_name

    @property
    def id(self):
        """
        Gets the id of this UserAchievementGroupResource.
        The id of the achievement progress

        :return: The id of this UserAchievementGroupResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserAchievementGroupResource.
        The id of the achievement progress

        :param id: The id of this UserAchievementGroupResource.
        :type: str
        """

        self._id = id

    @property
    def progress(self):
        """
        Gets the progress of this UserAchievementGroupResource.
        The current progress of the user on the group

        :return: The progress of this UserAchievementGroupResource.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """
        Sets the progress of this UserAchievementGroupResource.
        The current progress of the user on the group

        :param progress: The progress of this UserAchievementGroupResource.
        :type: int
        """
        if progress is None:
            raise ValueError("Invalid value for `progress`, must not be `None`")

        self._progress = progress

    @property
    def user_id(self):
        """
        Gets the user_id of this UserAchievementGroupResource.
        The id of the user whose progress is being tracked

        :return: The user_id of this UserAchievementGroupResource.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UserAchievementGroupResource.
        The id of the user whose progress is being tracked

        :param user_id: The user_id of this UserAchievementGroupResource.
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")

        self._user_id = user_id

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
