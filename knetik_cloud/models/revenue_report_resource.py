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


class RevenueReportResource(object):
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
        'customer_count': 'int',
        'sale_count': 'int',
        'sales_average': 'float',
        'sales_total': 'float'
    }

    attribute_map = {
        'customer_count': 'customer_count',
        'sale_count': 'sale_count',
        'sales_average': 'sales_average',
        'sales_total': 'sales_total'
    }

    def __init__(self, customer_count=None, sale_count=None, sales_average=None, sales_total=None):
        """
        RevenueReportResource - a model defined in Swagger
        """

        self._customer_count = None
        self._sale_count = None
        self._sales_average = None
        self._sales_total = None
        self.discriminator = None

        if customer_count is not None:
          self.customer_count = customer_count
        if sale_count is not None:
          self.sale_count = sale_count
        if sales_average is not None:
          self.sales_average = sales_average
        if sales_total is not None:
          self.sales_total = sales_total

    @property
    def customer_count(self):
        """
        Gets the customer_count of this RevenueReportResource.

        :return: The customer_count of this RevenueReportResource.
        :rtype: int
        """
        return self._customer_count

    @customer_count.setter
    def customer_count(self, customer_count):
        """
        Sets the customer_count of this RevenueReportResource.

        :param customer_count: The customer_count of this RevenueReportResource.
        :type: int
        """

        self._customer_count = customer_count

    @property
    def sale_count(self):
        """
        Gets the sale_count of this RevenueReportResource.

        :return: The sale_count of this RevenueReportResource.
        :rtype: int
        """
        return self._sale_count

    @sale_count.setter
    def sale_count(self, sale_count):
        """
        Sets the sale_count of this RevenueReportResource.

        :param sale_count: The sale_count of this RevenueReportResource.
        :type: int
        """

        self._sale_count = sale_count

    @property
    def sales_average(self):
        """
        Gets the sales_average of this RevenueReportResource.

        :return: The sales_average of this RevenueReportResource.
        :rtype: float
        """
        return self._sales_average

    @sales_average.setter
    def sales_average(self, sales_average):
        """
        Sets the sales_average of this RevenueReportResource.

        :param sales_average: The sales_average of this RevenueReportResource.
        :type: float
        """

        self._sales_average = sales_average

    @property
    def sales_total(self):
        """
        Gets the sales_total of this RevenueReportResource.

        :return: The sales_total of this RevenueReportResource.
        :rtype: float
        """
        return self._sales_total

    @sales_total.setter
    def sales_total(self, sales_total):
        """
        Sets the sales_total of this RevenueReportResource.

        :param sales_total: The sales_total of this RevenueReportResource.
        :type: float
        """

        self._sales_total = sales_total

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
        if not isinstance(other, RevenueReportResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
