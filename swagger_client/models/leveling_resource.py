# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LevelingResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, additional_properties=None, created_date=None, description=None, name=None, tiers=None, updated_date=None):
        """
        LevelingResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'additional_properties': 'dict(str, ModelProperty)',
            'created_date': 'int',
            'description': 'str',
            'name': 'str',
            'tiers': 'list[TierResource]',
            'updated_date': 'int'
        }

        self.attribute_map = {
            'additional_properties': 'additional_properties',
            'created_date': 'created_date',
            'description': 'description',
            'name': 'name',
            'tiers': 'tiers',
            'updated_date': 'updated_date'
        }

        self._additional_properties = additional_properties
        self._created_date = created_date
        self._description = description
        self._name = name
        self._tiers = tiers
        self._updated_date = updated_date

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this LevelingResource.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type

        :return: The additional_properties of this LevelingResource.
        :rtype: dict(str, ModelProperty)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this LevelingResource.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type

        :param additional_properties: The additional_properties of this LevelingResource.
        :type: dict(str, ModelProperty)
        """

        self._additional_properties = additional_properties

    @property
    def created_date(self):
        """
        Gets the created_date of this LevelingResource.
        The date the leveling schema was created

        :return: The created_date of this LevelingResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this LevelingResource.
        The date the leveling schema was created

        :param created_date: The created_date of this LevelingResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def description(self):
        """
        Gets the description of this LevelingResource.
        The description of the leveling schema

        :return: The description of this LevelingResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LevelingResource.
        The description of the leveling schema

        :param description: The description of this LevelingResource.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this LevelingResource.
        The name of the leveling schema.  IMMUTABLE

        :return: The name of this LevelingResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LevelingResource.
        The name of the leveling schema.  IMMUTABLE

        :param name: The name of this LevelingResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def tiers(self):
        """
        Gets the tiers of this LevelingResource.
        A set of tiers that contain experience boundaries

        :return: The tiers of this LevelingResource.
        :rtype: list[TierResource]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """
        Sets the tiers of this LevelingResource.
        A set of tiers that contain experience boundaries

        :param tiers: The tiers of this LevelingResource.
        :type: list[TierResource]
        """

        self._tiers = tiers

    @property
    def updated_date(self):
        """
        Gets the updated_date of this LevelingResource.
        The date the leveling schema was updated

        :return: The updated_date of this LevelingResource.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this LevelingResource.
        The date the leveling schema was updated

        :param updated_date: The updated_date of this LevelingResource.
        :type: int
        """

        self._updated_date = updated_date

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
