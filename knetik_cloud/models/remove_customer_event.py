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


class RemoveCustomerEvent(object):
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
        'customer_config': 'CustomerConfig'
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
        'customer_config': 'customer_config'
    }

    def __init__(self, client=None, customer=None, do_not_broadcast=None, section=None, source=None, specifics=None, synchronous=None, timestamp=None, type=None, customer_config=None):
        """
        RemoveCustomerEvent - a model defined in Swagger
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
        self._customer_config = None

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
        if customer_config is not None:
          self.customer_config = customer_config

    @property
    def client(self):
        """
        Gets the client of this RemoveCustomerEvent.

        :return: The client of this RemoveCustomerEvent.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """
        Sets the client of this RemoveCustomerEvent.

        :param client: The client of this RemoveCustomerEvent.
        :type: str
        """

        self._client = client

    @property
    def customer(self):
        """
        Gets the customer of this RemoveCustomerEvent.

        :return: The customer of this RemoveCustomerEvent.
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this RemoveCustomerEvent.

        :param customer: The customer of this RemoveCustomerEvent.
        :type: str
        """

        self._customer = customer

    @property
    def do_not_broadcast(self):
        """
        Gets the do_not_broadcast of this RemoveCustomerEvent.

        :return: The do_not_broadcast of this RemoveCustomerEvent.
        :rtype: bool
        """
        return self._do_not_broadcast

    @do_not_broadcast.setter
    def do_not_broadcast(self, do_not_broadcast):
        """
        Sets the do_not_broadcast of this RemoveCustomerEvent.

        :param do_not_broadcast: The do_not_broadcast of this RemoveCustomerEvent.
        :type: bool
        """

        self._do_not_broadcast = do_not_broadcast

    @property
    def section(self):
        """
        Gets the section of this RemoveCustomerEvent.

        :return: The section of this RemoveCustomerEvent.
        :rtype: str
        """
        return self._section

    @section.setter
    def section(self, section):
        """
        Sets the section of this RemoveCustomerEvent.

        :param section: The section of this RemoveCustomerEvent.
        :type: str
        """

        self._section = section

    @property
    def source(self):
        """
        Gets the source of this RemoveCustomerEvent.

        :return: The source of this RemoveCustomerEvent.
        :rtype: object
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this RemoveCustomerEvent.

        :param source: The source of this RemoveCustomerEvent.
        :type: object
        """

        self._source = source

    @property
    def specifics(self):
        """
        Gets the specifics of this RemoveCustomerEvent.

        :return: The specifics of this RemoveCustomerEvent.
        :rtype: str
        """
        return self._specifics

    @specifics.setter
    def specifics(self, specifics):
        """
        Sets the specifics of this RemoveCustomerEvent.

        :param specifics: The specifics of this RemoveCustomerEvent.
        :type: str
        """

        self._specifics = specifics

    @property
    def synchronous(self):
        """
        Gets the synchronous of this RemoveCustomerEvent.

        :return: The synchronous of this RemoveCustomerEvent.
        :rtype: bool
        """
        return self._synchronous

    @synchronous.setter
    def synchronous(self, synchronous):
        """
        Sets the synchronous of this RemoveCustomerEvent.

        :param synchronous: The synchronous of this RemoveCustomerEvent.
        :type: bool
        """

        self._synchronous = synchronous

    @property
    def timestamp(self):
        """
        Gets the timestamp of this RemoveCustomerEvent.

        :return: The timestamp of this RemoveCustomerEvent.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this RemoveCustomerEvent.

        :param timestamp: The timestamp of this RemoveCustomerEvent.
        :type: int
        """

        self._timestamp = timestamp

    @property
    def type(self):
        """
        Gets the type of this RemoveCustomerEvent.
        The type of the event. Used for polymorphic type recognition and thus must match an expected type

        :return: The type of this RemoveCustomerEvent.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RemoveCustomerEvent.
        The type of the event. Used for polymorphic type recognition and thus must match an expected type

        :param type: The type of this RemoveCustomerEvent.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def customer_config(self):
        """
        Gets the customer_config of this RemoveCustomerEvent.

        :return: The customer_config of this RemoveCustomerEvent.
        :rtype: CustomerConfig
        """
        return self._customer_config

    @customer_config.setter
    def customer_config(self, customer_config):
        """
        Sets the customer_config of this RemoveCustomerEvent.

        :param customer_config: The customer_config of this RemoveCustomerEvent.
        :type: CustomerConfig
        """

        self._customer_config = customer_config

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
        if not isinstance(other, RemoveCustomerEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other