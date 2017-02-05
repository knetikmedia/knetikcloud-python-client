# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AchievementProgressUpdateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, increment_value=None, progress_value=None):
        """
        AchievementProgressUpdateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'increment_value': 'bool',
            'progress_value': 'int'
        }

        self.attribute_map = {
            'increment_value': 'increment_value',
            'progress_value': 'progress_value'
        }

        self._increment_value = increment_value
        self._progress_value = progress_value

    @property
    def increment_value(self):
        """
        Gets the increment_value of this AchievementProgressUpdateRequest.
        Whether to add one to the current progress instead of setting it to progress_value. Default: false

        :return: The increment_value of this AchievementProgressUpdateRequest.
        :rtype: bool
        """
        return self._increment_value

    @increment_value.setter
    def increment_value(self, increment_value):
        """
        Sets the increment_value of this AchievementProgressUpdateRequest.
        Whether to add one to the current progress instead of setting it to progress_value. Default: false

        :param increment_value: The increment_value of this AchievementProgressUpdateRequest.
        :type: bool
        """

        self._increment_value = increment_value

    @property
    def progress_value(self):
        """
        Gets the progress_value of this AchievementProgressUpdateRequest.
        The amount of progress towards earning the achievement. The max/target depends on the achievement. Required if increment_value is false/missing.

        :return: The progress_value of this AchievementProgressUpdateRequest.
        :rtype: int
        """
        return self._progress_value

    @progress_value.setter
    def progress_value(self, progress_value):
        """
        Sets the progress_value of this AchievementProgressUpdateRequest.
        The amount of progress towards earning the achievement. The max/target depends on the achievement. Required if increment_value is false/missing.

        :param progress_value: The progress_value of this AchievementProgressUpdateRequest.
        :type: int
        """

        self._progress_value = progress_value

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
        if not isinstance(other, AchievementProgressUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
