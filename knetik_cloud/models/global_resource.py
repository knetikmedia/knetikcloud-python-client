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


class GlobalResource(object):
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
        'definition': 'str',
        'global_def_id': 'str',
        'scopes': 'dict(str, ExpressionResource)',
        'type': 'str'
    }

    attribute_map = {
        'definition': 'definition',
        'global_def_id': 'global_def_id',
        'scopes': 'scopes',
        'type': 'type'
    }

    def __init__(self, definition=None, global_def_id=None, scopes=None, type=None):
        """
        GlobalResource - a model defined in Swagger
        """

        self._definition = None
        self._global_def_id = None
        self._scopes = None
        self._type = None
        self.discriminator = None

        if definition is not None:
          self.definition = definition
        if global_def_id is not None:
          self.global_def_id = global_def_id
        if scopes is not None:
          self.scopes = scopes
        if type is not None:
          self.type = type

    @property
    def definition(self):
        """
        Gets the definition of this GlobalResource.

        :return: The definition of this GlobalResource.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """
        Sets the definition of this GlobalResource.

        :param definition: The definition of this GlobalResource.
        :type: str
        """

        self._definition = definition

    @property
    def global_def_id(self):
        """
        Gets the global_def_id of this GlobalResource.

        :return: The global_def_id of this GlobalResource.
        :rtype: str
        """
        return self._global_def_id

    @global_def_id.setter
    def global_def_id(self, global_def_id):
        """
        Sets the global_def_id of this GlobalResource.

        :param global_def_id: The global_def_id of this GlobalResource.
        :type: str
        """

        self._global_def_id = global_def_id

    @property
    def scopes(self):
        """
        Gets the scopes of this GlobalResource.

        :return: The scopes of this GlobalResource.
        :rtype: dict(str, ExpressionResource)
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this GlobalResource.

        :param scopes: The scopes of this GlobalResource.
        :type: dict(str, ExpressionResource)
        """

        self._scopes = scopes

    @property
    def type(self):
        """
        Gets the type of this GlobalResource.

        :return: The type of this GlobalResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GlobalResource.

        :param type: The type of this GlobalResource.
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
        if not isinstance(other, GlobalResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
