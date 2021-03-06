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


class WebsocketUnsubscribeEvent(object):
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
        'topic': 'Topic',
        'topic_subscriber': 'TopicSubscriber'
    }

    attribute_map = {
        'topic': 'topic',
        'topic_subscriber': 'topic_subscriber'
    }

    def __init__(self, topic=None, topic_subscriber=None):
        """
        WebsocketUnsubscribeEvent - a model defined in Swagger
        """

        self._topic = None
        self._topic_subscriber = None
        self.discriminator = None

        if topic is not None:
          self.topic = topic
        if topic_subscriber is not None:
          self.topic_subscriber = topic_subscriber

    @property
    def topic(self):
        """
        Gets the topic of this WebsocketUnsubscribeEvent.

        :return: The topic of this WebsocketUnsubscribeEvent.
        :rtype: Topic
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """
        Sets the topic of this WebsocketUnsubscribeEvent.

        :param topic: The topic of this WebsocketUnsubscribeEvent.
        :type: Topic
        """

        self._topic = topic

    @property
    def topic_subscriber(self):
        """
        Gets the topic_subscriber of this WebsocketUnsubscribeEvent.

        :return: The topic_subscriber of this WebsocketUnsubscribeEvent.
        :rtype: TopicSubscriber
        """
        return self._topic_subscriber

    @topic_subscriber.setter
    def topic_subscriber(self, topic_subscriber):
        """
        Sets the topic_subscriber of this WebsocketUnsubscribeEvent.

        :param topic_subscriber: The topic_subscriber of this WebsocketUnsubscribeEvent.
        :type: TopicSubscriber
        """

        self._topic_subscriber = topic_subscriber

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
        if not isinstance(other, WebsocketUnsubscribeEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
