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


class UserInventoryResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, behavior_data=None, created_date=None, expires=None, id=None, invoice_id=None, item_id=None, item_name=None, item_type_hint=None, status=None, updated_date=None, user=None):
        """
        UserInventoryResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'behavior_data': 'object',
            'created_date': 'int',
            'expires': 'int',
            'id': 'int',
            'invoice_id': 'int',
            'item_id': 'int',
            'item_name': 'str',
            'item_type_hint': 'str',
            'status': 'str',
            'updated_date': 'int',
            'user': 'SimpleUserResource'
        }

        self.attribute_map = {
            'behavior_data': 'behavior_data',
            'created_date': 'created_date',
            'expires': 'expires',
            'id': 'id',
            'invoice_id': 'invoice_id',
            'item_id': 'item_id',
            'item_name': 'item_name',
            'item_type_hint': 'item_type_hint',
            'status': 'status',
            'updated_date': 'updated_date',
            'user': 'user'
        }

        self._behavior_data = behavior_data
        self._created_date = created_date
        self._expires = expires
        self._id = id
        self._invoice_id = invoice_id
        self._item_id = item_id
        self._item_name = item_name
        self._item_type_hint = item_type_hint
        self._status = status
        self._updated_date = updated_date
        self._user = user

    @property
    def behavior_data(self):
        """
        Gets the behavior_data of this UserInventoryResource.
        A map of data for behaviors

        :return: The behavior_data of this UserInventoryResource.
        :rtype: object
        """
        return self._behavior_data

    @behavior_data.setter
    def behavior_data(self, behavior_data):
        """
        Sets the behavior_data of this UserInventoryResource.
        A map of data for behaviors

        :param behavior_data: The behavior_data of this UserInventoryResource.
        :type: object
        """

        self._behavior_data = behavior_data

    @property
    def created_date(self):
        """
        Gets the created_date of this UserInventoryResource.
        The date/time this resource was created in seconds since epoch

        :return: The created_date of this UserInventoryResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this UserInventoryResource.
        The date/time this resource was created in seconds since epoch

        :param created_date: The created_date of this UserInventoryResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def expires(self):
        """
        Gets the expires of this UserInventoryResource.
        The date/time this resource exires in seconds since epoch. Null for no expiration. For subscriptions, this is the end of the 'grace period' if left unpaid

        :return: The expires of this UserInventoryResource.
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """
        Sets the expires of this UserInventoryResource.
        The date/time this resource exires in seconds since epoch. Null for no expiration. For subscriptions, this is the end of the 'grace period' if left unpaid

        :param expires: The expires of this UserInventoryResource.
        :type: int
        """

        self._expires = expires

    @property
    def id(self):
        """
        Gets the id of this UserInventoryResource.
        The id of the inventory

        :return: The id of this UserInventoryResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserInventoryResource.
        The id of the inventory

        :param id: The id of this UserInventoryResource.
        :type: int
        """

        self._id = id

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this UserInventoryResource.
        The id of the invoice that resulted in this inventory, if any

        :return: The invoice_id of this UserInventoryResource.
        :rtype: int
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this UserInventoryResource.
        The id of the invoice that resulted in this inventory, if any

        :param invoice_id: The invoice_id of this UserInventoryResource.
        :type: int
        """

        self._invoice_id = invoice_id

    @property
    def item_id(self):
        """
        Gets the item_id of this UserInventoryResource.
        The id of the item

        :return: The item_id of this UserInventoryResource.
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        Sets the item_id of this UserInventoryResource.
        The id of the item

        :param item_id: The item_id of this UserInventoryResource.
        :type: int
        """

        self._item_id = item_id

    @property
    def item_name(self):
        """
        Gets the item_name of this UserInventoryResource.
        The name of the item

        :return: The item_name of this UserInventoryResource.
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        """
        Sets the item_name of this UserInventoryResource.
        The name of the item

        :param item_name: The item_name of this UserInventoryResource.
        :type: str
        """

        self._item_name = item_name

    @property
    def item_type_hint(self):
        """
        Gets the item_type_hint of this UserInventoryResource.
        The type hint of the item

        :return: The item_type_hint of this UserInventoryResource.
        :rtype: str
        """
        return self._item_type_hint

    @item_type_hint.setter
    def item_type_hint(self, item_type_hint):
        """
        Sets the item_type_hint of this UserInventoryResource.
        The type hint of the item

        :param item_type_hint: The item_type_hint of this UserInventoryResource.
        :type: str
        """

        self._item_type_hint = item_type_hint

    @property
    def status(self):
        """
        Gets the status of this UserInventoryResource.
        The status of the inventory. Pending inventory is not yet ready for use. Inactive inventory has expired or been used up

        :return: The status of this UserInventoryResource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UserInventoryResource.
        The status of the inventory. Pending inventory is not yet ready for use. Inactive inventory has expired or been used up

        :param status: The status of this UserInventoryResource.
        :type: str
        """
        allowed_values = ["pending", "active", "inactive"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def updated_date(self):
        """
        Gets the updated_date of this UserInventoryResource.
        The date/time this resource was last updated in seconds since epoch

        :return: The updated_date of this UserInventoryResource.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this UserInventoryResource.
        The date/time this resource was last updated in seconds since epoch

        :param updated_date: The updated_date of this UserInventoryResource.
        :type: int
        """

        self._updated_date = updated_date

    @property
    def user(self):
        """
        Gets the user of this UserInventoryResource.
        The id of the user this inventory belongs to

        :return: The user of this UserInventoryResource.
        :rtype: SimpleUserResource
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this UserInventoryResource.
        The id of the user this inventory belongs to

        :param user: The user of this UserInventoryResource.
        :type: SimpleUserResource
        """

        self._user = user

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