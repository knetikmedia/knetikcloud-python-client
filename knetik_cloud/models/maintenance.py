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


class Maintenance(object):
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
        'access_locked': 'bool',
        'details': 'object',
        'message': 'str'
    }

    attribute_map = {
        'access_locked': 'access_locked',
        'details': 'details',
        'message': 'message'
    }

    def __init__(self, access_locked=None, details=None, message=None):
        """
        Maintenance - a model defined in Swagger
        """

        self._access_locked = None
        self._details = None
        self._message = None

        self.access_locked = access_locked
        if details is not None:
          self.details = details
        self.message = message

    @property
    def access_locked(self):
        """
        Gets the access_locked of this Maintenance.
        Whether access to the system has been locked

        :return: The access_locked of this Maintenance.
        :rtype: bool
        """
        return self._access_locked

    @access_locked.setter
    def access_locked(self, access_locked):
        """
        Sets the access_locked of this Maintenance.
        Whether access to the system has been locked

        :param access_locked: The access_locked of this Maintenance.
        :type: bool
        """
        if access_locked is None:
            raise ValueError("Invalid value for `access_locked`, must not be `None`")

        self._access_locked = access_locked

    @property
    def details(self):
        """
        Gets the details of this Maintenance.
        A simple object of any schema for client side use and processing

        :return: The details of this Maintenance.
        :rtype: object
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this Maintenance.
        A simple object of any schema for client side use and processing

        :param details: The details of this Maintenance.
        :type: object
        """

        self._details = details

    @property
    def message(self):
        """
        Gets the message of this Maintenance.
        User displayable message about the maintenance

        :return: The message of this Maintenance.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Maintenance.
        User displayable message about the maintenance

        :param message: The message of this Maintenance.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

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
        if not isinstance(other, Maintenance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other