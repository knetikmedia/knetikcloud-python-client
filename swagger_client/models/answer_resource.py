# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AnswerResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, answer=None, correct=None, id=None):
        """
        AnswerResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'answer': 'ModelProperty',
            'correct': 'bool',
            'id': 'str'
        }

        self.attribute_map = {
            'answer': 'answer',
            'correct': 'correct',
            'id': 'id'
        }

        self._answer = answer
        self._correct = correct
        self._id = id

    @property
    def answer(self):
        """
        Gets the answer of this AnswerResource.
        The answer to the question. Different 'type' values indicate different structures as the answer may be test, image, etc. See information on additional properties for the list and their structures

        :return: The answer of this AnswerResource.
        :rtype: ModelProperty
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """
        Sets the answer of this AnswerResource.
        The answer to the question. Different 'type' values indicate different structures as the answer may be test, image, etc. See information on additional properties for the list and their structures

        :param answer: The answer of this AnswerResource.
        :type: ModelProperty
        """
        if answer is None:
            raise ValueError("Invalid value for `answer`, must not be `None`")

        self._answer = answer

    @property
    def correct(self):
        """
        Gets the correct of this AnswerResource.
        Whether the answer is correct or not

        :return: The correct of this AnswerResource.
        :rtype: bool
        """
        return self._correct

    @correct.setter
    def correct(self, correct):
        """
        Sets the correct of this AnswerResource.
        Whether the answer is correct or not

        :param correct: The correct of this AnswerResource.
        :type: bool
        """
        if correct is None:
            raise ValueError("Invalid value for `correct`, must not be `None`")

        self._correct = correct

    @property
    def id(self):
        """
        Gets the id of this AnswerResource.
        The unique ID for that resource

        :return: The id of this AnswerResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AnswerResource.
        The unique ID for that resource

        :param id: The id of this AnswerResource.
        :type: str
        """

        self._id = id

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
