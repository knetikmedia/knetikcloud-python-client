# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BreGlobalResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, description=None, id=None, key=None, name=None, scopes=None, system_global=None, type=None):
        """
        BreGlobalResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'id': 'str',
            'key': 'str',
            'name': 'str',
            'scopes': 'list[BreGlobalScopeDefinition]',
            'system_global': 'bool',
            'type': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'id': 'id',
            'key': 'key',
            'name': 'name',
            'scopes': 'scopes',
            'system_global': 'system_global',
            'type': 'type'
        }

        self._description = description
        self._id = id
        self._key = key
        self._name = name
        self._scopes = scopes
        self._system_global = system_global
        self._type = type

    @property
    def description(self):
        """
        Gets the description of this BreGlobalResource.
        A human readable description for display in admin pages

        :return: The description of this BreGlobalResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BreGlobalResource.
        A human readable description for display in admin pages

        :param description: The description of this BreGlobalResource.
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """
        Gets the id of this BreGlobalResource.
        The id of the global definition. Default is a random guid. Cannot be updated

        :return: The id of this BreGlobalResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BreGlobalResource.
        The id of the global definition. Default is a random guid. Cannot be updated

        :param id: The id of this BreGlobalResource.
        :type: str
        """

        self._id = id

    @property
    def key(self):
        """
        Gets the key of this BreGlobalResource.
        The key for the global. Must be unique when combined with scope names. Usually a single descriptive word like 'purchases' or 'logins'

        :return: The key of this BreGlobalResource.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this BreGlobalResource.
        The key for the global. Must be unique when combined with scope names. Usually a single descriptive word like 'purchases' or 'logins'

        :param key: The key of this BreGlobalResource.
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def name(self):
        """
        Gets the name of this BreGlobalResource.
        A human readable name for display in admin pages

        :return: The name of this BreGlobalResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BreGlobalResource.
        A human readable name for display in admin pages

        :param name: The name of this BreGlobalResource.
        :type: str
        """

        self._name = name

    @property
    def scopes(self):
        """
        Gets the scopes of this BreGlobalResource.
        A list of scoping parameters. Allows the global to have a different value in different context such as a count of purchases for each user (by putting a 'user' scope in this list). When using this global in a rule these scopes will need to be mapped with an expression to provide a value, similar to the parameters in an action

        :return: The scopes of this BreGlobalResource.
        :rtype: list[BreGlobalScopeDefinition]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this BreGlobalResource.
        A list of scoping parameters. Allows the global to have a different value in different context such as a count of purchases for each user (by putting a 'user' scope in this list). When using this global in a rule these scopes will need to be mapped with an expression to provide a value, similar to the parameters in an action

        :param scopes: The scopes of this BreGlobalResource.
        :type: list[BreGlobalScopeDefinition]
        """

        self._scopes = scopes

    @property
    def system_global(self):
        """
        Gets the system_global of this BreGlobalResource.
        Where this global came from. System globals cannot be removed or updated

        :return: The system_global of this BreGlobalResource.
        :rtype: bool
        """
        return self._system_global

    @system_global.setter
    def system_global(self, system_global):
        """
        Sets the system_global of this BreGlobalResource.
        Where this global came from. System globals cannot be removed or updated

        :param system_global: The system_global of this BreGlobalResource.
        :type: bool
        """

        self._system_global = system_global

    @property
    def type(self):
        """
        Gets the type of this BreGlobalResource.
        The variable type the global stores. See the See Bre Variables enpoint for list

        :return: The type of this BreGlobalResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BreGlobalResource.
        The variable type the global stores. See the See Bre Variables enpoint for list

        :param type: The type of this BreGlobalResource.
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
        if not isinstance(other, BreGlobalResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other