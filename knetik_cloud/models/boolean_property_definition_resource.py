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


class BooleanPropertyDefinitionResource(object):
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
        'field_list': 'PropertyFieldListResource',
        'name': 'str',
        'required': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'field_list': 'field_list',
        'name': 'name',
        'required': 'required',
        'type': 'type'
    }

    def __init__(self, field_list=None, name=None, required=None, type=None):
        """
        BooleanPropertyDefinitionResource - a model defined in Swagger
        """

        self._field_list = None
        self._name = None
        self._required = None
        self._type = None

        if field_list is not None:
          self.field_list = field_list
        self.name = name
        self.required = required
        self.type = type

    @property
    def field_list(self):
        """
        Gets the field_list of this BooleanPropertyDefinitionResource.
        A list of the fields on both the property definition and property of this type

        :return: The field_list of this BooleanPropertyDefinitionResource.
        :rtype: PropertyFieldListResource
        """
        return self._field_list

    @field_list.setter
    def field_list(self, field_list):
        """
        Sets the field_list of this BooleanPropertyDefinitionResource.
        A list of the fields on both the property definition and property of this type

        :param field_list: The field_list of this BooleanPropertyDefinitionResource.
        :type: PropertyFieldListResource
        """

        self._field_list = field_list

    @property
    def name(self):
        """
        Gets the name of this BooleanPropertyDefinitionResource.
        The name of the property

        :return: The name of this BooleanPropertyDefinitionResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BooleanPropertyDefinitionResource.
        The name of the property

        :param name: The name of this BooleanPropertyDefinitionResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def required(self):
        """
        Gets the required of this BooleanPropertyDefinitionResource.
        Whether the property is required

        :return: The required of this BooleanPropertyDefinitionResource.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this BooleanPropertyDefinitionResource.
        Whether the property is required

        :param required: The required of this BooleanPropertyDefinitionResource.
        :type: bool
        """
        if required is None:
            raise ValueError("Invalid value for `required`, must not be `None`")

        self._required = required

    @property
    def type(self):
        """
        Gets the type of this BooleanPropertyDefinitionResource.
        The type of the property. Used for polymorphic type recognition and thus must match an expected type with additional properties.

        :return: The type of this BooleanPropertyDefinitionResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BooleanPropertyDefinitionResource.
        The type of the property. Used for polymorphic type recognition and thus must match an expected type with additional properties.

        :param type: The type of this BooleanPropertyDefinitionResource.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

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
        if not isinstance(other, BooleanPropertyDefinitionResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
