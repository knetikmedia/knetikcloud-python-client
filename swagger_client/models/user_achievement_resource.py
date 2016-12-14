# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserAchievementResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, achieved=None, achievement_name=None, created_date=None, earned_date=None, id=None, progress=None, updated_date=None, user_id=None):
        """
        UserAchievementResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'achieved': 'bool',
            'achievement_name': 'str',
            'created_date': 'int',
            'earned_date': 'int',
            'id': 'str',
            'progress': 'int',
            'updated_date': 'int',
            'user_id': 'int'
        }

        self.attribute_map = {
            'achieved': 'achieved',
            'achievement_name': 'achievement_name',
            'created_date': 'created_date',
            'earned_date': 'earned_date',
            'id': 'id',
            'progress': 'progress',
            'updated_date': 'updated_date',
            'user_id': 'user_id'
        }

        self._achieved = achieved
        self._achievement_name = achievement_name
        self._created_date = created_date
        self._earned_date = earned_date
        self._id = id
        self._progress = progress
        self._updated_date = updated_date
        self._user_id = user_id

    @property
    def achieved(self):
        """
        Gets the achieved of this UserAchievementResource.
        Flag indicating whether the user has earned the achievement

        :return: The achieved of this UserAchievementResource.
        :rtype: bool
        """
        return self._achieved

    @achieved.setter
    def achieved(self, achieved):
        """
        Sets the achieved of this UserAchievementResource.
        Flag indicating whether the user has earned the achievement

        :param achieved: The achieved of this UserAchievementResource.
        :type: bool
        """

        self._achieved = achieved

    @property
    def achievement_name(self):
        """
        Gets the achievement_name of this UserAchievementResource.
        The achievement being tracked

        :return: The achievement_name of this UserAchievementResource.
        :rtype: str
        """
        return self._achievement_name

    @achievement_name.setter
    def achievement_name(self, achievement_name):
        """
        Sets the achievement_name of this UserAchievementResource.
        The achievement being tracked

        :param achievement_name: The achievement_name of this UserAchievementResource.
        :type: str
        """
        if achievement_name is None:
            raise ValueError("Invalid value for `achievement_name`, must not be `None`")

        self._achievement_name = achievement_name

    @property
    def created_date(self):
        """
        Gets the created_date of this UserAchievementResource.
        The date/time this resource was created in seconds since unix epoch

        :return: The created_date of this UserAchievementResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this UserAchievementResource.
        The date/time this resource was created in seconds since unix epoch

        :param created_date: The created_date of this UserAchievementResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def earned_date(self):
        """
        Gets the earned_date of this UserAchievementResource.
        The date/time the achievement was earned as a unix timestamp in seconds

        :return: The earned_date of this UserAchievementResource.
        :rtype: int
        """
        return self._earned_date

    @earned_date.setter
    def earned_date(self, earned_date):
        """
        Sets the earned_date of this UserAchievementResource.
        The date/time the achievement was earned as a unix timestamp in seconds

        :param earned_date: The earned_date of this UserAchievementResource.
        :type: int
        """

        self._earned_date = earned_date

    @property
    def id(self):
        """
        Gets the id of this UserAchievementResource.
        The id of the achievement progress

        :return: The id of this UserAchievementResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserAchievementResource.
        The id of the achievement progress

        :param id: The id of this UserAchievementResource.
        :type: str
        """

        self._id = id

    @property
    def progress(self):
        """
        Gets the progress of this UserAchievementResource.
        The current progress of the user on the achievement

        :return: The progress of this UserAchievementResource.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """
        Sets the progress of this UserAchievementResource.
        The current progress of the user on the achievement

        :param progress: The progress of this UserAchievementResource.
        :type: int
        """
        if progress is None:
            raise ValueError("Invalid value for `progress`, must not be `None`")

        self._progress = progress

    @property
    def updated_date(self):
        """
        Gets the updated_date of this UserAchievementResource.
        The date/time this resource was last updated in seconds since unix epoch

        :return: The updated_date of this UserAchievementResource.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this UserAchievementResource.
        The date/time this resource was last updated in seconds since unix epoch

        :param updated_date: The updated_date of this UserAchievementResource.
        :type: int
        """

        self._updated_date = updated_date

    @property
    def user_id(self):
        """
        Gets the user_id of this UserAchievementResource.
        The id of the user whose progress is being tracked

        :return: The user_id of this UserAchievementResource.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UserAchievementResource.
        The id of the user whose progress is being tracked

        :param user_id: The user_id of this UserAchievementResource.
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
