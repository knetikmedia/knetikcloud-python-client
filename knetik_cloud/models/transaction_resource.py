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


class TransactionResource(object):
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
        'create_date': 'int',
        'currency_code': 'str',
        'details': 'str',
        'id': 'int',
        'invoice_id': 'int',
        'is_refunded': 'bool',
        'response': 'str',
        'source': 'str',
        'successful': 'bool',
        'transaction_id': 'str',
        'type': 'str',
        'type_hint': 'str',
        'value': 'float'
    }

    attribute_map = {
        'create_date': 'create_date',
        'currency_code': 'currency_code',
        'details': 'details',
        'id': 'id',
        'invoice_id': 'invoice_id',
        'is_refunded': 'is_refunded',
        'response': 'response',
        'source': 'source',
        'successful': 'successful',
        'transaction_id': 'transaction_id',
        'type': 'type',
        'type_hint': 'type_hint',
        'value': 'value'
    }

    def __init__(self, create_date=None, currency_code=None, details=None, id=None, invoice_id=None, is_refunded=None, response=None, source=None, successful=None, transaction_id=None, type=None, type_hint=None, value=None):
        """
        TransactionResource - a model defined in Swagger
        """

        self._create_date = None
        self._currency_code = None
        self._details = None
        self._id = None
        self._invoice_id = None
        self._is_refunded = None
        self._response = None
        self._source = None
        self._successful = None
        self._transaction_id = None
        self._type = None
        self._type_hint = None
        self._value = None
        self.discriminator = None

        if create_date is not None:
          self.create_date = create_date
        if currency_code is not None:
          self.currency_code = currency_code
        if details is not None:
          self.details = details
        if id is not None:
          self.id = id
        if invoice_id is not None:
          self.invoice_id = invoice_id
        if is_refunded is not None:
          self.is_refunded = is_refunded
        if response is not None:
          self.response = response
        if source is not None:
          self.source = source
        if successful is not None:
          self.successful = successful
        if transaction_id is not None:
          self.transaction_id = transaction_id
        if type is not None:
          self.type = type
        if type_hint is not None:
          self.type_hint = type_hint
        if value is not None:
          self.value = value

    @property
    def create_date(self):
        """
        Gets the create_date of this TransactionResource.
        The unix timestamp in seconds of the transaction

        :return: The create_date of this TransactionResource.
        :rtype: int
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this TransactionResource.
        The unix timestamp in seconds of the transaction

        :param create_date: The create_date of this TransactionResource.
        :type: int
        """

        self._create_date = create_date

    @property
    def currency_code(self):
        """
        Gets the currency_code of this TransactionResource.
        The code of the currency for the transaction

        :return: The currency_code of this TransactionResource.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this TransactionResource.
        The code of the currency for the transaction

        :param currency_code: The currency_code of this TransactionResource.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def details(self):
        """
        Gets the details of this TransactionResource.
        The specific details of the transaction, such as a message from the admin that created it

        :return: The details of this TransactionResource.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this TransactionResource.
        The specific details of the transaction, such as a message from the admin that created it

        :param details: The details of this TransactionResource.
        :type: str
        """

        self._details = details

    @property
    def id(self):
        """
        Gets the id of this TransactionResource.
        The id of the transaction

        :return: The id of this TransactionResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TransactionResource.
        The id of the transaction

        :param id: The id of this TransactionResource.
        :type: int
        """

        self._id = id

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this TransactionResource.
        The id of the invoice that spawned the transaction, if any

        :return: The invoice_id of this TransactionResource.
        :rtype: int
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this TransactionResource.
        The id of the invoice that spawned the transaction, if any

        :param invoice_id: The invoice_id of this TransactionResource.
        :type: int
        """

        self._invoice_id = invoice_id

    @property
    def is_refunded(self):
        """
        Gets the is_refunded of this TransactionResource.
        Whether the transaction has been refunded

        :return: The is_refunded of this TransactionResource.
        :rtype: bool
        """
        return self._is_refunded

    @is_refunded.setter
    def is_refunded(self, is_refunded):
        """
        Sets the is_refunded of this TransactionResource.
        Whether the transaction has been refunded

        :param is_refunded: The is_refunded of this TransactionResource.
        :type: bool
        """

        self._is_refunded = is_refunded

    @property
    def response(self):
        """
        Gets the response of this TransactionResource.
        The response

        :return: The response of this TransactionResource.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """
        Sets the response of this TransactionResource.
        The response

        :param response: The response of this TransactionResource.
        :type: str
        """

        self._response = response

    @property
    def source(self):
        """
        Gets the source of this TransactionResource.
        The root source of the transaction

        :return: The source of this TransactionResource.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this TransactionResource.
        The root source of the transaction

        :param source: The source of this TransactionResource.
        :type: str
        """
        allowed_values = ["digital", "physical"]
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def successful(self):
        """
        Gets the successful of this TransactionResource.
        If the transaction was successful

        :return: The successful of this TransactionResource.
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """
        Sets the successful of this TransactionResource.
        If the transaction was successful

        :param successful: The successful of this TransactionResource.
        :type: bool
        """

        self._successful = successful

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this TransactionResource.
        The payment gateway (external) transaction ID

        :return: The transaction_id of this TransactionResource.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this TransactionResource.
        The payment gateway (external) transaction ID

        :param transaction_id: The transaction_id of this TransactionResource.
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def type(self):
        """
        Gets the type of this TransactionResource.
        The general type of the transaction

        :return: The type of this TransactionResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TransactionResource.
        The general type of the transaction

        :param type: The type of this TransactionResource.
        :type: str
        """

        self._type = type

    @property
    def type_hint(self):
        """
        Gets the type_hint of this TransactionResource.
        The table name of the subclass

        :return: The type_hint of this TransactionResource.
        :rtype: str
        """
        return self._type_hint

    @type_hint.setter
    def type_hint(self, type_hint):
        """
        Sets the type_hint of this TransactionResource.
        The table name of the subclass

        :param type_hint: The type_hint of this TransactionResource.
        :type: str
        """

        self._type_hint = type_hint

    @property
    def value(self):
        """
        Gets the value of this TransactionResource.
        The amount of the transaction, positive if a gain, negative if an expenditure

        :return: The value of this TransactionResource.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this TransactionResource.
        The amount of the transaction, positive if a gain, negative if an expenditure

        :param value: The value of this TransactionResource.
        :type: float
        """

        self._value = value

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
        if not isinstance(other, TransactionResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
