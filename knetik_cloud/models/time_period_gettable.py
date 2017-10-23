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


class TimePeriodGettable(object):
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
        'get_limit': 'int',
        'group_name': 'str',
        'time_length': 'int',
        'unit_of_time': 'str'
    }

    attribute_map = {
        'get_limit': 'get_limit',
        'group_name': 'group_name',
        'time_length': 'time_length',
        'unit_of_time': 'unit_of_time'
    }

    def __init__(self, get_limit=None, group_name=None, time_length=None, unit_of_time=None):
        """
        TimePeriodGettable - a model defined in Swagger
        """

        self._get_limit = None
        self._group_name = None
        self._time_length = None
        self._unit_of_time = None
        self.discriminator = None

        self.get_limit = get_limit
        if group_name is not None:
          self.group_name = group_name
        self.time_length = time_length
        self.unit_of_time = unit_of_time

    @property
    def get_limit(self):
        """
        Gets the get_limit of this TimePeriodGettable.
        The time period limit

        :return: The get_limit of this TimePeriodGettable.
        :rtype: int
        """
        return self._get_limit

    @get_limit.setter
    def get_limit(self, get_limit):
        """
        Sets the get_limit of this TimePeriodGettable.
        The time period limit

        :param get_limit: The get_limit of this TimePeriodGettable.
        :type: int
        """
        if get_limit is None:
            raise ValueError("Invalid value for `get_limit`, must not be `None`")

        self._get_limit = get_limit

    @property
    def group_name(self):
        """
        Gets the group_name of this TimePeriodGettable.
        The name of a group of items. Multiple items with the same group name will be limited together, leave null to be assigned a random unique name. It is typical that the other properties here will be the same for all, but this is not enforced and the item being recieved will use its settings.

        :return: The group_name of this TimePeriodGettable.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """
        Sets the group_name of this TimePeriodGettable.
        The name of a group of items. Multiple items with the same group name will be limited together, leave null to be assigned a random unique name. It is typical that the other properties here will be the same for all, but this is not enforced and the item being recieved will use its settings.

        :param group_name: The group_name of this TimePeriodGettable.
        :type: str
        """

        self._group_name = group_name

    @property
    def time_length(self):
        """
        Gets the time_length of this TimePeriodGettable.
        The length of time

        :return: The time_length of this TimePeriodGettable.
        :rtype: int
        """
        return self._time_length

    @time_length.setter
    def time_length(self, time_length):
        """
        Sets the time_length of this TimePeriodGettable.
        The length of time

        :param time_length: The time_length of this TimePeriodGettable.
        :type: int
        """
        if time_length is None:
            raise ValueError("Invalid value for `time_length`, must not be `None`")

        self._time_length = time_length

    @property
    def unit_of_time(self):
        """
        Gets the unit_of_time of this TimePeriodGettable.
        The unit of time

        :return: The unit_of_time of this TimePeriodGettable.
        :rtype: str
        """
        return self._unit_of_time

    @unit_of_time.setter
    def unit_of_time(self, unit_of_time):
        """
        Sets the unit_of_time of this TimePeriodGettable.
        The unit of time

        :param unit_of_time: The unit_of_time of this TimePeriodGettable.
        :type: str
        """
        if unit_of_time is None:
            raise ValueError("Invalid value for `unit_of_time`, must not be `None`")

        self._unit_of_time = unit_of_time

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
        if not isinstance(other, TimePeriodGettable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
