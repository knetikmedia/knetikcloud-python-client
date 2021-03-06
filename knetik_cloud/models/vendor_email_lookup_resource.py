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


class VendorEmailLookupResource(object):
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
        'lookup_key': 'ExpressionResource',
        'required_key_type': 'str',
        'type': 'str',
        'value_type': 'str'
    }

    attribute_map = {
        'definition': 'definition',
        'lookup_key': 'lookup_key',
        'required_key_type': 'required_key_type',
        'type': 'type',
        'value_type': 'value_type'
    }

    def __init__(self, definition=None, lookup_key=None, required_key_type=None, type=None, value_type=None):
        """
        VendorEmailLookupResource - a model defined in Swagger
        """

        self._definition = None
        self._lookup_key = None
        self._required_key_type = None
        self._type = None
        self._value_type = None
        self.discriminator = None

        if definition is not None:
          self.definition = definition
        if lookup_key is not None:
          self.lookup_key = lookup_key
        if required_key_type is not None:
          self.required_key_type = required_key_type
        if type is not None:
          self.type = type
        if value_type is not None:
          self.value_type = value_type

    @property
    def definition(self):
        """
        Gets the definition of this VendorEmailLookupResource.

        :return: The definition of this VendorEmailLookupResource.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """
        Sets the definition of this VendorEmailLookupResource.

        :param definition: The definition of this VendorEmailLookupResource.
        :type: str
        """

        self._definition = definition

    @property
    def lookup_key(self):
        """
        Gets the lookup_key of this VendorEmailLookupResource.

        :return: The lookup_key of this VendorEmailLookupResource.
        :rtype: ExpressionResource
        """
        return self._lookup_key

    @lookup_key.setter
    def lookup_key(self, lookup_key):
        """
        Sets the lookup_key of this VendorEmailLookupResource.

        :param lookup_key: The lookup_key of this VendorEmailLookupResource.
        :type: ExpressionResource
        """

        self._lookup_key = lookup_key

    @property
    def required_key_type(self):
        """
        Gets the required_key_type of this VendorEmailLookupResource.

        :return: The required_key_type of this VendorEmailLookupResource.
        :rtype: str
        """
        return self._required_key_type

    @required_key_type.setter
    def required_key_type(self, required_key_type):
        """
        Sets the required_key_type of this VendorEmailLookupResource.

        :param required_key_type: The required_key_type of this VendorEmailLookupResource.
        :type: str
        """

        self._required_key_type = required_key_type

    @property
    def type(self):
        """
        Gets the type of this VendorEmailLookupResource.

        :return: The type of this VendorEmailLookupResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VendorEmailLookupResource.

        :param type: The type of this VendorEmailLookupResource.
        :type: str
        """

        self._type = type

    @property
    def value_type(self):
        """
        Gets the value_type of this VendorEmailLookupResource.

        :return: The value_type of this VendorEmailLookupResource.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """
        Sets the value_type of this VendorEmailLookupResource.

        :param value_type: The value_type of this VendorEmailLookupResource.
        :type: str
        """

        self._value_type = value_type

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
        if not isinstance(other, VendorEmailLookupResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
