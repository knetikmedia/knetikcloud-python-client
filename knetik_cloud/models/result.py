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


class Result(object):
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
        'code': 'int',
        'request_id': 'str',
        'result': 'list[ErrorResource]'
    }

    attribute_map = {
        'code': 'code',
        'request_id': 'request_id',
        'result': 'result'
    }

    def __init__(self, code=None, request_id=None, result=None):
        """
        Result - a model defined in Swagger
        """

        self._code = None
        self._request_id = None
        self._result = None
        self.discriminator = None

        if code is not None:
          self.code = code
        if request_id is not None:
          self.request_id = request_id
        if result is not None:
          self.result = result

    @property
    def code(self):
        """
        Gets the code of this Result.
        The JSAPI error code

        :return: The code of this Result.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Result.
        The JSAPI error code

        :param code: The code of this Result.
        :type: int
        """

        self._code = code

    @property
    def request_id(self):
        """
        Gets the request_id of this Result.
        The id used for debugging lookup

        :return: The request_id of this Result.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this Result.
        The id used for debugging lookup

        :param request_id: The request_id of this Result.
        :type: str
        """

        self._request_id = request_id

    @property
    def result(self):
        """
        Gets the result of this Result.
        The error object

        :return: The result of this Result.
        :rtype: list[ErrorResource]
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this Result.
        The error object

        :param result: The result of this Result.
        :type: list[ErrorResource]
        """

        self._result = result

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
        if not isinstance(other, Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
