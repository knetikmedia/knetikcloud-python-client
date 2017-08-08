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


class MongoDatabaseConfig(object):
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
        'db_name': 'str',
        'options': 'str',
        'password': 'str',
        'servers': 'str',
        'username': 'str'
    }

    attribute_map = {
        'db_name': 'db_name',
        'options': 'options',
        'password': 'password',
        'servers': 'servers',
        'username': 'username'
    }

    def __init__(self, db_name=None, options=None, password=None, servers=None, username=None):
        """
        MongoDatabaseConfig - a model defined in Swagger
        """

        self._db_name = None
        self._options = None
        self._password = None
        self._servers = None
        self._username = None
        self.discriminator = None

        if db_name is not None:
          self.db_name = db_name
        if options is not None:
          self.options = options
        if password is not None:
          self.password = password
        if servers is not None:
          self.servers = servers
        if username is not None:
          self.username = username

    @property
    def db_name(self):
        """
        Gets the db_name of this MongoDatabaseConfig.

        :return: The db_name of this MongoDatabaseConfig.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this MongoDatabaseConfig.

        :param db_name: The db_name of this MongoDatabaseConfig.
        :type: str
        """

        self._db_name = db_name

    @property
    def options(self):
        """
        Gets the options of this MongoDatabaseConfig.

        :return: The options of this MongoDatabaseConfig.
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this MongoDatabaseConfig.

        :param options: The options of this MongoDatabaseConfig.
        :type: str
        """

        self._options = options

    @property
    def password(self):
        """
        Gets the password of this MongoDatabaseConfig.

        :return: The password of this MongoDatabaseConfig.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this MongoDatabaseConfig.

        :param password: The password of this MongoDatabaseConfig.
        :type: str
        """

        self._password = password

    @property
    def servers(self):
        """
        Gets the servers of this MongoDatabaseConfig.

        :return: The servers of this MongoDatabaseConfig.
        :rtype: str
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """
        Sets the servers of this MongoDatabaseConfig.

        :param servers: The servers of this MongoDatabaseConfig.
        :type: str
        """

        self._servers = servers

    @property
    def username(self):
        """
        Gets the username of this MongoDatabaseConfig.

        :return: The username of this MongoDatabaseConfig.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this MongoDatabaseConfig.

        :param username: The username of this MongoDatabaseConfig.
        :type: str
        """

        self._username = username

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
        if not isinstance(other, MongoDatabaseConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
