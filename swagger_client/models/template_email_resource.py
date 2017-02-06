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


class TemplateEmailResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _from=None, recipients=None, template_key=None, template_vars=None):
        """
        TemplateEmailResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_from': 'str',
            'recipients': 'list[int]',
            'template_key': 'str',
            'template_vars': 'list[KeyValuePairstringstring]'
        }

        self.attribute_map = {
            '_from': 'from',
            'recipients': 'recipients',
            'template_key': 'template_key',
            'template_vars': 'template_vars'
        }

        self.__from = _from
        self._recipients = recipients
        self._template_key = template_key
        self._template_vars = template_vars

    @property
    def _from(self):
        """
        Gets the _from of this TemplateEmailResource.
        Address to attribute the outgoing message to. Optional if the config email.out_address is set.

        :return: The _from of this TemplateEmailResource.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this TemplateEmailResource.
        Address to attribute the outgoing message to. Optional if the config email.out_address is set.

        :param _from: The _from of this TemplateEmailResource.
        :type: str
        """

        self.__from = _from

    @property
    def recipients(self):
        """
        Gets the recipients of this TemplateEmailResource.
        A list of user ids to send the message to.

        :return: The recipients of this TemplateEmailResource.
        :rtype: list[int]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """
        Sets the recipients of this TemplateEmailResource.
        A list of user ids to send the message to.

        :param recipients: The recipients of this TemplateEmailResource.
        :type: list[int]
        """
        if recipients is None:
            raise ValueError("Invalid value for `recipients`, must not be `None`")

        self._recipients = recipients

    @property
    def template_key(self):
        """
        Gets the template_key of this TemplateEmailResource.
        The key for the template

        :return: The template_key of this TemplateEmailResource.
        :rtype: str
        """
        return self._template_key

    @template_key.setter
    def template_key(self, template_key):
        """
        Sets the template_key of this TemplateEmailResource.
        The key for the template

        :param template_key: The template_key of this TemplateEmailResource.
        :type: str
        """
        if template_key is None:
            raise ValueError("Invalid value for `template_key`, must not be `None`")

        self._template_key = template_key

    @property
    def template_vars(self):
        """
        Gets the template_vars of this TemplateEmailResource.
        A list of variables to fill in the template

        :return: The template_vars of this TemplateEmailResource.
        :rtype: list[KeyValuePairstringstring]
        """
        return self._template_vars

    @template_vars.setter
    def template_vars(self, template_vars):
        """
        Sets the template_vars of this TemplateEmailResource.
        A list of variables to fill in the template

        :param template_vars: The template_vars of this TemplateEmailResource.
        :type: list[KeyValuePairstringstring]
        """

        self._template_vars = template_vars

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
        if not isinstance(other, TemplateEmailResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
