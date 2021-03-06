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


class GoogleToken(object):
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
        'authorization_code': 'str'
    }

    attribute_map = {
        'authorization_code': 'authorization_code'
    }

    def __init__(self, authorization_code=None):
        """
        GoogleToken - a model defined in Swagger
        """

        self._authorization_code = None
        self.discriminator = None

        self.authorization_code = authorization_code

    @property
    def authorization_code(self):
        """
        Gets the authorization_code of this GoogleToken.
        A valid authorization code from google. See google documention for how to obtain one.

        :return: The authorization_code of this GoogleToken.
        :rtype: str
        """
        return self._authorization_code

    @authorization_code.setter
    def authorization_code(self, authorization_code):
        """
        Sets the authorization_code of this GoogleToken.
        A valid authorization code from google. See google documention for how to obtain one.

        :param authorization_code: The authorization_code of this GoogleToken.
        :type: str
        """
        if authorization_code is None:
            raise ValueError("Invalid value for `authorization_code`, must not be `None`")

        self._authorization_code = authorization_code

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
        if not isinstance(other, GoogleToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
