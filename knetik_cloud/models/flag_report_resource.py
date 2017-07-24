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


class FlagReportResource(object):
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
        'context': 'str',
        'context_id': 'str',
        'created_date': 'int',
        'id': 'int',
        'reason': 'str',
        'resolution': 'str',
        'resolved': 'int',
        'updated_date': 'int'
    }

    attribute_map = {
        'context': 'context',
        'context_id': 'context_id',
        'created_date': 'created_date',
        'id': 'id',
        'reason': 'reason',
        'resolution': 'resolution',
        'resolved': 'resolved',
        'updated_date': 'updated_date'
    }

    def __init__(self, context=None, context_id=None, created_date=None, id=None, reason=None, resolution=None, resolved=None, updated_date=None):
        """
        FlagReportResource - a model defined in Swagger
        """

        self._context = None
        self._context_id = None
        self._created_date = None
        self._id = None
        self._reason = None
        self._resolution = None
        self._resolved = None
        self._updated_date = None

        if context is not None:
          self.context = context
        if context_id is not None:
          self.context_id = context_id
        if created_date is not None:
          self.created_date = created_date
        if id is not None:
          self.id = id
        if reason is not None:
          self.reason = reason
        self.resolution = resolution
        if resolved is not None:
          self.resolved = resolved
        if updated_date is not None:
          self.updated_date = updated_date

    @property
    def context(self):
        """
        Gets the context of this FlagReportResource.
        The context of that resource 

        :return: The context of this FlagReportResource.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this FlagReportResource.
        The context of that resource 

        :param context: The context of this FlagReportResource.
        :type: str
        """

        self._context = context

    @property
    def context_id(self):
        """
        Gets the context_id of this FlagReportResource.
        The context ID of that resource

        :return: The context_id of this FlagReportResource.
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id):
        """
        Sets the context_id of this FlagReportResource.
        The context ID of that resource

        :param context_id: The context_id of this FlagReportResource.
        :type: str
        """

        self._context_id = context_id

    @property
    def created_date(self):
        """
        Gets the created_date of this FlagReportResource.
        The date/time this resource was created in seconds since epoch

        :return: The created_date of this FlagReportResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this FlagReportResource.
        The date/time this resource was created in seconds since epoch

        :param created_date: The created_date of this FlagReportResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def id(self):
        """
        Gets the id of this FlagReportResource.
        The unique ID for that resource

        :return: The id of this FlagReportResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FlagReportResource.
        The unique ID for that resource

        :param id: The id of this FlagReportResource.
        :type: int
        """

        self._id = id

    @property
    def reason(self):
        """
        Gets the reason of this FlagReportResource.
        The reason of that resource required only in case of active resolution

        :return: The reason of this FlagReportResource.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this FlagReportResource.
        The reason of that resource required only in case of active resolution

        :param reason: The reason of this FlagReportResource.
        :type: str
        """

        self._reason = reason

    @property
    def resolution(self):
        """
        Gets the resolution of this FlagReportResource.
        The resolution of that resource

        :return: The resolution of this FlagReportResource.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """
        Sets the resolution of this FlagReportResource.
        The resolution of that resource

        :param resolution: The resolution of this FlagReportResource.
        :type: str
        """
        if resolution is None:
            raise ValueError("Invalid value for `resolution`, must not be `None`")
        allowed_values = ["banned", "ignored"]
        if resolution not in allowed_values:
            raise ValueError(
                "Invalid value for `resolution` ({0}), must be one of {1}"
                .format(resolution, allowed_values)
            )

        self._resolution = resolution

    @property
    def resolved(self):
        """
        Gets the resolved of this FlagReportResource.
        The date/time this report was resolved in seconds since epoch. Null if not resolved yet

        :return: The resolved of this FlagReportResource.
        :rtype: int
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        """
        Sets the resolved of this FlagReportResource.
        The date/time this report was resolved in seconds since epoch. Null if not resolved yet

        :param resolved: The resolved of this FlagReportResource.
        :type: int
        """

        self._resolved = resolved

    @property
    def updated_date(self):
        """
        Gets the updated_date of this FlagReportResource.
        The date/time this resource was last updated in seconds since epoch

        :return: The updated_date of this FlagReportResource.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this FlagReportResource.
        The date/time this resource was last updated in seconds since epoch

        :param updated_date: The updated_date of this FlagReportResource.
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
        if not isinstance(other, FlagReportResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
