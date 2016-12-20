# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CampaignResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active=None, additional_properties=None, created_date=None, id=None, leaderboard_strategy=None, long_description=None, name=None, next_challenge=None, next_challenge_date=None, reward_set=None, reward_status=None, short_description=None, template=None, updated_date=None):
        """
        CampaignResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active': 'bool',
            'additional_properties': 'dict(str, ModelProperty)',
            'created_date': 'int',
            'id': 'int',
            'leaderboard_strategy': 'str',
            'long_description': 'str',
            'name': 'str',
            'next_challenge': 'str',
            'next_challenge_date': 'int',
            'reward_set': 'RewardSetResource',
            'reward_status': 'str',
            'short_description': 'str',
            'template': 'str',
            'updated_date': 'int'
        }

        self.attribute_map = {
            'active': 'active',
            'additional_properties': 'additional_properties',
            'created_date': 'created_date',
            'id': 'id',
            'leaderboard_strategy': 'leaderboard_strategy',
            'long_description': 'long_description',
            'name': 'name',
            'next_challenge': 'next_challenge',
            'next_challenge_date': 'next_challenge_date',
            'reward_set': 'reward_set',
            'reward_status': 'reward_status',
            'short_description': 'short_description',
            'template': 'template',
            'updated_date': 'updated_date'
        }

        self._active = active
        self._additional_properties = additional_properties
        self._created_date = created_date
        self._id = id
        self._leaderboard_strategy = leaderboard_strategy
        self._long_description = long_description
        self._name = name
        self._next_challenge = next_challenge
        self._next_challenge_date = next_challenge_date
        self._reward_set = reward_set
        self._reward_status = reward_status
        self._short_description = short_description
        self._template = template
        self._updated_date = updated_date

    @property
    def active(self):
        """
        Gets the active of this CampaignResource.
        Whether the campaign is active or not.  Defaults to false

        :return: The active of this CampaignResource.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this CampaignResource.
        Whether the campaign is active or not.  Defaults to false

        :param active: The active of this CampaignResource.
        :type: bool
        """

        self._active = active

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this CampaignResource.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type

        :return: The additional_properties of this CampaignResource.
        :rtype: dict(str, ModelProperty)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this CampaignResource.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type

        :param additional_properties: The additional_properties of this CampaignResource.
        :type: dict(str, ModelProperty)
        """

        self._additional_properties = additional_properties

    @property
    def created_date(self):
        """
        Gets the created_date of this CampaignResource.
        The date/time this resource was created in seconds since unix epoch

        :return: The created_date of this CampaignResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this CampaignResource.
        The date/time this resource was created in seconds since unix epoch

        :param created_date: The created_date of this CampaignResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def id(self):
        """
        Gets the id of this CampaignResource.
        The unique ID for that resource

        :return: The id of this CampaignResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CampaignResource.
        The unique ID for that resource

        :param id: The id of this CampaignResource.
        :type: int
        """

        self._id = id

    @property
    def leaderboard_strategy(self):
        """
        Gets the leaderboard_strategy of this CampaignResource.
        The strategy for calculating the leaderboard. Defaults to highest score. Value MUST come from the list of available strategies from the Leaderboard Service

        :return: The leaderboard_strategy of this CampaignResource.
        :rtype: str
        """
        return self._leaderboard_strategy

    @leaderboard_strategy.setter
    def leaderboard_strategy(self, leaderboard_strategy):
        """
        Sets the leaderboard_strategy of this CampaignResource.
        The strategy for calculating the leaderboard. Defaults to highest score. Value MUST come from the list of available strategies from the Leaderboard Service

        :param leaderboard_strategy: The leaderboard_strategy of this CampaignResource.
        :type: str
        """

        self._leaderboard_strategy = leaderboard_strategy

    @property
    def long_description(self):
        """
        Gets the long_description of this CampaignResource.
        The user friendly name of that resource. Defaults to blank string

        :return: The long_description of this CampaignResource.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this CampaignResource.
        The user friendly name of that resource. Defaults to blank string

        :param long_description: The long_description of this CampaignResource.
        :type: str
        """

        self._long_description = long_description

    @property
    def name(self):
        """
        Gets the name of this CampaignResource.
        The user friendly name of that resource

        :return: The name of this CampaignResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CampaignResource.
        The user friendly name of that resource

        :param name: The name of this CampaignResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def next_challenge(self):
        """
        Gets the next_challenge of this CampaignResource.
        The name of the next challenge coming up

        :return: The next_challenge of this CampaignResource.
        :rtype: str
        """
        return self._next_challenge

    @next_challenge.setter
    def next_challenge(self, next_challenge):
        """
        Sets the next_challenge of this CampaignResource.
        The name of the next challenge coming up

        :param next_challenge: The next_challenge of this CampaignResource.
        :type: str
        """

        self._next_challenge = next_challenge

    @property
    def next_challenge_date(self):
        """
        Gets the next_challenge_date of this CampaignResource.
        The date/time of the next challenge coming up

        :return: The next_challenge_date of this CampaignResource.
        :rtype: int
        """
        return self._next_challenge_date

    @next_challenge_date.setter
    def next_challenge_date(self, next_challenge_date):
        """
        Sets the next_challenge_date of this CampaignResource.
        The date/time of the next challenge coming up

        :param next_challenge_date: The next_challenge_date of this CampaignResource.
        :type: int
        """

        self._next_challenge_date = next_challenge_date

    @property
    def reward_set(self):
        """
        Gets the reward_set of this CampaignResource.
        The rewards to give at the end of the campaign. When creating/updating only id is used. Reward set must be pre-existing

        :return: The reward_set of this CampaignResource.
        :rtype: RewardSetResource
        """
        return self._reward_set

    @reward_set.setter
    def reward_set(self, reward_set):
        """
        Sets the reward_set of this CampaignResource.
        The rewards to give at the end of the campaign. When creating/updating only id is used. Reward set must be pre-existing

        :param reward_set: The reward_set of this CampaignResource.
        :type: RewardSetResource
        """

        self._reward_set = reward_set

    @property
    def reward_status(self):
        """
        Gets the reward_status of this CampaignResource.
        Indicate if the rewards have been given out already

        :return: The reward_status of this CampaignResource.
        :rtype: str
        """
        return self._reward_status

    @reward_status.setter
    def reward_status(self, reward_status):
        """
        Sets the reward_status of this CampaignResource.
        Indicate if the rewards have been given out already

        :param reward_status: The reward_status of this CampaignResource.
        :type: str
        """
        allowed_values = ["pending", "failed", "complete", "partial"]
        if reward_status not in allowed_values:
            raise ValueError(
                "Invalid value for `reward_status` ({0}), must be one of {1}"
                .format(reward_status, allowed_values)
            )

        self._reward_status = reward_status

    @property
    def short_description(self):
        """
        Gets the short_description of this CampaignResource.
        The user friendly name of that resource. Defaults to blank string

        :return: The short_description of this CampaignResource.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this CampaignResource.
        The user friendly name of that resource. Defaults to blank string

        :param short_description: The short_description of this CampaignResource.
        :type: str
        """

        self._short_description = short_description

    @property
    def template(self):
        """
        Gets the template of this CampaignResource.
        A campaign template this campaign is validated against (private). May be null and no validation of additional_properties will be done

        :return: The template of this CampaignResource.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this CampaignResource.
        A campaign template this campaign is validated against (private). May be null and no validation of additional_properties will be done

        :param template: The template of this CampaignResource.
        :type: str
        """

        self._template = template

    @property
    def updated_date(self):
        """
        Gets the updated_date of this CampaignResource.
        The date/time this resource was last updated in seconds since unix epoch

        :return: The updated_date of this CampaignResource.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this CampaignResource.
        The date/time this resource was last updated in seconds since unix epoch

        :param updated_date: The updated_date of this CampaignResource.
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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
