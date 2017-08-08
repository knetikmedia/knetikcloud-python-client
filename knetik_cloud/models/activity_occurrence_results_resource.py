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


class ActivityOccurrenceResultsResource(object):
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
        'users': 'list[UserActivityResultsResource]'
    }

    attribute_map = {
        'users': 'users'
    }

    def __init__(self, users=None):
        """
        ActivityOccurrenceResultsResource - a model defined in Swagger
        """

        self._users = None
        self.discriminator = None

        self.users = users

    @property
    def users(self):
        """
        Gets the users of this ActivityOccurrenceResultsResource.
        The game results for each user. Include all users that played (paid to get in) even if they were eliminated without a result. A null metric is allowed

        :return: The users of this ActivityOccurrenceResultsResource.
        :rtype: list[UserActivityResultsResource]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this ActivityOccurrenceResultsResource.
        The game results for each user. Include all users that played (paid to get in) even if they were eliminated without a result. A null metric is allowed

        :param users: The users of this ActivityOccurrenceResultsResource.
        :type: list[UserActivityResultsResource]
        """
        if users is None:
            raise ValueError("Invalid value for `users`, must not be `None`")

        self._users = users

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
        if not isinstance(other, ActivityOccurrenceResultsResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
