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


class CommentSearch(object):
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
        'content': 'str',
        'context': 'str',
        'context_id': 'int',
        'id': 'int',
        'owner_id': 'int',
        'owner_username': 'str'
    }

    attribute_map = {
        'content': 'content',
        'context': 'context',
        'context_id': 'context_id',
        'id': 'id',
        'owner_id': 'owner_id',
        'owner_username': 'owner_username'
    }

    def __init__(self, content=None, context=None, context_id=None, id=None, owner_id=None, owner_username=None):
        """
        CommentSearch - a model defined in Swagger
        """

        self._content = None
        self._context = None
        self._context_id = None
        self._id = None
        self._owner_id = None
        self._owner_username = None

        if content is not None:
          self.content = content
        if context is not None:
          self.context = context
        if context_id is not None:
          self.context_id = context_id
        if id is not None:
          self.id = id
        if owner_id is not None:
          self.owner_id = owner_id
        if owner_username is not None:
          self.owner_username = owner_username

    @property
    def content(self):
        """
        Gets the content of this CommentSearch.

        :return: The content of this CommentSearch.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this CommentSearch.

        :param content: The content of this CommentSearch.
        :type: str
        """

        self._content = content

    @property
    def context(self):
        """
        Gets the context of this CommentSearch.

        :return: The context of this CommentSearch.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this CommentSearch.

        :param context: The context of this CommentSearch.
        :type: str
        """

        self._context = context

    @property
    def context_id(self):
        """
        Gets the context_id of this CommentSearch.

        :return: The context_id of this CommentSearch.
        :rtype: int
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """
        Sets the context_id of this CommentSearch.

        :param context_id: The context_id of this CommentSearch.
        :type: int
        """

        self._context_id = context_id

    @property
    def id(self):
        """
        Gets the id of this CommentSearch.

        :return: The id of this CommentSearch.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CommentSearch.

        :param id: The id of this CommentSearch.
        :type: int
        """

        self._id = id

    @property
    def owner_id(self):
        """
        Gets the owner_id of this CommentSearch.

        :return: The owner_id of this CommentSearch.
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """
        Sets the owner_id of this CommentSearch.

        :param owner_id: The owner_id of this CommentSearch.
        :type: int
        """

        self._owner_id = owner_id

    @property
    def owner_username(self):
        """
        Gets the owner_username of this CommentSearch.

        :return: The owner_username of this CommentSearch.
        :rtype: str
        """
        return self._owner_username

    @owner_username.setter
    def owner_username(self, owner_username):
        """
        Sets the owner_username of this CommentSearch.

        :param owner_username: The owner_username of this CommentSearch.
        :type: str
        """

        self._owner_username = owner_username

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
        if not isinstance(other, CommentSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other