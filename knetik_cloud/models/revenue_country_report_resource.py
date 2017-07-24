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


class RevenueCountryReportResource(object):
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
        'country': 'str',
        'revenue': 'float',
        'volume': 'int'
    }

    attribute_map = {
        'country': 'country',
        'revenue': 'revenue',
        'volume': 'volume'
    }

    def __init__(self, country=None, revenue=None, volume=None):
        """
        RevenueCountryReportResource - a model defined in Swagger
        """

        self._country = None
        self._revenue = None
        self._volume = None

        if country is not None:
          self.country = country
        if revenue is not None:
          self.revenue = revenue
        if volume is not None:
          self.volume = volume

    @property
    def country(self):
        """
        Gets the country of this RevenueCountryReportResource.

        :return: The country of this RevenueCountryReportResource.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this RevenueCountryReportResource.

        :param country: The country of this RevenueCountryReportResource.
        :type: str
        """

        self._country = country

    @property
    def revenue(self):
        """
        Gets the revenue of this RevenueCountryReportResource.

        :return: The revenue of this RevenueCountryReportResource.
        :rtype: float
        """
        return self._revenue

    @revenue.setter
    def revenue(self, revenue):
        """
        Sets the revenue of this RevenueCountryReportResource.

        :param revenue: The revenue of this RevenueCountryReportResource.
        :type: float
        """

        self._revenue = revenue

    @property
    def volume(self):
        """
        Gets the volume of this RevenueCountryReportResource.

        :return: The volume of this RevenueCountryReportResource.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """
        Sets the volume of this RevenueCountryReportResource.

        :param volume: The volume of this RevenueCountryReportResource.
        :type: int
        """

        self._volume = volume

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
        if not isinstance(other, RevenueCountryReportResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
