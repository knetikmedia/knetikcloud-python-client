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


class CountryResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, iso2=None, iso3=None, name=None):
        """
        CountryResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'iso2': 'str',
            'iso3': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'iso2': 'iso2',
            'iso3': 'iso3',
            'name': 'name'
        }

        self._iso2 = iso2
        self._iso3 = iso3
        self._name = name

    @property
    def iso2(self):
        """
        Gets the iso2 of this CountryResource.
        The iso2 of the country

        :return: The iso2 of this CountryResource.
        :rtype: str
        """
        return self._iso2

    @iso2.setter
    def iso2(self, iso2):
        """
        Sets the iso2 of this CountryResource.
        The iso2 of the country

        :param iso2: The iso2 of this CountryResource.
        :type: str
        """

        self._iso2 = iso2

    @property
    def iso3(self):
        """
        Gets the iso3 of this CountryResource.
        The iso3 of the country

        :return: The iso3 of this CountryResource.
        :rtype: str
        """
        return self._iso3

    @iso3.setter
    def iso3(self, iso3):
        """
        Sets the iso3 of this CountryResource.
        The iso3 of the country

        :param iso3: The iso3 of this CountryResource.
        :type: str
        """

        self._iso3 = iso3

    @property
    def name(self):
        """
        Gets the name of this CountryResource.
        The name of the country resource

        :return: The name of this CountryResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CountryResource.
        The name of the country resource

        :param name: The name of this CountryResource.
        :type: str
        """

        self._name = name

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
