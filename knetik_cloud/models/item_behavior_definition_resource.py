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


class ItemBehaviorDefinitionResource(object):
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
        'behavior': 'Behavior',
        'modifiable': 'bool',
        'required': 'bool'
    }

    attribute_map = {
        'behavior': 'behavior',
        'modifiable': 'modifiable',
        'required': 'required'
    }

    def __init__(self, behavior=None, modifiable=None, required=None):
        """
        ItemBehaviorDefinitionResource - a model defined in Swagger
        """

        self._behavior = None
        self._modifiable = None
        self._required = None
        self.discriminator = None

        self.behavior = behavior
        self.modifiable = modifiable
        self.required = required

    @property
    def behavior(self):
        """
        Gets the behavior of this ItemBehaviorDefinitionResource.
        The default version of the behavior

        :return: The behavior of this ItemBehaviorDefinitionResource.
        :rtype: Behavior
        """
        return self._behavior

    @behavior.setter
    def behavior(self, behavior):
        """
        Sets the behavior of this ItemBehaviorDefinitionResource.
        The default version of the behavior

        :param behavior: The behavior of this ItemBehaviorDefinitionResource.
        :type: Behavior
        """
        if behavior is None:
            raise ValueError("Invalid value for `behavior`, must not be `None`")

        self._behavior = behavior

    @property
    def modifiable(self):
        """
        Gets the modifiable of this ItemBehaviorDefinitionResource.
        Whether the behavior's values can be modified

        :return: The modifiable of this ItemBehaviorDefinitionResource.
        :rtype: bool
        """
        return self._modifiable

    @modifiable.setter
    def modifiable(self, modifiable):
        """
        Sets the modifiable of this ItemBehaviorDefinitionResource.
        Whether the behavior's values can be modified

        :param modifiable: The modifiable of this ItemBehaviorDefinitionResource.
        :type: bool
        """
        if modifiable is None:
            raise ValueError("Invalid value for `modifiable`, must not be `None`")

        self._modifiable = modifiable

    @property
    def required(self):
        """
        Gets the required of this ItemBehaviorDefinitionResource.
        Whether the behavior can be removed

        :return: The required of this ItemBehaviorDefinitionResource.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this ItemBehaviorDefinitionResource.
        Whether the behavior can be removed

        :param required: The required of this ItemBehaviorDefinitionResource.
        :type: bool
        """
        if required is None:
            raise ValueError("Invalid value for `required`, must not be `None`")

        self._required = required

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
        if not isinstance(other, ItemBehaviorDefinitionResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
