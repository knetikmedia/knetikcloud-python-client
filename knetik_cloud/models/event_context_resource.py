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


class EventContextResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, event_name=None, parameters=None, type=None):
        """
        EventContextResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'event_name': 'str',
            'parameters': 'dict(str, ExpressionResource)',
            'type': 'str'
        }

        self.attribute_map = {
            'event_name': 'event_name',
            'parameters': 'parameters',
            'type': 'type'
        }

        self._event_name = event_name
        self._parameters = parameters
        self._type = type

    @property
    def event_name(self):
        """
        Gets the event_name of this EventContextResource.

        :return: The event_name of this EventContextResource.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this EventContextResource.

        :param event_name: The event_name of this EventContextResource.
        :type: str
        """

        self._event_name = event_name

    @property
    def parameters(self):
        """
        Gets the parameters of this EventContextResource.

        :return: The parameters of this EventContextResource.
        :rtype: dict(str, ExpressionResource)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this EventContextResource.

        :param parameters: The parameters of this EventContextResource.
        :type: dict(str, ExpressionResource)
        """

        self._parameters = parameters

    @property
    def type(self):
        """
        Gets the type of this EventContextResource.

        :return: The type of this EventContextResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this EventContextResource.

        :param type: The type of this EventContextResource.
        :type: str
        """

        self._type = type

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
        if not isinstance(other, EventContextResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
