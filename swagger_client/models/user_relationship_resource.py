# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserRelationshipResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, child=None, context=None, id=None, parent=None):
        """
        UserRelationshipResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'child': 'SimpleUserResource',
            'context': 'str',
            'id': 'int',
            'parent': 'SimpleUserResource'
        }

        self.attribute_map = {
            'child': 'child',
            'context': 'context',
            'id': 'id',
            'parent': 'parent'
        }

        self._child = child
        self._context = context
        self._id = id
        self._parent = parent

    @property
    def child(self):
        """
        Gets the child of this UserRelationshipResource.
        The child in the relationship

        :return: The child of this UserRelationshipResource.
        :rtype: SimpleUserResource
        """
        return self._child

    @child.setter
    def child(self, child):
        """
        Sets the child of this UserRelationshipResource.
        The child in the relationship

        :param child: The child of this UserRelationshipResource.
        :type: SimpleUserResource
        """
        if child is None:
            raise ValueError("Invalid value for `child`, must not be `None`")

        self._child = child

    @property
    def context(self):
        """
        Gets the context of this UserRelationshipResource.
        Context about the relationship or its type

        :return: The context of this UserRelationshipResource.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this UserRelationshipResource.
        Context about the relationship or its type

        :param context: The context of this UserRelationshipResource.
        :type: str
        """

        self._context = context

    @property
    def id(self):
        """
        Gets the id of this UserRelationshipResource.
        A generated unique id. Read-Only

        :return: The id of this UserRelationshipResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserRelationshipResource.
        A generated unique id. Read-Only

        :param id: The id of this UserRelationshipResource.
        :type: int
        """

        self._id = id

    @property
    def parent(self):
        """
        Gets the parent of this UserRelationshipResource.
        The parent in the relationship

        :return: The parent of this UserRelationshipResource.
        :rtype: SimpleUserResource
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this UserRelationshipResource.
        The parent in the relationship

        :param parent: The parent of this UserRelationshipResource.
        :type: SimpleUserResource
        """
        if parent is None:
            raise ValueError("Invalid value for `parent`, must not be `None`")

        self._parent = parent

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
