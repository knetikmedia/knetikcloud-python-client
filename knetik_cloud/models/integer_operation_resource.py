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


class IntegerOperationResource(object):
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
        'args': 'list[ExpressionResource]',
        'op': 'str',
        'type': 'str'
    }

    attribute_map = {
        'args': 'args',
        'op': 'op',
        'type': 'type'
    }

    def __init__(self, args=None, op=None, type=None):
        """
        IntegerOperationResource - a model defined in Swagger
        """

        self._args = None
        self._op = None
        self._type = None

        if args is not None:
          self.args = args
        if op is not None:
          self.op = op
        if type is not None:
          self.type = type

    @property
    def args(self):
        """
        Gets the args of this IntegerOperationResource.

        :return: The args of this IntegerOperationResource.
        :rtype: list[ExpressionResource]
        """
        return self._args

    @args.setter
    def args(self, args):
        """
        Sets the args of this IntegerOperationResource.

        :param args: The args of this IntegerOperationResource.
        :type: list[ExpressionResource]
        """

        self._args = args

    @property
    def op(self):
        """
        Gets the op of this IntegerOperationResource.

        :return: The op of this IntegerOperationResource.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """
        Sets the op of this IntegerOperationResource.

        :param op: The op of this IntegerOperationResource.
        :type: str
        """

        self._op = op

    @property
    def type(self):
        """
        Gets the type of this IntegerOperationResource.

        :return: The type of this IntegerOperationResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IntegerOperationResource.

        :param type: The type of this IntegerOperationResource.
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
        if not isinstance(other, IntegerOperationResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
