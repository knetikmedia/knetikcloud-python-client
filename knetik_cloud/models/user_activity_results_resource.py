# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com.

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserActivityResultsResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'score': 'int',
        'tags': 'list[str]',
        'user_id': 'int'
    }

    attribute_map = {
        'score': 'score',
        'tags': 'tags',
        'user_id': 'user_id'
    }

    def __init__(self, score=None, tags=None, user_id=None):
        """
        UserActivityResultsResource - a model defined in Swagger
        """

        self._score = None
        self._tags = None
        self._user_id = None
        self.discriminator = None

        if score is not None:
          self.score = score
        if tags is not None:
          self.tags = tags
        self.user_id = user_id

    @property
    def score(self):
        """
        Gets the score of this UserActivityResultsResource.
        The raw score. Null means non-compete or disqualification

        :return: The score of this UserActivityResultsResource.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this UserActivityResultsResource.
        The raw score. Null means non-compete or disqualification

        :param score: The score of this UserActivityResultsResource.
        :type: int
        """

        self._score = score

    @property
    def tags(self):
        """
        Gets the tags of this UserActivityResultsResource.
        Any tags for the metric. Each unique tag will translate into a unique leaderboard. Maximum 5 tags and 50 characters each

        :return: The tags of this UserActivityResultsResource.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this UserActivityResultsResource.
        Any tags for the metric. Each unique tag will translate into a unique leaderboard. Maximum 5 tags and 50 characters each

        :param tags: The tags of this UserActivityResultsResource.
        :type: list[str]
        """

        self._tags = tags

    @property
    def user_id(self):
        """
        Gets the user_id of this UserActivityResultsResource.
        The id of the player

        :return: The user_id of this UserActivityResultsResource.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UserActivityResultsResource.
        The id of the player

        :param user_id: The user_id of this UserActivityResultsResource.
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
        if not isinstance(other, UserActivityResultsResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
