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


class BreCategoryResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, additional_properties=None, name=None, template=None):
        """
        BreCategoryResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'additional_properties': 'dict(str, ModelProperty)',
            'name': 'str',
            'template': 'str'
        }

        self.attribute_map = {
            'additional_properties': 'additional_properties',
            'name': 'name',
            'template': 'template'
        }

        self._additional_properties = additional_properties
        self._name = name
        self._template = template

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this BreCategoryResource.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type

        :return: The additional_properties of this BreCategoryResource.
        :rtype: dict(str, ModelProperty)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this BreCategoryResource.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type

        :param additional_properties: The additional_properties of this BreCategoryResource.
        :type: dict(str, ModelProperty)
        """

        self._additional_properties = additional_properties

    @property
    def name(self):
        """
        Gets the name of this BreCategoryResource.
        The name of the category. Serves as the unique id

        :return: The name of this BreCategoryResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BreCategoryResource.
        The name of the category. Serves as the unique id

        :param name: The name of this BreCategoryResource.
        :type: str
        """

        self._name = name

    @property
    def template(self):
        """
        Gets the template of this BreCategoryResource.
        A template this BRE category is validated against (private). May be null and no validation of additional_properties will be done

        :return: The template of this BreCategoryResource.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this BreCategoryResource.
        A template this BRE category is validated against (private). May be null and no validation of additional_properties will be done

        :param template: The template of this BreCategoryResource.
        :type: str
        """

        self._template = template

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
        if not isinstance(other, BreCategoryResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
