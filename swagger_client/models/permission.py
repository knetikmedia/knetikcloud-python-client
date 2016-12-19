# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Permission(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created_date=None, description=None, id=None, locked=None, name=None, parent=None, permission=None, permission_role=None, updated_date=None):
        """
        Permission - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created_date': 'int',
            'description': 'str',
            'id': 'int',
            'locked': 'bool',
            'name': 'str',
            'parent': 'str',
            'permission': 'str',
            'permission_role': 'list[Role]',
            'updated_date': 'int'
        }

        self.attribute_map = {
            'created_date': 'created_date',
            'description': 'description',
            'id': 'id',
            'locked': 'locked',
            'name': 'name',
            'parent': 'parent',
            'permission': 'permission',
            'permission_role': 'permission_role',
            'updated_date': 'updated_date'
        }

        self._created_date = created_date
        self._description = description
        self._id = id
        self._locked = locked
        self._name = name
        self._parent = parent
        self._permission = permission
        self._permission_role = permission_role
        self._updated_date = updated_date

    @property
    def created_date(self):
        """
        Gets the created_date of this Permission.

        :return: The created_date of this Permission.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this Permission.

        :param created_date: The created_date of this Permission.
        :type: int
        """

        self._created_date = created_date

    @property
    def description(self):
        """
        Gets the description of this Permission.

        :return: The description of this Permission.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Permission.

        :param description: The description of this Permission.
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """
        Gets the id of this Permission.

        :return: The id of this Permission.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Permission.

        :param id: The id of this Permission.
        :type: int
        """

        self._id = id

    @property
    def locked(self):
        """
        Gets the locked of this Permission.

        :return: The locked of this Permission.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """
        Sets the locked of this Permission.

        :param locked: The locked of this Permission.
        :type: bool
        """

        self._locked = locked

    @property
    def name(self):
        """
        Gets the name of this Permission.

        :return: The name of this Permission.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Permission.

        :param name: The name of this Permission.
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """
        Gets the parent of this Permission.

        :return: The parent of this Permission.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this Permission.

        :param parent: The parent of this Permission.
        :type: str
        """

        self._parent = parent

    @property
    def permission(self):
        """
        Gets the permission of this Permission.

        :return: The permission of this Permission.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """
        Sets the permission of this Permission.

        :param permission: The permission of this Permission.
        :type: str
        """

        self._permission = permission

    @property
    def permission_role(self):
        """
        Gets the permission_role of this Permission.

        :return: The permission_role of this Permission.
        :rtype: list[Role]
        """
        return self._permission_role

    @permission_role.setter
    def permission_role(self, permission_role):
        """
        Sets the permission_role of this Permission.

        :param permission_role: The permission_role of this Permission.
        :type: list[Role]
        """

        self._permission_role = permission_role

    @property
    def updated_date(self):
        """
        Gets the updated_date of this Permission.

        :return: The updated_date of this Permission.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this Permission.

        :param updated_date: The updated_date of this Permission.
        :type: int
        """

        self._updated_date = updated_date

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
