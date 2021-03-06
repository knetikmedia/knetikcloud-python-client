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


class Topic(object):
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
        'created_date': 'int',
        'display_name': 'str',
        'id': 'str',
        'locked': 'bool',
        'tags': 'list[str]',
        'topic_map': 'object',
        'updated_date': 'int',
        'user_count': 'int'
    }

    attribute_map = {
        'created_date': 'created_date',
        'display_name': 'display_name',
        'id': 'id',
        'locked': 'locked',
        'tags': 'tags',
        'topic_map': 'topic_map',
        'updated_date': 'updated_date',
        'user_count': 'user_count'
    }

    def __init__(self, created_date=None, display_name=None, id=None, locked=None, tags=None, topic_map=None, updated_date=None, user_count=None):
        """
        Topic - a model defined in Swagger
        """

        self._created_date = None
        self._display_name = None
        self._id = None
        self._locked = None
        self._tags = None
        self._topic_map = None
        self._updated_date = None
        self._user_count = None
        self.discriminator = None

        if created_date is not None:
          self.created_date = created_date
        if display_name is not None:
          self.display_name = display_name
        if id is not None:
          self.id = id
        if locked is not None:
          self.locked = locked
        if tags is not None:
          self.tags = tags
        if topic_map is not None:
          self.topic_map = topic_map
        if updated_date is not None:
          self.updated_date = updated_date
        if user_count is not None:
          self.user_count = user_count

    @property
    def created_date(self):
        """
        Gets the created_date of this Topic.

        :return: The created_date of this Topic.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this Topic.

        :param created_date: The created_date of this Topic.
        :type: int
        """

        self._created_date = created_date

    @property
    def display_name(self):
        """
        Gets the display_name of this Topic.

        :return: The display_name of this Topic.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Topic.

        :param display_name: The display_name of this Topic.
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this Topic.

        :return: The id of this Topic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Topic.

        :param id: The id of this Topic.
        :type: str
        """

        self._id = id

    @property
    def locked(self):
        """
        Gets the locked of this Topic.

        :return: The locked of this Topic.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """
        Sets the locked of this Topic.

        :param locked: The locked of this Topic.
        :type: bool
        """

        self._locked = locked

    @property
    def tags(self):
        """
        Gets the tags of this Topic.

        :return: The tags of this Topic.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Topic.

        :param tags: The tags of this Topic.
        :type: list[str]
        """

        self._tags = tags

    @property
    def topic_map(self):
        """
        Gets the topic_map of this Topic.

        :return: The topic_map of this Topic.
        :rtype: object
        """
        return self._topic_map

    @topic_map.setter
    def topic_map(self, topic_map):
        """
        Sets the topic_map of this Topic.

        :param topic_map: The topic_map of this Topic.
        :type: object
        """

        self._topic_map = topic_map

    @property
    def updated_date(self):
        """
        Gets the updated_date of this Topic.

        :return: The updated_date of this Topic.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this Topic.

        :param updated_date: The updated_date of this Topic.
        :type: int
        """

        self._updated_date = updated_date

    @property
    def user_count(self):
        """
        Gets the user_count of this Topic.

        :return: The user_count of this Topic.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """
        Sets the user_count of this Topic.

        :param user_count: The user_count of this Topic.
        :type: int
        """

        self._user_count = user_count

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
        if not isinstance(other, Topic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
