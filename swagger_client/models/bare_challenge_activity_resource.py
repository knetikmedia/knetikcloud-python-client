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


class BareChallengeActivityResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, activity_id=None, challenge_id=None, id=None):
        """
        BareChallengeActivityResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'activity_id': 'int',
            'challenge_id': 'int',
            'id': 'int'
        }

        self.attribute_map = {
            'activity_id': 'activity_id',
            'challenge_id': 'challenge_id',
            'id': 'id'
        }

        self._activity_id = activity_id
        self._challenge_id = challenge_id
        self._id = id

    @property
    def activity_id(self):
        """
        Gets the activity_id of this BareChallengeActivityResource.
        The id of the activity

        :return: The activity_id of this BareChallengeActivityResource.
        :rtype: int
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """
        Sets the activity_id of this BareChallengeActivityResource.
        The id of the activity

        :param activity_id: The activity_id of this BareChallengeActivityResource.
        :type: int
        """
        if activity_id is None:
            raise ValueError("Invalid value for `activity_id`, must not be `None`")

        self._activity_id = activity_id

    @property
    def challenge_id(self):
        """
        Gets the challenge_id of this BareChallengeActivityResource.
        The id of the challenge

        :return: The challenge_id of this BareChallengeActivityResource.
        :rtype: int
        """
        return self._challenge_id

    @challenge_id.setter
    def challenge_id(self, challenge_id):
        """
        Sets the challenge_id of this BareChallengeActivityResource.
        The id of the challenge

        :param challenge_id: The challenge_id of this BareChallengeActivityResource.
        :type: int
        """
        if challenge_id is None:
            raise ValueError("Invalid value for `challenge_id`, must not be `None`")

        self._challenge_id = challenge_id

    @property
    def id(self):
        """
        Gets the id of this BareChallengeActivityResource.
        The unique ID for this resource

        :return: The id of this BareChallengeActivityResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BareChallengeActivityResource.
        The unique ID for this resource

        :param id: The id of this BareChallengeActivityResource.
        :type: int
        """

        self._id = id

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
