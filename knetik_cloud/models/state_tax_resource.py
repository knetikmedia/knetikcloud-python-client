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


class StateTaxResource(object):
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
        'country_iso3': 'str',
        'federally_exempt': 'bool',
        'name': 'str',
        'rate': 'float',
        'state_code': 'str',
        'tax_shipping': 'bool'
    }

    attribute_map = {
        'country_iso3': 'country_iso3',
        'federally_exempt': 'federally_exempt',
        'name': 'name',
        'rate': 'rate',
        'state_code': 'state_code',
        'tax_shipping': 'tax_shipping'
    }

    def __init__(self, country_iso3=None, federally_exempt=None, name=None, rate=None, state_code=None, tax_shipping=None):
        """
        StateTaxResource - a model defined in Swagger
        """

        self._country_iso3 = None
        self._federally_exempt = None
        self._name = None
        self._rate = None
        self._state_code = None
        self._tax_shipping = None

        self.country_iso3 = country_iso3
        self.federally_exempt = federally_exempt
        self.name = name
        self.rate = rate
        self.state_code = state_code
        self.tax_shipping = tax_shipping

    @property
    def country_iso3(self):
        """
        Gets the country_iso3 of this StateTaxResource.
        The iso3 code of the country, cannot be changed

        :return: The country_iso3 of this StateTaxResource.
        :rtype: str
        """
        return self._country_iso3

    @country_iso3.setter
    def country_iso3(self, country_iso3):
        """
        Sets the country_iso3 of this StateTaxResource.
        The iso3 code of the country, cannot be changed

        :param country_iso3: The country_iso3 of this StateTaxResource.
        :type: str
        """
        if country_iso3 is None:
            raise ValueError("Invalid value for `country_iso3`, must not be `None`")

        self._country_iso3 = country_iso3

    @property
    def federally_exempt(self):
        """
        Gets the federally_exempt of this StateTaxResource.
        Whether the state is exempt from paying the country tax

        :return: The federally_exempt of this StateTaxResource.
        :rtype: bool
        """
        return self._federally_exempt

    @federally_exempt.setter
    def federally_exempt(self, federally_exempt):
        """
        Sets the federally_exempt of this StateTaxResource.
        Whether the state is exempt from paying the country tax

        :param federally_exempt: The federally_exempt of this StateTaxResource.
        :type: bool
        """
        if federally_exempt is None:
            raise ValueError("Invalid value for `federally_exempt`, must not be `None`")

        self._federally_exempt = federally_exempt

    @property
    def name(self):
        """
        Gets the name of this StateTaxResource.
        The name of the tax

        :return: The name of this StateTaxResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StateTaxResource.
        The name of the tax

        :param name: The name of this StateTaxResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def rate(self):
        """
        Gets the rate of this StateTaxResource.
        The tax rate as a percentage to a maximum of two decimal places (1.5 means 1.5%)

        :return: The rate of this StateTaxResource.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this StateTaxResource.
        The tax rate as a percentage to a maximum of two decimal places (1.5 means 1.5%)

        :param rate: The rate of this StateTaxResource.
        :type: float
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")

        self._rate = rate

    @property
    def state_code(self):
        """
        Gets the state_code of this StateTaxResource.
        The code of the state, cannot be changed

        :return: The state_code of this StateTaxResource.
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """
        Sets the state_code of this StateTaxResource.
        The code of the state, cannot be changed

        :param state_code: The state_code of this StateTaxResource.
        :type: str
        """
        if state_code is None:
            raise ValueError("Invalid value for `state_code`, must not be `None`")

        self._state_code = state_code

    @property
    def tax_shipping(self):
        """
        Gets the tax_shipping of this StateTaxResource.
        Whether the tax applies to shipping costs

        :return: The tax_shipping of this StateTaxResource.
        :rtype: bool
        """
        return self._tax_shipping

    @tax_shipping.setter
    def tax_shipping(self, tax_shipping):
        """
        Sets the tax_shipping of this StateTaxResource.
        Whether the tax applies to shipping costs

        :param tax_shipping: The tax_shipping of this StateTaxResource.
        :type: bool
        """
        if tax_shipping is None:
            raise ValueError("Invalid value for `tax_shipping`, must not be `None`")

        self._tax_shipping = tax_shipping

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
        if not isinstance(other, StateTaxResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
