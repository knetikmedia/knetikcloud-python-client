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


class MetricResource(object):
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
        'activity_occurence_id': 'int',
        'tags': 'list[str]',
        'user_id': 'int',
        'value': 'int'
    }

    attribute_map = {
        'activity_occurence_id': 'activity_occurence_id',
        'tags': 'tags',
        'user_id': 'user_id',
        'value': 'value'
    }

    def __init__(self, activity_occurence_id=None, tags=None, user_id=None, value=None):
        """
        MetricResource - a model defined in Swagger
        """

        self._activity_occurence_id = None
        self._tags = None
        self._user_id = None
        self._value = None
        self.discriminator = None

        self.activity_occurence_id = activity_occurence_id
        if tags is not None:
          self.tags = tags
        if user_id is not None:
          self.user_id = user_id
        self.value = value

    @property
    def activity_occurence_id(self):
        """
        Gets the activity_occurence_id of this MetricResource.
        The id of the activity occurence where this score/metric occurred

        :return: The activity_occurence_id of this MetricResource.
        :rtype: int
        """
        return self._activity_occurence_id

    @activity_occurence_id.setter
    def activity_occurence_id(self, activity_occurence_id):
        """
        Sets the activity_occurence_id of this MetricResource.
        The id of the activity occurence where this score/metric occurred

        :param activity_occurence_id: The activity_occurence_id of this MetricResource.
        :type: int
        """
        if activity_occurence_id is None:
            raise ValueError("Invalid value for `activity_occurence_id`, must not be `None`")

        self._activity_occurence_id = activity_occurence_id

    @property
    def tags(self):
        """
        Gets the tags of this MetricResource.
        Any tags for the metric. Each unique tag will translate into a unique leaderboard. Maximum 5 tags and 50 characters each

        :return: The tags of this MetricResource.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this MetricResource.
        Any tags for the metric. Each unique tag will translate into a unique leaderboard. Maximum 5 tags and 50 characters each

        :param tags: The tags of this MetricResource.
        :type: list[str]
        """

        self._tags = tags

    @property
    def user_id(self):
        """
        Gets the user_id of this MetricResource.
        The id of the user this metric is for. Default to caller and requires METRICS_ADMIN permission to specify another

        :return: The user_id of this MetricResource.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this MetricResource.
        The id of the user this metric is for. Default to caller and requires METRICS_ADMIN permission to specify another

        :param user_id: The user_id of this MetricResource.
        :type: int
        """

        self._user_id = user_id

    @property
    def value(self):
        """
        Gets the value of this MetricResource.
        The value/score of the metric

        :return: The value of this MetricResource.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this MetricResource.
        The value/score of the metric

        :param value: The value of this MetricResource.
        :type: int
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value

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
        if not isinstance(other, MetricResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
