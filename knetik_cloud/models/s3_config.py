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


class S3Config(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, bucket_name=None, cdn_url=None, region=None, upload_prefix=None):
        """
        S3Config - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'bucket_name': 'str',
            'cdn_url': 'str',
            'region': 'str',
            'upload_prefix': 'str'
        }

        self.attribute_map = {
            'bucket_name': 'bucket_name',
            'cdn_url': 'cdn_url',
            'region': 'region',
            'upload_prefix': 'upload_prefix'
        }

        self._bucket_name = bucket_name
        self._cdn_url = cdn_url
        self._region = region
        self._upload_prefix = upload_prefix

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this S3Config.

        :return: The bucket_name of this S3Config.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this S3Config.

        :param bucket_name: The bucket_name of this S3Config.
        :type: str
        """

        self._bucket_name = bucket_name

    @property
    def cdn_url(self):
        """
        Gets the cdn_url of this S3Config.

        :return: The cdn_url of this S3Config.
        :rtype: str
        """
        return self._cdn_url

    @cdn_url.setter
    def cdn_url(self, cdn_url):
        """
        Sets the cdn_url of this S3Config.

        :param cdn_url: The cdn_url of this S3Config.
        :type: str
        """

        self._cdn_url = cdn_url

    @property
    def region(self):
        """
        Gets the region of this S3Config.

        :return: The region of this S3Config.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this S3Config.

        :param region: The region of this S3Config.
        :type: str
        """

        self._region = region

    @property
    def upload_prefix(self):
        """
        Gets the upload_prefix of this S3Config.

        :return: The upload_prefix of this S3Config.
        :rtype: str
        """
        return self._upload_prefix

    @upload_prefix.setter
    def upload_prefix(self, upload_prefix):
        """
        Sets the upload_prefix of this S3Config.

        :param upload_prefix: The upload_prefix of this S3Config.
        :type: str
        """

        self._upload_prefix = upload_prefix

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
        if not isinstance(other, S3Config):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
