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


class UserActivityResults(object):
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
        'currency_rewards': 'list[RewardCurrencyResource]',
        'item_rewards': 'list[RewardItemResource]',
        'rank': 'int',
        'score': 'int',
        'tags': 'list[str]',
        'ties': 'int',
        'updated_date': 'int',
        'user': 'SimpleUserResource'
    }

    attribute_map = {
        'currency_rewards': 'currency_rewards',
        'item_rewards': 'item_rewards',
        'rank': 'rank',
        'score': 'score',
        'tags': 'tags',
        'ties': 'ties',
        'updated_date': 'updated_date',
        'user': 'user'
    }

    def __init__(self, currency_rewards=None, item_rewards=None, rank=None, score=None, tags=None, ties=None, updated_date=None, user=None):
        """
        UserActivityResults - a model defined in Swagger
        """

        self._currency_rewards = None
        self._item_rewards = None
        self._rank = None
        self._score = None
        self._tags = None
        self._ties = None
        self._updated_date = None
        self._user = None

        if currency_rewards is not None:
          self.currency_rewards = currency_rewards
        if item_rewards is not None:
          self.item_rewards = item_rewards
        if rank is not None:
          self.rank = rank
        if score is not None:
          self.score = score
        if tags is not None:
          self.tags = tags
        if ties is not None:
          self.ties = ties
        if updated_date is not None:
          self.updated_date = updated_date
        self.user = user

    @property
    def currency_rewards(self):
        """
        Gets the currency_rewards of this UserActivityResults.
        Any currency rewarded to this user

        :return: The currency_rewards of this UserActivityResults.
        :rtype: list[RewardCurrencyResource]
        """
        return self._currency_rewards

    @currency_rewards.setter
    def currency_rewards(self, currency_rewards):
        """
        Sets the currency_rewards of this UserActivityResults.
        Any currency rewarded to this user

        :param currency_rewards: The currency_rewards of this UserActivityResults.
        :type: list[RewardCurrencyResource]
        """

        self._currency_rewards = currency_rewards

    @property
    def item_rewards(self):
        """
        Gets the item_rewards of this UserActivityResults.
        Any items rewarded to this user

        :return: The item_rewards of this UserActivityResults.
        :rtype: list[RewardItemResource]
        """
        return self._item_rewards

    @item_rewards.setter
    def item_rewards(self, item_rewards):
        """
        Sets the item_rewards of this UserActivityResults.
        Any items rewarded to this user

        :param item_rewards: The item_rewards of this UserActivityResults.
        :type: list[RewardItemResource]
        """

        self._item_rewards = item_rewards

    @property
    def rank(self):
        """
        Gets the rank of this UserActivityResults.
        The position of the user in the leaderboard. Null means non-compete or disqualification

        :return: The rank of this UserActivityResults.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """
        Sets the rank of this UserActivityResults.
        The position of the user in the leaderboard. Null means non-compete or disqualification

        :param rank: The rank of this UserActivityResults.
        :type: int
        """

        self._rank = rank

    @property
    def score(self):
        """
        Gets the score of this UserActivityResults.
        The raw score in this leaderboard. Null means non-compete or disqualification

        :return: The score of this UserActivityResults.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this UserActivityResults.
        The raw score in this leaderboard. Null means non-compete or disqualification

        :param score: The score of this UserActivityResults.
        :type: int
        """

        self._score = score

    @property
    def tags(self):
        """
        Gets the tags of this UserActivityResults.
        Any tags for the metric. Each unique tag will translate into a unique leaderboard. Maximum 5 tags and 50 characters each

        :return: The tags of this UserActivityResults.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this UserActivityResults.
        Any tags for the metric. Each unique tag will translate into a unique leaderboard. Maximum 5 tags and 50 characters each

        :param tags: The tags of this UserActivityResults.
        :type: list[str]
        """

        self._tags = tags

    @property
    def ties(self):
        """
        Gets the ties of this UserActivityResults.
        The number of users tied at this rank, including this user. 1 means no tie

        :return: The ties of this UserActivityResults.
        :rtype: int
        """
        return self._ties

    @ties.setter
    def ties(self, ties):
        """
        Sets the ties of this UserActivityResults.
        The number of users tied at this rank, including this user. 1 means no tie

        :param ties: The ties of this UserActivityResults.
        :type: int
        """

        self._ties = ties

    @property
    def updated_date(self):
        """
        Gets the updated_date of this UserActivityResults.
        The date this score was recorded or updated. Unix timestamp in seconds

        :return: The updated_date of this UserActivityResults.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this UserActivityResults.
        The date this score was recorded or updated. Unix timestamp in seconds

        :param updated_date: The updated_date of this UserActivityResults.
        :type: int
        """

        self._updated_date = updated_date

    @property
    def user(self):
        """
        Gets the user of this UserActivityResults.
        The player for this entry

        :return: The user of this UserActivityResults.
        :rtype: SimpleUserResource
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this UserActivityResults.
        The player for this entry

        :param user: The user of this UserActivityResults.
        :type: SimpleUserResource
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")

        self._user = user

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
        if not isinstance(other, UserActivityResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
