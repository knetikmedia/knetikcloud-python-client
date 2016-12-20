# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BreRuleLog(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ran=None, reason=None, rule_end_date=None, rule_id=None, rule_name=None, rule_start_date=None):
        """
        BreRuleLog - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ran': 'bool',
            'reason': 'str',
            'rule_end_date': 'int',
            'rule_id': 'str',
            'rule_name': 'str',
            'rule_start_date': 'int'
        }

        self.attribute_map = {
            'ran': 'ran',
            'reason': 'reason',
            'rule_end_date': 'rule_end_date',
            'rule_id': 'rule_id',
            'rule_name': 'rule_name',
            'rule_start_date': 'rule_start_date'
        }

        self._ran = ran
        self._reason = reason
        self._rule_end_date = rule_end_date
        self._rule_id = rule_id
        self._rule_name = rule_name
        self._rule_start_date = rule_start_date

    @property
    def ran(self):
        """
        Gets the ran of this BreRuleLog.
        Whether the rule ran

        :return: The ran of this BreRuleLog.
        :rtype: bool
        """
        return self._ran

    @ran.setter
    def ran(self, ran):
        """
        Sets the ran of this BreRuleLog.
        Whether the rule ran

        :param ran: The ran of this BreRuleLog.
        :type: bool
        """

        self._ran = ran

    @property
    def reason(self):
        """
        Gets the reason of this BreRuleLog.
        The reason for the rule

        :return: The reason of this BreRuleLog.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this BreRuleLog.
        The reason for the rule

        :param reason: The reason of this BreRuleLog.
        :type: str
        """

        self._reason = reason

    @property
    def rule_end_date(self):
        """
        Gets the rule_end_date of this BreRuleLog.
        The end date of the rule in seconds

        :return: The rule_end_date of this BreRuleLog.
        :rtype: int
        """
        return self._rule_end_date

    @rule_end_date.setter
    def rule_end_date(self, rule_end_date):
        """
        Sets the rule_end_date of this BreRuleLog.
        The end date of the rule in seconds

        :param rule_end_date: The rule_end_date of this BreRuleLog.
        :type: int
        """

        self._rule_end_date = rule_end_date

    @property
    def rule_id(self):
        """
        Gets the rule_id of this BreRuleLog.
        The id of the rule

        :return: The rule_id of this BreRuleLog.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """
        Sets the rule_id of this BreRuleLog.
        The id of the rule

        :param rule_id: The rule_id of this BreRuleLog.
        :type: str
        """

        self._rule_id = rule_id

    @property
    def rule_name(self):
        """
        Gets the rule_name of this BreRuleLog.
        The name of the rule

        :return: The rule_name of this BreRuleLog.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """
        Sets the rule_name of this BreRuleLog.
        The name of the rule

        :param rule_name: The rule_name of this BreRuleLog.
        :type: str
        """

        self._rule_name = rule_name

    @property
    def rule_start_date(self):
        """
        Gets the rule_start_date of this BreRuleLog.
        The start date of the rule in seconds

        :return: The rule_start_date of this BreRuleLog.
        :rtype: int
        """
        return self._rule_start_date

    @rule_start_date.setter
    def rule_start_date(self, rule_start_date):
        """
        Sets the rule_start_date of this BreRuleLog.
        The start date of the rule in seconds

        :param rule_start_date: The rule_start_date of this BreRuleLog.
        :type: int
        """

        self._rule_start_date = rule_start_date

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