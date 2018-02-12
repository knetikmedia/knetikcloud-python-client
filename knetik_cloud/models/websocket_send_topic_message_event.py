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


class WebsocketSendTopicMessageEvent(object):
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
        'topic': 'str'
    }

    attribute_map = {
        'content': 'content',
        'topic': 'topic'
    }

    def __init__(self, content=None, topic=None):
        """
        WebsocketSendTopicMessageEvent - a model defined in Swagger
        """

        self._content = None
        self._topic = None
        self.discriminator = None

        if content is not None:
          self.content = content
        if topic is not None:
          self.topic = topic

    @property
    def content(self):
        """
        Gets the content of this WebsocketSendTopicMessageEvent.

        :return: The content of this WebsocketSendTopicMessageEvent.
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this WebsocketSendTopicMessageEvent.

        :param content: The content of this WebsocketSendTopicMessageEvent.
        :type: object
        """

        self._content = content

    @property
    def topic(self):
        """
        Gets the topic of this WebsocketSendTopicMessageEvent.

        :return: The topic of this WebsocketSendTopicMessageEvent.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """
        Sets the topic of this WebsocketSendTopicMessageEvent.

        :param topic: The topic of this WebsocketSendTopicMessageEvent.
        :type: str
        """

        self._topic = topic

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
        if not isinstance(other, WebsocketSendTopicMessageEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
