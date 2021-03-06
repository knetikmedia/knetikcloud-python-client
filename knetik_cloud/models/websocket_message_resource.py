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


class WebsocketMessageResource(object):
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
        'content': 'object',
        'message_type': 'str',
        'recipients': 'list[int]'
    }

    attribute_map = {
        'content': 'content',
        'message_type': 'message_type',
        'recipients': 'recipients'
    }

    def __init__(self, content=None, message_type=None, recipients=None):
        """
        WebsocketMessageResource - a model defined in Swagger
        """

        self._content = None
        self._message_type = None
        self._recipients = None
        self.discriminator = None

        self.content = content
        if message_type is not None:
          self.message_type = message_type
        self.recipients = recipients

    @property
    def content(self):
        """
        Gets the content of this WebsocketMessageResource.
        The body of the outgoing message.

        :return: The content of this WebsocketMessageResource.
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this WebsocketMessageResource.
        The body of the outgoing message.

        :param content: The content of this WebsocketMessageResource.
        :type: object
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")

        self._content = content

    @property
    def message_type(self):
        """
        Gets the message_type of this WebsocketMessageResource.
        A message type to inform websocket recipient how to parse content

        :return: The message_type of this WebsocketMessageResource.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """
        Sets the message_type of this WebsocketMessageResource.
        A message type to inform websocket recipient how to parse content

        :param message_type: The message_type of this WebsocketMessageResource.
        :type: str
        """

        self._message_type = message_type

    @property
    def recipients(self):
        """
        Gets the recipients of this WebsocketMessageResource.
        A list of user ids to send the message to.

        :return: The recipients of this WebsocketMessageResource.
        :rtype: list[int]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """
        Sets the recipients of this WebsocketMessageResource.
        A list of user ids to send the message to.

        :param recipients: The recipients of this WebsocketMessageResource.
        :type: list[int]
        """
        if recipients is None:
            raise ValueError("Invalid value for `recipients`, must not be `None`")

        self._recipients = recipients

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
        if not isinstance(other, WebsocketMessageResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
