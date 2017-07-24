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


class CacheClearEvent(object):
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
        'client': 'str',
        'customer': 'str',
        'do_not_broadcast': 'bool',
        'section': 'str',
        'source': 'object',
        'specifics': 'str',
        'synchronous': 'bool',
        'timestamp': 'int',
        'type': 'str',
        'customer_setup': 'bool',
        'customer_teardown': 'bool'
    }

    attribute_map = {
        'client': 'client',
        'customer': 'customer',
        'do_not_broadcast': 'do_not_broadcast',
        'section': 'section',
        'source': 'source',
        'specifics': 'specifics',
        'synchronous': 'synchronous',
        'timestamp': 'timestamp',
        'type': 'type',
        'customer_setup': 'customer_setup',
        'customer_teardown': 'customer_teardown'
    }

    def __init__(self, client=None, customer=None, do_not_broadcast=None, section=None, source=None, specifics=None, synchronous=None, timestamp=None, type=None, customer_setup=None, customer_teardown=None):
        """
        CacheClearEvent - a model defined in Swagger
        """

        self._client = None
        self._customer = None
        self._do_not_broadcast = None
        self._section = None
        self._source = None
        self._specifics = None
        self._synchronous = None
        self._timestamp = None
        self._type = None
        self._customer_setup = None
        self._customer_teardown = None

        if client is not None:
          self.client = client
        if customer is not None:
          self.customer = customer
        if do_not_broadcast is not None:
          self.do_not_broadcast = do_not_broadcast
        if section is not None:
          self.section = section
        if source is not None:
          self.source = source
        if specifics is not None:
          self.specifics = specifics
        if synchronous is not None:
          self.synchronous = synchronous
        if timestamp is not None:
          self.timestamp = timestamp
        self.type = type
        if customer_setup is not None:
          self.customer_setup = customer_setup
        if customer_teardown is not None:
          self.customer_teardown = customer_teardown

    @property
    def client(self):
        """
        Gets the client of this CacheClearEvent.

        :return: The client of this CacheClearEvent.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """
        Sets the client of this CacheClearEvent.

        :param client: The client of this CacheClearEvent.
        :type: str
        """

        self._client = client

    @property
    def customer(self):
        """
        Gets the customer of this CacheClearEvent.

        :return: The customer of this CacheClearEvent.
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this CacheClearEvent.

        :param customer: The customer of this CacheClearEvent.
        :type: str
        """

        self._customer = customer

    @property
    def do_not_broadcast(self):
        """
        Gets the do_not_broadcast of this CacheClearEvent.

        :return: The do_not_broadcast of this CacheClearEvent.
        :rtype: bool
        """
        return self._do_not_broadcast

    @do_not_broadcast.setter
    def do_not_broadcast(self, do_not_broadcast):
        """
        Sets the do_not_broadcast of this CacheClearEvent.

        :param do_not_broadcast: The do_not_broadcast of this CacheClearEvent.
        :type: bool
        """

        self._do_not_broadcast = do_not_broadcast

    @property
    def section(self):
        """
        Gets the section of this CacheClearEvent.

        :return: The section of this CacheClearEvent.
        :rtype: str
        """
        return self._section

    @section.setter
    def section(self, section):
        """
        Sets the section of this CacheClearEvent.

        :param section: The section of this CacheClearEvent.
        :type: str
        """

        self._section = section

    @property
    def source(self):
        """
        Gets the source of this CacheClearEvent.

        :return: The source of this CacheClearEvent.
        :rtype: object
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CacheClearEvent.

        :param source: The source of this CacheClearEvent.
        :type: object
        """

        self._source = source

    @property
    def specifics(self):
        """
        Gets the specifics of this CacheClearEvent.

        :return: The specifics of this CacheClearEvent.
        :rtype: str
        """
        return self._specifics

    @specifics.setter
    def specifics(self, specifics):
        """
        Sets the specifics of this CacheClearEvent.

        :param specifics: The specifics of this CacheClearEvent.
        :type: str
        """

        self._specifics = specifics

    @property
    def synchronous(self):
        """
        Gets the synchronous of this CacheClearEvent.

        :return: The synchronous of this CacheClearEvent.
        :rtype: bool
        """
        return self._synchronous

    @synchronous.setter
    def synchronous(self, synchronous):
        """
        Sets the synchronous of this CacheClearEvent.

        :param synchronous: The synchronous of this CacheClearEvent.
        :type: bool
        """

        self._synchronous = synchronous

    @property
    def timestamp(self):
        """
        Gets the timestamp of this CacheClearEvent.

        :return: The timestamp of this CacheClearEvent.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this CacheClearEvent.

        :param timestamp: The timestamp of this CacheClearEvent.
        :type: int
        """

        self._timestamp = timestamp

    @property
    def type(self):
        """
        Gets the type of this CacheClearEvent.
        The type of the event. Used for polymorphic type recognition and thus must match an expected type

        :return: The type of this CacheClearEvent.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CacheClearEvent.
        The type of the event. Used for polymorphic type recognition and thus must match an expected type

        :param type: The type of this CacheClearEvent.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def customer_setup(self):
        """
        Gets the customer_setup of this CacheClearEvent.

        :return: The customer_setup of this CacheClearEvent.
        :rtype: bool
        """
        return self._customer_setup

    @customer_setup.setter
    def customer_setup(self, customer_setup):
        """
        Sets the customer_setup of this CacheClearEvent.

        :param customer_setup: The customer_setup of this CacheClearEvent.
        :type: bool
        """

        self._customer_setup = customer_setup

    @property
    def customer_teardown(self):
        """
        Gets the customer_teardown of this CacheClearEvent.

        :return: The customer_teardown of this CacheClearEvent.
        :rtype: bool
        """
        return self._customer_teardown

    @customer_teardown.setter
    def customer_teardown(self, customer_teardown):
        """
        Sets the customer_teardown of this CacheClearEvent.

        :param customer_teardown: The customer_teardown of this CacheClearEvent.
        :type: bool
        """

        self._customer_teardown = customer_teardown

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
        if not isinstance(other, CacheClearEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
