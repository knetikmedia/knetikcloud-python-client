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


class NotificationTypeResource(object):
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
        'email_body_template_external': 'bool',
        'email_body_template_id': 'str',
        'email_subject_template_id': 'str',
        'id': 'str',
        'name': 'str',
        'sms_template_id': 'str',
        'updated_date': 'int'
    }

    attribute_map = {
        'created_date': 'created_date',
        'email_body_template_external': 'email_body_template_external',
        'email_body_template_id': 'email_body_template_id',
        'email_subject_template_id': 'email_subject_template_id',
        'id': 'id',
        'name': 'name',
        'sms_template_id': 'sms_template_id',
        'updated_date': 'updated_date'
    }

    def __init__(self, created_date=None, email_body_template_external=None, email_body_template_id=None, email_subject_template_id=None, id=None, name=None, sms_template_id=None, updated_date=None):
        """
        NotificationTypeResource - a model defined in Swagger
        """

        self._created_date = None
        self._email_body_template_external = None
        self._email_body_template_id = None
        self._email_subject_template_id = None
        self._id = None
        self._name = None
        self._sms_template_id = None
        self._updated_date = None
        self.discriminator = None

        if created_date is not None:
          self.created_date = created_date
        if email_body_template_external is not None:
          self.email_body_template_external = email_body_template_external
        if email_body_template_id is not None:
          self.email_body_template_id = email_body_template_id
        if email_subject_template_id is not None:
          self.email_subject_template_id = email_subject_template_id
        if id is not None:
          self.id = id
        self.name = name
        if sms_template_id is not None:
          self.sms_template_id = sms_template_id
        if updated_date is not None:
          self.updated_date = updated_date

    @property
    def created_date(self):
        """
        Gets the created_date of this NotificationTypeResource.
        The date the type was created, as a unix timestamp in seconds

        :return: The created_date of this NotificationTypeResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this NotificationTypeResource.
        The date the type was created, as a unix timestamp in seconds

        :param created_date: The created_date of this NotificationTypeResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def email_body_template_external(self):
        """
        Gets the email_body_template_external of this NotificationTypeResource.
        Whether the email body should be resolved. If true, the external email delivery system will be expected to handle the templating (Mandrill/Mailchimp). default: false

        :return: The email_body_template_external of this NotificationTypeResource.
        :rtype: bool
        """
        return self._email_body_template_external

    @email_body_template_external.setter
    def email_body_template_external(self, email_body_template_external):
        """
        Sets the email_body_template_external of this NotificationTypeResource.
        Whether the email body should be resolved. If true, the external email delivery system will be expected to handle the templating (Mandrill/Mailchimp). default: false

        :param email_body_template_external: The email_body_template_external of this NotificationTypeResource.
        :type: bool
        """

        self._email_body_template_external = email_body_template_external

    @property
    def email_body_template_id(self):
        """
        Gets the email_body_template_id of this NotificationTypeResource.
        The id of a message template to resolve the email body. If null, no websocket message wil be sent

        :return: The email_body_template_id of this NotificationTypeResource.
        :rtype: str
        """
        return self._email_body_template_id

    @email_body_template_id.setter
    def email_body_template_id(self, email_body_template_id):
        """
        Sets the email_body_template_id of this NotificationTypeResource.
        The id of a message template to resolve the email body. If null, no websocket message wil be sent

        :param email_body_template_id: The email_body_template_id of this NotificationTypeResource.
        :type: str
        """

        self._email_body_template_id = email_body_template_id

    @property
    def email_subject_template_id(self):
        """
        Gets the email_subject_template_id of this NotificationTypeResource.
        The id of a message template to resolve the email subject. If null, no websocket message wil be sent

        :return: The email_subject_template_id of this NotificationTypeResource.
        :rtype: str
        """
        return self._email_subject_template_id

    @email_subject_template_id.setter
    def email_subject_template_id(self, email_subject_template_id):
        """
        Sets the email_subject_template_id of this NotificationTypeResource.
        The id of a message template to resolve the email subject. If null, no websocket message wil be sent

        :param email_subject_template_id: The email_subject_template_id of this NotificationTypeResource.
        :type: str
        """

        self._email_subject_template_id = email_subject_template_id

    @property
    def id(self):
        """
        Gets the id of this NotificationTypeResource.
        The id of the notification type. Default: random

        :return: The id of this NotificationTypeResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NotificationTypeResource.
        The id of the notification type. Default: random

        :param id: The id of this NotificationTypeResource.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this NotificationTypeResource.
        The name of the notification type

        :return: The name of this NotificationTypeResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NotificationTypeResource.
        The name of the notification type

        :param name: The name of this NotificationTypeResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def sms_template_id(self):
        """
        Gets the sms_template_id of this NotificationTypeResource.
        The id of a message template to resolve the SMS message. If null, no sms message wil be sent

        :return: The sms_template_id of this NotificationTypeResource.
        :rtype: str
        """
        return self._sms_template_id

    @sms_template_id.setter
    def sms_template_id(self, sms_template_id):
        """
        Sets the sms_template_id of this NotificationTypeResource.
        The id of a message template to resolve the SMS message. If null, no sms message wil be sent

        :param sms_template_id: The sms_template_id of this NotificationTypeResource.
        :type: str
        """

        self._sms_template_id = sms_template_id

    @property
    def updated_date(self):
        """
        Gets the updated_date of this NotificationTypeResource.
        The date the type was last updated, as a unix timestamp in seconds

        :return: The updated_date of this NotificationTypeResource.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this NotificationTypeResource.
        The date the type was last updated, as a unix timestamp in seconds

        :param updated_date: The updated_date of this NotificationTypeResource.
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
        if not isinstance(other, NotificationTypeResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other