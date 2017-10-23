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


class ActivityOccurrenceJoinResult(object):
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
        'entitlement': 'ActivityEntitlementResource',
        'error_code': 'int',
        'message': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'entitlement': 'entitlement',
        'error_code': 'error_code',
        'message': 'message',
        'user_id': 'user_id'
    }

    def __init__(self, entitlement=None, error_code=None, message=None, user_id=None):
        """
        ActivityOccurrenceJoinResult - a model defined in Swagger
        """

        self._entitlement = None
        self._error_code = None
        self._message = None
        self._user_id = None
        self.discriminator = None

        if entitlement is not None:
          self.entitlement = entitlement
        self.error_code = error_code
        if message is not None:
          self.message = message
        self.user_id = user_id

    @property
    def entitlement(self):
        """
        Gets the entitlement of this ActivityOccurrenceJoinResult.
        The details on the entitlement object needed to enter the occurrence (if any)

        :return: The entitlement of this ActivityOccurrenceJoinResult.
        :rtype: ActivityEntitlementResource
        """
        return self._entitlement

    @entitlement.setter
    def entitlement(self, entitlement):
        """
        Sets the entitlement of this ActivityOccurrenceJoinResult.
        The details on the entitlement object needed to enter the occurrence (if any)

        :param entitlement: The entitlement of this ActivityOccurrenceJoinResult.
        :type: ActivityEntitlementResource
        """

        self._entitlement = entitlement

    @property
    def error_code(self):
        """
        Gets the error_code of this ActivityOccurrenceJoinResult.
        Zero if the user was/could be added to the occurrence. Jsapi error code indicating the reason of the failure otherwise

        :return: The error_code of this ActivityOccurrenceJoinResult.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this ActivityOccurrenceJoinResult.
        Zero if the user was/could be added to the occurrence. Jsapi error code indicating the reason of the failure otherwise

        :param error_code: The error_code of this ActivityOccurrenceJoinResult.
        :type: int
        """
        if error_code is None:
            raise ValueError("Invalid value for `error_code`, must not be `None`")

        self._error_code = error_code

    @property
    def message(self):
        """
        Gets the message of this ActivityOccurrenceJoinResult.
        An error message if failure

        :return: The message of this ActivityOccurrenceJoinResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ActivityOccurrenceJoinResult.
        An error message if failure

        :param message: The message of this ActivityOccurrenceJoinResult.
        :type: str
        """

        self._message = message

    @property
    def user_id(self):
        """
        Gets the user_id of this ActivityOccurrenceJoinResult.
        The user's id

        :return: The user_id of this ActivityOccurrenceJoinResult.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ActivityOccurrenceJoinResult.
        The user's id

        :param user_id: The user_id of this ActivityOccurrenceJoinResult.
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
        if not isinstance(other, ActivityOccurrenceJoinResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
