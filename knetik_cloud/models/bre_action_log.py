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


class BreActionLog(object):
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
        'name': 'str',
        'runtime': 'int',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'runtime': 'runtime',
        'status': 'status'
    }

    def __init__(self, name=None, runtime=None, status=None):
        """
        BreActionLog - a model defined in Swagger
        """

        self._name = None
        self._runtime = None
        self._status = None
        self.discriminator = None

        if name is not None:
          self.name = name
        if runtime is not None:
          self.runtime = runtime
        if status is not None:
          self.status = status

    @property
    def name(self):
        """
        Gets the name of this BreActionLog.
        The name of the action

        :return: The name of this BreActionLog.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BreActionLog.
        The name of the action

        :param name: The name of this BreActionLog.
        :type: str
        """

        self._name = name

    @property
    def runtime(self):
        """
        Gets the runtime of this BreActionLog.
        The runtime of the action in milliseconds

        :return: The runtime of this BreActionLog.
        :rtype: int
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """
        Sets the runtime of this BreActionLog.
        The runtime of the action in milliseconds

        :param runtime: The runtime of this BreActionLog.
        :type: int
        """

        self._runtime = runtime

    @property
    def status(self):
        """
        Gets the status of this BreActionLog.
        The status of the action (ran, failed)

        :return: The status of this BreActionLog.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BreActionLog.
        The status of the action (ran, failed)

        :param status: The status of this BreActionLog.
        :type: str
        """

        self._status = status

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
        if not isinstance(other, BreActionLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
