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


class RawSMSResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _from=None, recipients=None, text=None):
        """
        RawSMSResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_from': 'str',
            'recipients': 'list[int]',
            'text': 'str'
        }

        self.attribute_map = {
            '_from': 'from',
            'recipients': 'recipients',
            'text': 'text'
        }

        self.__from = _from
        self._recipients = recipients
        self._text = text

    @property
    def _from(self):
        """
        Gets the _from of this RawSMSResource.
        The phone number to attribute the outgoing message to. Optional if the config text.out_number is set.

        :return: The _from of this RawSMSResource.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this RawSMSResource.
        The phone number to attribute the outgoing message to. Optional if the config text.out_number is set.

        :param _from: The _from of this RawSMSResource.
        :type: str
        """

        self.__from = _from

    @property
    def recipients(self):
        """
        Gets the recipients of this RawSMSResource.
        A list of user ids to send the message to.

        :return: The recipients of this RawSMSResource.
        :rtype: list[int]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """
        Sets the recipients of this RawSMSResource.
        A list of user ids to send the message to.

        :param recipients: The recipients of this RawSMSResource.
        :type: list[int]
        """
        if recipients is None:
            raise ValueError("Invalid value for `recipients`, must not be `None`")

        self._recipients = recipients

    @property
    def text(self):
        """
        Gets the text of this RawSMSResource.
        The body of the outgoing text message.

        :return: The text of this RawSMSResource.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this RawSMSResource.
        The body of the outgoing text message.

        :param text: The text of this RawSMSResource.
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")

        self._text = text

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
