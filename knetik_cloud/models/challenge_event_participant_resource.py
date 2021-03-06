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


class ChallengeEventParticipantResource(object):
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
        'fullname': 'str',
        'score': 'int',
        'user_id': 'int',
        'username': 'str'
    }

    attribute_map = {
        'email': 'email',
        'fullname': 'fullname',
        'score': 'score',
        'user_id': 'user_id',
        'username': 'username'
    }

    def __init__(self, email=None, fullname=None, score=None, user_id=None, username=None):
        """
        ChallengeEventParticipantResource - a model defined in Swagger
        """

        self._email = None
        self._fullname = None
        self._score = None
        self._user_id = None
        self._username = None
        self.discriminator = None

        if email is not None:
          self.email = email
        if fullname is not None:
          self.fullname = fullname
        if score is not None:
          self.score = score
        if user_id is not None:
          self.user_id = user_id
        if username is not None:
          self.username = username

    @property
    def email(self):
        """
        Gets the email of this ChallengeEventParticipantResource.
        The email address of the user

        :return: The email of this ChallengeEventParticipantResource.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ChallengeEventParticipantResource.
        The email address of the user

        :param email: The email of this ChallengeEventParticipantResource.
        :type: str
        """

        self._email = email

    @property
    def fullname(self):
        """
        Gets the fullname of this ChallengeEventParticipantResource.
        The full name of the user

        :return: The fullname of this ChallengeEventParticipantResource.
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """
        Sets the fullname of this ChallengeEventParticipantResource.
        The full name of the user

        :param fullname: The fullname of this ChallengeEventParticipantResource.
        :type: str
        """

        self._fullname = fullname

    @property
    def score(self):
        """
        Gets the score of this ChallengeEventParticipantResource.
        The user's score

        :return: The score of this ChallengeEventParticipantResource.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this ChallengeEventParticipantResource.
        The user's score

        :param score: The score of this ChallengeEventParticipantResource.
        :type: int
        """

        self._score = score

    @property
    def user_id(self):
        """
        Gets the user_id of this ChallengeEventParticipantResource.
        The id of the user

        :return: The user_id of this ChallengeEventParticipantResource.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ChallengeEventParticipantResource.
        The id of the user

        :param user_id: The user_id of this ChallengeEventParticipantResource.
        :type: int
        """

        self._user_id = user_id

    @property
    def username(self):
        """
        Gets the username of this ChallengeEventParticipantResource.
        The username of the user

        :return: The username of this ChallengeEventParticipantResource.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this ChallengeEventParticipantResource.
        The username of the user

        :param username: The username of this ChallengeEventParticipantResource.
        :type: str
        """

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
        if not isinstance(other, ChallengeEventParticipantResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
