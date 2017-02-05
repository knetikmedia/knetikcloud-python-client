# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ActionResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, category=None, description=None, name=None, variables=None):
        """
        ActionResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category': 'str',
            'description': 'str',
            'name': 'str',
            'variables': 'list[ActionVariableResource]'
        }

        self.attribute_map = {
            'category': 'category',
            'description': 'description',
            'name': 'name',
            'variables': 'variables'
        }

        self._category = category
        self._description = description
        self._name = name
        self._variables = variables

    @property
    def category(self):
        """
        Gets the category of this ActionResource.
        The category the action is in. All customer specific actions are in the 'custom' category

        :return: The category of this ActionResource.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this ActionResource.
        The category the action is in. All customer specific actions are in the 'custom' category

        :param category: The category of this ActionResource.
        :type: str
        """
        allowed_values = ["achievement", "behavior", "comment", "disposition", "entitlement", "friends", "fulfillment", "gamification", "inventory", "invoice", "media", "scheduler", "store", "subscription", "user", "wallet", "custom", "challenge", "activity", "campaign", "event"]
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def description(self):
        """
        Gets the description of this ActionResource.
        The description of the action

        :return: The description of this ActionResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ActionResource.
        The description of the action

        :param description: The description of this ActionResource.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this ActionResource.
        The name of the action. Used as the unique id for reference

        :return: The name of this ActionResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ActionResource.
        The name of the action. Used as the unique id for reference

        :param name: The name of this ActionResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def variables(self):
        """
        Gets the variables of this ActionResource.
        The variables required for the action

        :return: The variables of this ActionResource.
        :rtype: list[ActionVariableResource]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this ActionResource.
        The variables required for the action

        :param variables: The variables of this ActionResource.
        :type: list[ActionVariableResource]
        """
        if variables is None:
            raise ValueError("Invalid value for `variables`, must not be `None`")

        self._variables = variables

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
        if not isinstance(other, ActionResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
