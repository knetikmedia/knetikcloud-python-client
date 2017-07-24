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


class BreEvent(object):
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
        'event_name': 'str',
        'params': 'object'
    }

    attribute_map = {
        'event_name': 'event_name',
        'params': 'params'
    }

    def __init__(self, event_name=None, params=None):
        """
        BreEvent - a model defined in Swagger
        """

        self._event_name = None
        self._params = None

        self.event_name = event_name
        self.params = params

    @property
    def event_name(self):
        """
        Gets the event_name of this BreEvent.
        The event name of the trigger to be fired

        :return: The event_name of this BreEvent.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this BreEvent.
        The event name of the trigger to be fired

        :param event_name: The event_name of this BreEvent.
        :type: str
        """
        if event_name is None:
            raise ValueError("Invalid value for `event_name`, must not be `None`")

        self._event_name = event_name

    @property
    def params(self):
        """
        Gets the params of this BreEvent.
        The parameters to the event. A Map (assosiative array) with a key for each trigger parameter name and a corrosponding value.

        :return: The params of this BreEvent.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """
        Sets the params of this BreEvent.
        The parameters to the event. A Map (assosiative array) with a key for each trigger parameter name and a corrosponding value.

        :param params: The params of this BreEvent.
        :type: object
        """
        if params is None:
            raise ValueError("Invalid value for `params`, must not be `None`")

        self._params = params

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
        if not isinstance(other, BreEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
