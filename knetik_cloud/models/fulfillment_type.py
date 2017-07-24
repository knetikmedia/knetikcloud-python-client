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


class FulfillmentType(object):
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
        'core': 'bool',
        'description': 'str',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'core': 'core',
        'description': 'description',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, core=None, description=None, id=None, name=None):
        """
        FulfillmentType - a model defined in Swagger
        """

        self._core = None
        self._description = None
        self._id = None
        self._name = None

        if core is not None:
          self.core = core
        if description is not None:
          self.description = description
        if id is not None:
          self.id = id
        self.name = name

    @property
    def core(self):
        """
        Gets the core of this FulfillmentType.
        Whether the type is core and cannot be altered/deleted, read-only

        :return: The core of this FulfillmentType.
        :rtype: bool
        """
        return self._core

    @core.setter
    def core(self, core):
        """
        Sets the core of this FulfillmentType.
        Whether the type is core and cannot be altered/deleted, read-only

        :param core: The core of this FulfillmentType.
        :type: bool
        """

        self._core = core

    @property
    def description(self):
        """
        Gets the description of this FulfillmentType.
        A description of the type

        :return: The description of this FulfillmentType.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FulfillmentType.
        A description of the type

        :param description: The description of this FulfillmentType.
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """
        Gets the id of this FulfillmentType.
        The unique id of the type, read-only

        :return: The id of this FulfillmentType.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FulfillmentType.
        The unique id of the type, read-only

        :param id: The id of this FulfillmentType.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FulfillmentType.
        The name of the type

        :return: The name of this FulfillmentType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FulfillmentType.
        The name of the type

        :param name: The name of this FulfillmentType.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, FulfillmentType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
