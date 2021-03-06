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


class Country(object):
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
        'id': 'int',
        'iso2': 'str',
        'iso3': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'iso2': 'iso2',
        'iso3': 'iso3',
        'name': 'name'
    }

    def __init__(self, id=None, iso2=None, iso3=None, name=None):
        """
        Country - a model defined in Swagger
        """

        self._id = None
        self._iso2 = None
        self._iso3 = None
        self._name = None
        self.discriminator = None

        if id is not None:
          self.id = id
        if iso2 is not None:
          self.iso2 = iso2
        if iso3 is not None:
          self.iso3 = iso3
        if name is not None:
          self.name = name

    @property
    def id(self):
        """
        Gets the id of this Country.

        :return: The id of this Country.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Country.

        :param id: The id of this Country.
        :type: int
        """

        self._id = id

    @property
    def iso2(self):
        """
        Gets the iso2 of this Country.

        :return: The iso2 of this Country.
        :rtype: str
        """
        return self._iso2

    @iso2.setter
    def iso2(self, iso2):
        """
        Sets the iso2 of this Country.

        :param iso2: The iso2 of this Country.
        :type: str
        """

        self._iso2 = iso2

    @property
    def iso3(self):
        """
        Gets the iso3 of this Country.

        :return: The iso3 of this Country.
        :rtype: str
        """
        return self._iso3

    @iso3.setter
    def iso3(self, iso3):
        """
        Sets the iso3 of this Country.

        :param iso3: The iso3 of this Country.
        :type: str
        """

        self._iso3 = iso3

    @property
    def name(self):
        """
        Gets the name of this Country.

        :return: The name of this Country.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Country.

        :param name: The name of this Country.
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
        if not isinstance(other, Country):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
