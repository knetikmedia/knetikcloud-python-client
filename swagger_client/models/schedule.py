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


class Schedule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, duration=None, duration_unit=None, repeat=None):
        """
        Schedule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'duration': 'int',
            'duration_unit': 'str',
            'repeat': 'str'
        }

        self.attribute_map = {
            'duration': 'duration',
            'duration_unit': 'duration_unit',
            'repeat': 'repeat'
        }

        self._duration = duration
        self._duration_unit = duration_unit
        self._repeat = repeat

    @property
    def duration(self):
        """
        Gets the duration of this Schedule.
        The duration of the repeatable events

        :return: The duration of this Schedule.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this Schedule.
        The duration of the repeatable events

        :param duration: The duration of this Schedule.
        :type: int
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")

        self._duration = duration

    @property
    def duration_unit(self):
        """
        Gets the duration_unit of this Schedule.
        The unit of time for the duration field

        :return: The duration_unit of this Schedule.
        :rtype: str
        """
        return self._duration_unit

    @duration_unit.setter
    def duration_unit(self, duration_unit):
        """
        Sets the duration_unit of this Schedule.
        The unit of time for the duration field

        :param duration_unit: The duration_unit of this Schedule.
        :type: str
        """
        allowed_values = ["millisecond", "second", "minute", "hour", "day", "week", "month", "year"]
        if duration_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `duration_unit` ({0}), must be one of {1}"
                .format(duration_unit, allowed_values)
            )

        self._duration_unit = duration_unit

    @property
    def repeat(self):
        """
        Gets the repeat of this Schedule.
        How often the event is scheduled

        :return: The repeat of this Schedule.
        :rtype: str
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat):
        """
        Sets the repeat of this Schedule.
        How often the event is scheduled

        :param repeat: The repeat of this Schedule.
        :type: str
        """
        allowed_values = ["DAILY", "WEEKLY"]
        if repeat not in allowed_values:
            raise ValueError(
                "Invalid value for `repeat` ({0}), must be one of {1}"
                .format(repeat, allowed_values)
            )

        self._repeat = repeat

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
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
