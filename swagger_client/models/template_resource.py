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


class TemplateResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created_date=None, id=None, name=None, properties=None, updated_date=None):
        """
        TemplateResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created_date': 'int',
            'id': 'str',
            'name': 'str',
            'properties': 'list[PropertyDefinitionResource]',
            'updated_date': 'int'
        }

        self.attribute_map = {
            'created_date': 'created_date',
            'id': 'id',
            'name': 'name',
            'properties': 'properties',
            'updated_date': 'updated_date'
        }

        self._created_date = created_date
        self._id = id
        self._name = name
        self._properties = properties
        self._updated_date = updated_date

    @property
    def created_date(self):
        """
        Gets the created_date of this TemplateResource.
        The date/time this resource was created in seconds since unix epoch

        :return: The created_date of this TemplateResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this TemplateResource.
        The date/time this resource was created in seconds since unix epoch

        :param created_date: The created_date of this TemplateResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def id(self):
        """
        Gets the id of this TemplateResource.
        The id of the template

        :return: The id of this TemplateResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TemplateResource.
        The id of the template

        :param id: The id of this TemplateResource.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this TemplateResource.
        The name of the template

        :return: The name of this TemplateResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TemplateResource.
        The name of the template

        :param name: The name of this TemplateResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def properties(self):
        """
        Gets the properties of this TemplateResource.
        The customized properties that are present

        :return: The properties of this TemplateResource.
        :rtype: list[PropertyDefinitionResource]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this TemplateResource.
        The customized properties that are present

        :param properties: The properties of this TemplateResource.
        :type: list[PropertyDefinitionResource]
        """

        self._properties = properties

    @property
    def updated_date(self):
        """
        Gets the updated_date of this TemplateResource.
        The date/time this resource was last updated in seconds since unix epoch

        :return: The updated_date of this TemplateResource.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this TemplateResource.
        The date/time this resource was last updated in seconds since unix epoch

        :param updated_date: The updated_date of this TemplateResource.
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
        if not isinstance(other, TemplateResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
