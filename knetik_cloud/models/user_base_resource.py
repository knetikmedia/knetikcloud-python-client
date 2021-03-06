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


class UserBaseResource(object):
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
        'avatar_url': 'str',
        'display_name': 'str',
        'email': 'str',
        'fullname': 'str',
        'id': 'int',
        'last_activity': 'int',
        'last_updated': 'int',
        'member_since': 'int',
        'username': 'str'
    }

    attribute_map = {
        'avatar_url': 'avatar_url',
        'display_name': 'display_name',
        'email': 'email',
        'fullname': 'fullname',
        'id': 'id',
        'last_activity': 'last_activity',
        'last_updated': 'last_updated',
        'member_since': 'member_since',
        'username': 'username'
    }

    def __init__(self, avatar_url=None, display_name=None, email=None, fullname=None, id=None, last_activity=None, last_updated=None, member_since=None, username=None):
        """
        UserBaseResource - a model defined in Swagger
        """

        self._avatar_url = None
        self._display_name = None
        self._email = None
        self._fullname = None
        self._id = None
        self._last_activity = None
        self._last_updated = None
        self._member_since = None
        self._username = None
        self.discriminator = None

        if avatar_url is not None:
          self.avatar_url = avatar_url
        if display_name is not None:
          self.display_name = display_name
        self.email = email
        if fullname is not None:
          self.fullname = fullname
        if id is not None:
          self.id = id
        if last_activity is not None:
          self.last_activity = last_activity
        if last_updated is not None:
          self.last_updated = last_updated
        if member_since is not None:
          self.member_since = member_since
        self.username = username

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this UserBaseResource.
        The url of the user's avatar image

        :return: The avatar_url of this UserBaseResource.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this UserBaseResource.
        The url of the user's avatar image

        :param avatar_url: The avatar_url of this UserBaseResource.
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def display_name(self):
        """
        Gets the display_name of this UserBaseResource.
        The chosen display name of the user, defaults to username if not present

        :return: The display_name of this UserBaseResource.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UserBaseResource.
        The chosen display name of the user, defaults to username if not present

        :param display_name: The display_name of this UserBaseResource.
        :type: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """
        Gets the email of this UserBaseResource.
        The user's email address (private). May be required and/or unique depending on system configuration (both on by default). Must match standard email requirements if provided (RFC 2822)

        :return: The email of this UserBaseResource.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserBaseResource.
        The user's email address (private). May be required and/or unique depending on system configuration (both on by default). Must match standard email requirements if provided (RFC 2822)

        :param email: The email of this UserBaseResource.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def fullname(self):
        """
        Gets the fullname of this UserBaseResource.
        The user's full name (private)

        :return: The fullname of this UserBaseResource.
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """
        Sets the fullname of this UserBaseResource.
        The user's full name (private)

        :param fullname: The fullname of this UserBaseResource.
        :type: str
        """

        self._fullname = fullname

    @property
    def id(self):
        """
        Gets the id of this UserBaseResource.
        The id of the user

        :return: The id of this UserBaseResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserBaseResource.
        The id of the user

        :param id: The id of this UserBaseResource.
        :type: int
        """

        self._id = id

    @property
    def last_activity(self):
        """
        Gets the last_activity of this UserBaseResource.
        The date the user last interacted with the API (private)

        :return: The last_activity of this UserBaseResource.
        :rtype: int
        """
        return self._last_activity

    @last_activity.setter
    def last_activity(self, last_activity):
        """
        Sets the last_activity of this UserBaseResource.
        The date the user last interacted with the API (private)

        :param last_activity: The last_activity of this UserBaseResource.
        :type: int
        """

        self._last_activity = last_activity

    @property
    def last_updated(self):
        """
        Gets the last_updated of this UserBaseResource.
        The date the user's info was last updated as a unix timestamp

        :return: The last_updated of this UserBaseResource.
        :rtype: int
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """
        Sets the last_updated of this UserBaseResource.
        The date the user's info was last updated as a unix timestamp

        :param last_updated: The last_updated of this UserBaseResource.
        :type: int
        """

        self._last_updated = last_updated

    @property
    def member_since(self):
        """
        Gets the member_since of this UserBaseResource.
        The user's date of registration as a unix timestamp

        :return: The member_since of this UserBaseResource.
        :rtype: int
        """
        return self._member_since

    @member_since.setter
    def member_since(self, member_since):
        """
        Sets the member_since of this UserBaseResource.
        The user's date of registration as a unix timestamp

        :param member_since: The member_since of this UserBaseResource.
        :type: int
        """

        self._member_since = member_since

    @property
    def username(self):
        """
        Gets the username of this UserBaseResource.
        The login username for the user (private). May be set to match email if system does not require usernames separately.

        :return: The username of this UserBaseResource.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserBaseResource.
        The login username for the user (private). May be set to match email if system does not require usernames separately.

        :param username: The username of this UserBaseResource.
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

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
        if not isinstance(other, UserBaseResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
