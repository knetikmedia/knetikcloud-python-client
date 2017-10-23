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


class OptimalPaymentRequest(object):
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
        'email': 'str',
        'first_name': 'str',
        'invoice_id': 'int',
        'last_name': 'str',
        'on_decline': 'str',
        'on_error': 'str',
        'on_success': 'str'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'first_name',
        'invoice_id': 'invoice_id',
        'last_name': 'last_name',
        'on_decline': 'on_decline',
        'on_error': 'on_error',
        'on_success': 'on_success'
    }

    def __init__(self, email=None, first_name=None, invoice_id=None, last_name=None, on_decline=None, on_error=None, on_success=None):
        """
        OptimalPaymentRequest - a model defined in Swagger
        """

        self._email = None
        self._first_name = None
        self._invoice_id = None
        self._last_name = None
        self._on_decline = None
        self._on_error = None
        self._on_success = None
        self.discriminator = None

        if email is not None:
          self.email = email
        if first_name is not None:
          self.first_name = first_name
        self.invoice_id = invoice_id
        if last_name is not None:
          self.last_name = last_name
        self.on_decline = on_decline
        self.on_error = on_error
        self.on_success = on_success

    @property
    def email(self):
        """
        Gets the email of this OptimalPaymentRequest.
        The email address of the user

        :return: The email of this OptimalPaymentRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this OptimalPaymentRequest.
        The email address of the user

        :param email: The email of this OptimalPaymentRequest.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this OptimalPaymentRequest.
        The first name of the user

        :return: The first_name of this OptimalPaymentRequest.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this OptimalPaymentRequest.
        The first name of the user

        :param first_name: The first_name of this OptimalPaymentRequest.
        :type: str
        """

        self._first_name = first_name

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this OptimalPaymentRequest.
        The id of the invoice to pay

        :return: The invoice_id of this OptimalPaymentRequest.
        :rtype: int
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this OptimalPaymentRequest.
        The id of the invoice to pay

        :param invoice_id: The invoice_id of this OptimalPaymentRequest.
        :type: int
        """
        if invoice_id is None:
            raise ValueError("Invalid value for `invoice_id`, must not be `None`")

        self._invoice_id = invoice_id

    @property
    def last_name(self):
        """
        Gets the last_name of this OptimalPaymentRequest.
        The last name of the user

        :return: The last_name of this OptimalPaymentRequest.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this OptimalPaymentRequest.
        The last name of the user

        :param last_name: The last_name of this OptimalPaymentRequest.
        :type: str
        """

        self._last_name = last_name

    @property
    def on_decline(self):
        """
        Gets the on_decline of this OptimalPaymentRequest.
        The url to redirect the user to after declining payment

        :return: The on_decline of this OptimalPaymentRequest.
        :rtype: str
        """
        return self._on_decline

    @on_decline.setter
    def on_decline(self, on_decline):
        """
        Sets the on_decline of this OptimalPaymentRequest.
        The url to redirect the user to after declining payment

        :param on_decline: The on_decline of this OptimalPaymentRequest.
        :type: str
        """
        if on_decline is None:
            raise ValueError("Invalid value for `on_decline`, must not be `None`")

        self._on_decline = on_decline

    @property
    def on_error(self):
        """
        Gets the on_error of this OptimalPaymentRequest.
        The url to redirect the user to after an error in payment

        :return: The on_error of this OptimalPaymentRequest.
        :rtype: str
        """
        return self._on_error

    @on_error.setter
    def on_error(self, on_error):
        """
        Sets the on_error of this OptimalPaymentRequest.
        The url to redirect the user to after an error in payment

        :param on_error: The on_error of this OptimalPaymentRequest.
        :type: str
        """
        if on_error is None:
            raise ValueError("Invalid value for `on_error`, must not be `None`")

        self._on_error = on_error

    @property
    def on_success(self):
        """
        Gets the on_success of this OptimalPaymentRequest.
        The url to redirect the user to after successful payment

        :return: The on_success of this OptimalPaymentRequest.
        :rtype: str
        """
        return self._on_success

    @on_success.setter
    def on_success(self, on_success):
        """
        Sets the on_success of this OptimalPaymentRequest.
        The url to redirect the user to after successful payment

        :param on_success: The on_success of this OptimalPaymentRequest.
        :type: str
        """
        if on_success is None:
            raise ValueError("Invalid value for `on_success`, must not be `None`")

        self._on_success = on_success

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
        if not isinstance(other, OptimalPaymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
