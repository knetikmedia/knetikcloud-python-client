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


class PredicateOperation(object):
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
        'args': 'list[Expressionobject]',
        'operator': 'Operator'
    }

    attribute_map = {
        'args': 'args',
        'operator': 'operator'
    }

    def __init__(self, args=None, operator=None):
        """
        PredicateOperation - a model defined in Swagger
        """

        self._args = None
        self._operator = None
        self.discriminator = None

        if args is not None:
          self.args = args
        if operator is not None:
          self.operator = operator

    @property
    def args(self):
        """
        Gets the args of this PredicateOperation.

        :return: The args of this PredicateOperation.
        :rtype: list[Expressionobject]
        """
        return self._args

    @args.setter
    def args(self, args):
        """
        Sets the args of this PredicateOperation.

        :param args: The args of this PredicateOperation.
        :type: list[Expressionobject]
        """

        self._args = args

    @property
    def operator(self):
        """
        Gets the operator of this PredicateOperation.

        :return: The operator of this PredicateOperation.
        :rtype: Operator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this PredicateOperation.

        :param operator: The operator of this PredicateOperation.
        :type: Operator
        """

        self._operator = operator

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
        if not isinstance(other, PredicateOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
