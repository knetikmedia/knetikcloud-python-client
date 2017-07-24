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


class ForwardLog(object):
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
        'end_date': 'int',
        'error_msg': 'str',
        'http_status_code': 'int',
        'id': 'str',
        'payload': 'object',
        'response': 'str',
        'retry_count': 'int',
        'start_date': 'int',
        'url': 'str'
    }

    attribute_map = {
        'end_date': 'end_date',
        'error_msg': 'error_msg',
        'http_status_code': 'http_status_code',
        'id': 'id',
        'payload': 'payload',
        'response': 'response',
        'retry_count': 'retry_count',
        'start_date': 'start_date',
        'url': 'url'
    }

    def __init__(self, end_date=None, error_msg=None, http_status_code=None, id=None, payload=None, response=None, retry_count=None, start_date=None, url=None):
        """
        ForwardLog - a model defined in Swagger
        """

        self._end_date = None
        self._error_msg = None
        self._http_status_code = None
        self._id = None
        self._payload = None
        self._response = None
        self._retry_count = None
        self._start_date = None
        self._url = None

        if end_date is not None:
          self.end_date = end_date
        if error_msg is not None:
          self.error_msg = error_msg
        if http_status_code is not None:
          self.http_status_code = http_status_code
        if id is not None:
          self.id = id
        if payload is not None:
          self.payload = payload
        if response is not None:
          self.response = response
        if retry_count is not None:
          self.retry_count = retry_count
        if start_date is not None:
          self.start_date = start_date
        if url is not None:
          self.url = url

    @property
    def end_date(self):
        """
        Gets the end_date of this ForwardLog.
        The end date of the forward log entry

        :return: The end_date of this ForwardLog.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this ForwardLog.
        The end date of the forward log entry

        :param end_date: The end_date of this ForwardLog.
        :type: int
        """

        self._end_date = end_date

    @property
    def error_msg(self):
        """
        Gets the error_msg of this ForwardLog.

        :return: The error_msg of this ForwardLog.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """
        Sets the error_msg of this ForwardLog.

        :param error_msg: The error_msg of this ForwardLog.
        :type: str
        """

        self._error_msg = error_msg

    @property
    def http_status_code(self):
        """
        Gets the http_status_code of this ForwardLog.
        The http status code the forward log entry

        :return: The http_status_code of this ForwardLog.
        :rtype: int
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """
        Sets the http_status_code of this ForwardLog.
        The http status code the forward log entry

        :param http_status_code: The http_status_code of this ForwardLog.
        :type: int
        """

        self._http_status_code = http_status_code

    @property
    def id(self):
        """
        Gets the id of this ForwardLog.
        The id of the forward log entry

        :return: The id of this ForwardLog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ForwardLog.
        The id of the forward log entry

        :param id: The id of this ForwardLog.
        :type: str
        """

        self._id = id

    @property
    def payload(self):
        """
        Gets the payload of this ForwardLog.
        The payload of the forward log entry

        :return: The payload of this ForwardLog.
        :rtype: object
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this ForwardLog.
        The payload of the forward log entry

        :param payload: The payload of this ForwardLog.
        :type: object
        """

        self._payload = payload

    @property
    def response(self):
        """
        Gets the response of this ForwardLog.
        The response string of the forward log entry

        :return: The response of this ForwardLog.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """
        Sets the response of this ForwardLog.
        The response string of the forward log entry

        :param response: The response of this ForwardLog.
        :type: str
        """

        self._response = response

    @property
    def retry_count(self):
        """
        Gets the retry_count of this ForwardLog.
        The retry count of the forward log entry

        :return: The retry_count of this ForwardLog.
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """
        Sets the retry_count of this ForwardLog.
        The retry count of the forward log entry

        :param retry_count: The retry_count of this ForwardLog.
        :type: int
        """

        self._retry_count = retry_count

    @property
    def start_date(self):
        """
        Gets the start_date of this ForwardLog.
        The start date of the forward log entry

        :return: The start_date of this ForwardLog.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this ForwardLog.
        The start date of the forward log entry

        :param start_date: The start_date of this ForwardLog.
        :type: int
        """

        self._start_date = start_date

    @property
    def url(self):
        """
        Gets the url of this ForwardLog.
        The endpoint url of the forward log entry

        :return: The url of this ForwardLog.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ForwardLog.
        The endpoint url of the forward log entry

        :param url: The url of this ForwardLog.
        :type: str
        """

        self._url = url

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
        if not isinstance(other, ForwardLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other