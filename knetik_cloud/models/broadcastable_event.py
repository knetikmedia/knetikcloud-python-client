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


class BroadcastableEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, client=None, customer=None, do_not_broadcast=None, section=None, source=None, specifics=None, synchronous=None, timestamp=None, type=None):
        """
        BroadcastableEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'client': 'str',
            'customer': 'str',
            'do_not_broadcast': 'bool',
            'section': 'str',
            'source': 'object',
            'specifics': 'str',
            'synchronous': 'bool',
            'timestamp': 'int',
            'type': 'str'
        }

        self.attribute_map = {
            'client': 'client',
            'customer': 'customer',
            'do_not_broadcast': 'do_not_broadcast',
            'section': 'section',
            'source': 'source',
            'specifics': 'specifics',
            'synchronous': 'synchronous',
            'timestamp': 'timestamp',
            'type': 'type'
        }

        self._client = client
        self._customer = customer
        self._do_not_broadcast = do_not_broadcast
        self._section = section
        self._source = source
        self._specifics = specifics
        self._synchronous = synchronous
        self._timestamp = timestamp
        self._type = type

    @property
    def client(self):
        """
        Gets the client of this BroadcastableEvent.

        :return: The client of this BroadcastableEvent.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """
        Sets the client of this BroadcastableEvent.

        :param client: The client of this BroadcastableEvent.
        :type: str
        """

        self._client = client

    @property
    def customer(self):
        """
        Gets the customer of this BroadcastableEvent.

        :return: The customer of this BroadcastableEvent.
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this BroadcastableEvent.

        :param customer: The customer of this BroadcastableEvent.
        :type: str
        """

        self._customer = customer

    @property
    def do_not_broadcast(self):
        """
        Gets the do_not_broadcast of this BroadcastableEvent.

        :return: The do_not_broadcast of this BroadcastableEvent.
        :rtype: bool
        """
        return self._do_not_broadcast

    @do_not_broadcast.setter
    def do_not_broadcast(self, do_not_broadcast):
        """
        Sets the do_not_broadcast of this BroadcastableEvent.

        :param do_not_broadcast: The do_not_broadcast of this BroadcastableEvent.
        :type: bool
        """

        self._do_not_broadcast = do_not_broadcast

    @property
    def section(self):
        """
        Gets the section of this BroadcastableEvent.

        :return: The section of this BroadcastableEvent.
        :rtype: str
        """
        return self._section

    @section.setter
    def section(self, section):
        """
        Sets the section of this BroadcastableEvent.

        :param section: The section of this BroadcastableEvent.
        :type: str
        """

        self._section = section

    @property
    def source(self):
        """
        Gets the source of this BroadcastableEvent.

        :return: The source of this BroadcastableEvent.
        :rtype: object
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this BroadcastableEvent.

        :param source: The source of this BroadcastableEvent.
        :type: object
        """

        self._source = source

    @property
    def specifics(self):
        """
        Gets the specifics of this BroadcastableEvent.

        :return: The specifics of this BroadcastableEvent.
        :rtype: str
        """
        return self._specifics

    @specifics.setter
    def specifics(self, specifics):
        """
        Sets the specifics of this BroadcastableEvent.

        :param specifics: The specifics of this BroadcastableEvent.
        :type: str
        """

        self._specifics = specifics

    @property
    def synchronous(self):
        """
        Gets the synchronous of this BroadcastableEvent.

        :return: The synchronous of this BroadcastableEvent.
        :rtype: bool
        """
        return self._synchronous

    @synchronous.setter
    def synchronous(self, synchronous):
        """
        Sets the synchronous of this BroadcastableEvent.

        :param synchronous: The synchronous of this BroadcastableEvent.
        :type: bool
        """

        self._synchronous = synchronous

    @property
    def timestamp(self):
        """
        Gets the timestamp of this BroadcastableEvent.

        :return: The timestamp of this BroadcastableEvent.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this BroadcastableEvent.

        :param timestamp: The timestamp of this BroadcastableEvent.
        :type: int
        """

        self._timestamp = timestamp

    @property
    def type(self):
        """
        Gets the type of this BroadcastableEvent.
        The type of the event. Used for polymorphic type recognition and thus must match an expected type

        :return: The type of this BroadcastableEvent.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BroadcastableEvent.
        The type of the event. Used for polymorphic type recognition and thus must match an expected type

        :param type: The type of this BroadcastableEvent.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

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
        if not isinstance(other, BroadcastableEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
