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


class DeviceResource(object):
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
        'authorization': 'str',
        'condition': 'str',
        'created_date': 'int',
        'data': 'dict(str, str)',
        'description': 'str',
        'device_type': 'str',
        'id': 'int',
        'location': 'str',
        'mac_address': 'str',
        'make': 'str',
        'model': 'str',
        'name': 'str',
        'os': 'str',
        'serial': 'str',
        'status': 'str',
        'updated_date': 'int',
        'user': 'SimpleUserResource',
        'users': 'list[SimpleUserResource]'
    }

    attribute_map = {
        'authorization': 'authorization',
        'condition': 'condition',
        'created_date': 'created_date',
        'data': 'data',
        'description': 'description',
        'device_type': 'device_type',
        'id': 'id',
        'location': 'location',
        'mac_address': 'mac_address',
        'make': 'make',
        'model': 'model',
        'name': 'name',
        'os': 'os',
        'serial': 'serial',
        'status': 'status',
        'updated_date': 'updated_date',
        'user': 'user',
        'users': 'users'
    }

    def __init__(self, authorization=None, condition=None, created_date=None, data=None, description=None, device_type=None, id=None, location=None, mac_address=None, make=None, model=None, name=None, os=None, serial=None, status=None, updated_date=None, user=None, users=None):
        """
        DeviceResource - a model defined in Swagger
        """

        self._authorization = None
        self._condition = None
        self._created_date = None
        self._data = None
        self._description = None
        self._device_type = None
        self._id = None
        self._location = None
        self._mac_address = None
        self._make = None
        self._model = None
        self._name = None
        self._os = None
        self._serial = None
        self._status = None
        self._updated_date = None
        self._user = None
        self._users = None
        self.discriminator = None

        if authorization is not None:
          self.authorization = authorization
        if condition is not None:
          self.condition = condition
        if created_date is not None:
          self.created_date = created_date
        if data is not None:
          self.data = data
        if description is not None:
          self.description = description
        if device_type is not None:
          self.device_type = device_type
        self.id = id
        if location is not None:
          self.location = location
        if mac_address is not None:
          self.mac_address = mac_address
        if make is not None:
          self.make = make
        if model is not None:
          self.model = model
        if name is not None:
          self.name = name
        if os is not None:
          self.os = os
        if serial is not None:
          self.serial = serial
        if status is not None:
          self.status = status
        if updated_date is not None:
          self.updated_date = updated_date
        if user is not None:
          self.user = user
        if users is not None:
          self.users = users

    @property
    def authorization(self):
        """
        Gets the authorization of this DeviceResource.
        The authorization code for the device

        :return: The authorization of this DeviceResource.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """
        Sets the authorization of this DeviceResource.
        The authorization code for the device

        :param authorization: The authorization of this DeviceResource.
        :type: str
        """

        self._authorization = authorization

    @property
    def condition(self):
        """
        Gets the condition of this DeviceResource.
        The current condition of the device (New, Defective, Reconditioned)

        :return: The condition of this DeviceResource.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this DeviceResource.
        The current condition of the device (New, Defective, Reconditioned)

        :param condition: The condition of this DeviceResource.
        :type: str
        """
        allowed_values = ["New", "Defective", "Reconditioned"]
        if condition not in allowed_values:
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def created_date(self):
        """
        Gets the created_date of this DeviceResource.
        The date the device log was created

        :return: The created_date of this DeviceResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this DeviceResource.
        The date the device log was created

        :param created_date: The created_date of this DeviceResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def data(self):
        """
        Gets the data of this DeviceResource.
        The key/value pairs for extended data

        :return: The data of this DeviceResource.
        :rtype: dict(str, str)
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this DeviceResource.
        The key/value pairs for extended data

        :param data: The data of this DeviceResource.
        :type: dict(str, str)
        """

        self._data = data

    @property
    def description(self):
        """
        Gets the description of this DeviceResource.
        The description of the device

        :return: The description of this DeviceResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeviceResource.
        The description of the device

        :param description: The description of this DeviceResource.
        :type: str
        """

        self._description = description

    @property
    def device_type(self):
        """
        Gets the device_type of this DeviceResource.
        The type of the device

        :return: The device_type of this DeviceResource.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """
        Sets the device_type of this DeviceResource.
        The type of the device

        :param device_type: The device_type of this DeviceResource.
        :type: str
        """

        self._device_type = device_type

    @property
    def id(self):
        """
        Gets the id of this DeviceResource.
        The unique ID for this device. Cannot be changed once created

        :return: The id of this DeviceResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeviceResource.
        The unique ID for this device. Cannot be changed once created

        :param id: The id of this DeviceResource.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def location(self):
        """
        Gets the location of this DeviceResource.
        The location of the device

        :return: The location of this DeviceResource.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this DeviceResource.
        The location of the device

        :param location: The location of this DeviceResource.
        :type: str
        """

        self._location = location

    @property
    def mac_address(self):
        """
        Gets the mac_address of this DeviceResource.
        The MAC (media access control) address of the device

        :return: The mac_address of this DeviceResource.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this DeviceResource.
        The MAC (media access control) address of the device

        :param mac_address: The mac_address of this DeviceResource.
        :type: str
        """

        self._mac_address = mac_address

    @property
    def make(self):
        """
        Gets the make of this DeviceResource.
        The make of the device

        :return: The make of this DeviceResource.
        :rtype: str
        """
        return self._make

    @make.setter
    def make(self, make):
        """
        Sets the make of this DeviceResource.
        The make of the device

        :param make: The make of this DeviceResource.
        :type: str
        """

        self._make = make

    @property
    def model(self):
        """
        Gets the model of this DeviceResource.
        The model of the device

        :return: The model of this DeviceResource.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this DeviceResource.
        The model of the device

        :param model: The model of this DeviceResource.
        :type: str
        """

        self._model = model

    @property
    def name(self):
        """
        Gets the name of this DeviceResource.
        The name of the device

        :return: The name of this DeviceResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceResource.
        The name of the device

        :param name: The name of this DeviceResource.
        :type: str
        """

        self._name = name

    @property
    def os(self):
        """
        Gets the os of this DeviceResource.
        The OS (operating system) on the device

        :return: The os of this DeviceResource.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this DeviceResource.
        The OS (operating system) on the device

        :param os: The os of this DeviceResource.
        :type: str
        """

        self._os = os

    @property
    def serial(self):
        """
        Gets the serial of this DeviceResource.
        The serial number of the device

        :return: The serial of this DeviceResource.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this DeviceResource.
        The serial number of the device

        :param serial: The serial of this DeviceResource.
        :type: str
        """

        self._serial = serial

    @property
    def status(self):
        """
        Gets the status of this DeviceResource.
        The current status the device (Active, Pending Active, Inactive, Repair

        :return: The status of this DeviceResource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DeviceResource.
        The current status the device (Active, Pending Active, Inactive, Repair

        :param status: The status of this DeviceResource.
        :type: str
        """
        allowed_values = ["Active", "PendingActive", "Inactive", "Repair"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def updated_date(self):
        """
        Gets the updated_date of this DeviceResource.
        The date the device log was updated

        :return: The updated_date of this DeviceResource.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this DeviceResource.
        The date the device log was updated

        :param updated_date: The updated_date of this DeviceResource.
        :type: int
        """

        self._updated_date = updated_date

    @property
    def user(self):
        """
        Gets the user of this DeviceResource.
        The user that owns the device

        :return: The user of this DeviceResource.
        :rtype: SimpleUserResource
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this DeviceResource.
        The user that owns the device

        :param user: The user of this DeviceResource.
        :type: SimpleUserResource
        """

        self._user = user

    @property
    def users(self):
        """
        Gets the users of this DeviceResource.
        The users currently using the device

        :return: The users of this DeviceResource.
        :rtype: list[SimpleUserResource]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this DeviceResource.
        The users currently using the device

        :param users: The users of this DeviceResource.
        :type: list[SimpleUserResource]
        """

        self._users = users

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
        if not isinstance(other, DeviceResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
