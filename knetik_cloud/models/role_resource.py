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


class RoleResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, client_count=None, created_date=None, locked=None, name=None, role=None, role_permission=None, user_count=None):
        """
        RoleResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'client_count': 'int',
            'created_date': 'int',
            'locked': 'bool',
            'name': 'str',
            'role': 'str',
            'role_permission': 'list[PermissionResource]',
            'user_count': 'int'
        }

        self.attribute_map = {
            'client_count': 'client_count',
            'created_date': 'created_date',
            'locked': 'locked',
            'name': 'name',
            'role': 'role',
            'role_permission': 'role_permission',
            'user_count': 'user_count'
        }

        self._client_count = client_count
        self._created_date = created_date
        self._locked = locked
        self._name = name
        self._role = role
        self._role_permission = role_permission
        self._user_count = user_count

    @property
    def client_count(self):
        """
        Gets the client_count of this RoleResource.
        The number of clients this role is assigned to

        :return: The client_count of this RoleResource.
        :rtype: int
        """
        return self._client_count

    @client_count.setter
    def client_count(self, client_count):
        """
        Sets the client_count of this RoleResource.
        The number of clients this role is assigned to

        :param client_count: The client_count of this RoleResource.
        :type: int
        """

        self._client_count = client_count

    @property
    def created_date(self):
        """
        Gets the created_date of this RoleResource.
        The date the role was added. Unix timestamp in seconds

        :return: The created_date of this RoleResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this RoleResource.
        The date the role was added. Unix timestamp in seconds

        :param created_date: The created_date of this RoleResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def locked(self):
        """
        Gets the locked of this RoleResource.
        Whether a role is locked from being deleted

        :return: The locked of this RoleResource.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """
        Sets the locked of this RoleResource.
        Whether a role is locked from being deleted

        :param locked: The locked of this RoleResource.
        :type: bool
        """

        self._locked = locked

    @property
    def name(self):
        """
        Gets the name of this RoleResource.
        The name of the role used for display purposes

        :return: The name of this RoleResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RoleResource.
        The name of the role used for display purposes

        :param name: The name of this RoleResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def role(self):
        """
        Gets the role of this RoleResource.
        The keyword that defines the role

        :return: The role of this RoleResource.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this RoleResource.
        The keyword that defines the role

        :param role: The role of this RoleResource.
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")

        self._role = role

    @property
    def role_permission(self):
        """
        Gets the role_permission of this RoleResource.
        The list of permissions this role has

        :return: The role_permission of this RoleResource.
        :rtype: list[PermissionResource]
        """
        return self._role_permission

    @role_permission.setter
    def role_permission(self, role_permission):
        """
        Sets the role_permission of this RoleResource.
        The list of permissions this role has

        :param role_permission: The role_permission of this RoleResource.
        :type: list[PermissionResource]
        """

        self._role_permission = role_permission

    @property
    def user_count(self):
        """
        Gets the user_count of this RoleResource.
        The number of users this role is assigned to

        :return: The user_count of this RoleResource.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """
        Sets the user_count of this RoleResource.
        The number of users this role is assigned to

        :param user_count: The user_count of this RoleResource.
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
        if not isinstance(other, RoleResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
