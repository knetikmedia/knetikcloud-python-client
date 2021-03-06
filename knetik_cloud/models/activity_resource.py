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


class ActivityResource(object):
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
        'additional_properties': 'dict(str, ModelProperty)',
        'core_settings': 'CoreActivitySettings',
        'created_date': 'int',
        'entitlements': 'list[ActivityEntitlementResource]',
        'id': 'int',
        'launch': 'str',
        'leaderboard_strategy': 'str',
        'long_description': 'str',
        'name': 'str',
        'reward_set': 'RewardSetResource',
        'settings': 'list[AvailableSettingResource]',
        'short_description': 'str',
        'template': 'bool',
        'template_id': 'str',
        'type': 'str',
        'unique_key': 'str',
        'updated_date': 'int'
    }

    attribute_map = {
        'additional_properties': 'additional_properties',
        'core_settings': 'core_settings',
        'created_date': 'created_date',
        'entitlements': 'entitlements',
        'id': 'id',
        'launch': 'launch',
        'leaderboard_strategy': 'leaderboard_strategy',
        'long_description': 'long_description',
        'name': 'name',
        'reward_set': 'reward_set',
        'settings': 'settings',
        'short_description': 'short_description',
        'template': 'template',
        'template_id': 'template_id',
        'type': 'type',
        'unique_key': 'unique_key',
        'updated_date': 'updated_date'
    }

    def __init__(self, additional_properties=None, core_settings=None, created_date=None, entitlements=None, id=None, launch=None, leaderboard_strategy=None, long_description=None, name=None, reward_set=None, settings=None, short_description=None, template=None, template_id=None, type=None, unique_key=None, updated_date=None):
        """
        ActivityResource - a model defined in Swagger
        """

        self._additional_properties = None
        self._core_settings = None
        self._created_date = None
        self._entitlements = None
        self._id = None
        self._launch = None
        self._leaderboard_strategy = None
        self._long_description = None
        self._name = None
        self._reward_set = None
        self._settings = None
        self._short_description = None
        self._template = None
        self._template_id = None
        self._type = None
        self._unique_key = None
        self._updated_date = None
        self.discriminator = None

        if additional_properties is not None:
          self.additional_properties = additional_properties
        if core_settings is not None:
          self.core_settings = core_settings
        if created_date is not None:
          self.created_date = created_date
        if entitlements is not None:
          self.entitlements = entitlements
        if id is not None:
          self.id = id
        if launch is not None:
          self.launch = launch
        if leaderboard_strategy is not None:
          self.leaderboard_strategy = leaderboard_strategy
        if long_description is not None:
          self.long_description = long_description
        self.name = name
        if reward_set is not None:
          self.reward_set = reward_set
        if settings is not None:
          self.settings = settings
        if short_description is not None:
          self.short_description = short_description
        if template is not None:
          self.template = template
        if template_id is not None:
          self.template_id = template_id
        if type is not None:
          self.type = type
        if unique_key is not None:
          self.unique_key = unique_key
        if updated_date is not None:
          self.updated_date = updated_date

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this ActivityResource.
        A map of additional properties keyed on the property name. Used to further describe an activity. While settings will vary from one activity occurrence (a game) to another, additional properties are shared by all the occurrences of this activity. Ex: Activity Logo, Disclaimer, Greeting, etc. Validated against template if one exists for activities

        :return: The additional_properties of this ActivityResource.
        :rtype: dict(str, ModelProperty)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this ActivityResource.
        A map of additional properties keyed on the property name. Used to further describe an activity. While settings will vary from one activity occurrence (a game) to another, additional properties are shared by all the occurrences of this activity. Ex: Activity Logo, Disclaimer, Greeting, etc. Validated against template if one exists for activities

        :param additional_properties: The additional_properties of this ActivityResource.
        :type: dict(str, ModelProperty)
        """

        self._additional_properties = additional_properties

    @property
    def core_settings(self):
        """
        Gets the core_settings of this ActivityResource.
        Defines core settings about the activity that affect how it can be created/played by users.

        :return: The core_settings of this ActivityResource.
        :rtype: CoreActivitySettings
        """
        return self._core_settings

    @core_settings.setter
    def core_settings(self, core_settings):
        """
        Sets the core_settings of this ActivityResource.
        Defines core settings about the activity that affect how it can be created/played by users.

        :param core_settings: The core_settings of this ActivityResource.
        :type: CoreActivitySettings
        """

        self._core_settings = core_settings

    @property
    def created_date(self):
        """
        Gets the created_date of this ActivityResource.
        The date/time this resource was created in seconds since unix epoch

        :return: The created_date of this ActivityResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this ActivityResource.
        The date/time this resource was created in seconds since unix epoch

        :param created_date: The created_date of this ActivityResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def entitlements(self):
        """
        Gets the entitlements of this ActivityResource.
        The list of items that can be used for entitlement (wager amounts/etc)

        :return: The entitlements of this ActivityResource.
        :rtype: list[ActivityEntitlementResource]
        """
        return self._entitlements

    @entitlements.setter
    def entitlements(self, entitlements):
        """
        Sets the entitlements of this ActivityResource.
        The list of items that can be used for entitlement (wager amounts/etc)

        :param entitlements: The entitlements of this ActivityResource.
        :type: list[ActivityEntitlementResource]
        """

        self._entitlements = entitlements

    @property
    def id(self):
        """
        Gets the id of this ActivityResource.
        The unique ID for that resource

        :return: The id of this ActivityResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ActivityResource.
        The unique ID for that resource

        :param id: The id of this ActivityResource.
        :type: int
        """

        self._id = id

    @property
    def launch(self):
        """
        Gets the launch of this ActivityResource.
        Details about how to launch the activity

        :return: The launch of this ActivityResource.
        :rtype: str
        """
        return self._launch

    @launch.setter
    def launch(self, launch):
        """
        Sets the launch of this ActivityResource.
        Details about how to launch the activity

        :param launch: The launch of this ActivityResource.
        :type: str
        """

        self._launch = launch

    @property
    def leaderboard_strategy(self):
        """
        Gets the leaderboard_strategy of this ActivityResource.
        The strategy for calculating the leaderboard. No strategy means no leaderboard for the top level context. Value MUST come from the list of available strategies from the Leaderboard Service

        :return: The leaderboard_strategy of this ActivityResource.
        :rtype: str
        """
        return self._leaderboard_strategy

    @leaderboard_strategy.setter
    def leaderboard_strategy(self, leaderboard_strategy):
        """
        Sets the leaderboard_strategy of this ActivityResource.
        The strategy for calculating the leaderboard. No strategy means no leaderboard for the top level context. Value MUST come from the list of available strategies from the Leaderboard Service

        :param leaderboard_strategy: The leaderboard_strategy of this ActivityResource.
        :type: str
        """

        self._leaderboard_strategy = leaderboard_strategy

    @property
    def long_description(self):
        """
        Gets the long_description of this ActivityResource.
        The user friendly name of that resource. Defaults to blank string

        :return: The long_description of this ActivityResource.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this ActivityResource.
        The user friendly name of that resource. Defaults to blank string

        :param long_description: The long_description of this ActivityResource.
        :type: str
        """

        self._long_description = long_description

    @property
    def name(self):
        """
        Gets the name of this ActivityResource.
        The user friendly name of that resource

        :return: The name of this ActivityResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ActivityResource.
        The user friendly name of that resource

        :param name: The name of this ActivityResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def reward_set(self):
        """
        Gets the reward_set of this ActivityResource.
        The rewards to give at the end of each occurence of the activity. When creating/updating only id is used. Reward set must be pre-existing

        :return: The reward_set of this ActivityResource.
        :rtype: RewardSetResource
        """
        return self._reward_set

    @reward_set.setter
    def reward_set(self, reward_set):
        """
        Sets the reward_set of this ActivityResource.
        The rewards to give at the end of each occurence of the activity. When creating/updating only id is used. Reward set must be pre-existing

        :param reward_set: The reward_set of this ActivityResource.
        :type: RewardSetResource
        """

        self._reward_set = reward_set

    @property
    def settings(self):
        """
        Gets the settings of this ActivityResource.
        Define what parameters are required/available to start and run an activity. For example: Difficulty, Number of Questions, Character name, Avatar, Duration, etc. Not populated when getting listing

        :return: The settings of this ActivityResource.
        :rtype: list[AvailableSettingResource]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """
        Sets the settings of this ActivityResource.
        Define what parameters are required/available to start and run an activity. For example: Difficulty, Number of Questions, Character name, Avatar, Duration, etc. Not populated when getting listing

        :param settings: The settings of this ActivityResource.
        :type: list[AvailableSettingResource]
        """

        self._settings = settings

    @property
    def short_description(self):
        """
        Gets the short_description of this ActivityResource.
        The user friendly name of that resource. Defaults to blank string

        :return: The short_description of this ActivityResource.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this ActivityResource.
        The user friendly name of that resource. Defaults to blank string

        :param short_description: The short_description of this ActivityResource.
        :type: str
        """

        self._short_description = short_description

    @property
    def template(self):
        """
        Gets the template of this ActivityResource.
        Whether this activity is a template for other activities. Default: false

        :return: The template of this ActivityResource.
        :rtype: bool
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this ActivityResource.
        Whether this activity is a template for other activities. Default: false

        :param template: The template of this ActivityResource.
        :type: bool
        """

        self._template = template

    @property
    def template_id(self):
        """
        Gets the template_id of this ActivityResource.
        An activity template this activity is validated against (private). May be null and no validation of additional_properties will be done

        :return: The template_id of this ActivityResource.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this ActivityResource.
        An activity template this activity is validated against (private). May be null and no validation of additional_properties will be done

        :param template_id: The template_id of this ActivityResource.
        :type: str
        """

        self._template_id = template_id

    @property
    def type(self):
        """
        Gets the type of this ActivityResource.
        The type of the activity

        :return: The type of this ActivityResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ActivityResource.
        The type of the activity

        :param type: The type of this ActivityResource.
        :type: str
        """

        self._type = type

    @property
    def unique_key(self):
        """
        Gets the unique_key of this ActivityResource.
        The unique key (for static reference in code) of the activity

        :return: The unique_key of this ActivityResource.
        :rtype: str
        """
        return self._unique_key

    @unique_key.setter
    def unique_key(self, unique_key):
        """
        Sets the unique_key of this ActivityResource.
        The unique key (for static reference in code) of the activity

        :param unique_key: The unique_key of this ActivityResource.
        :type: str
        """

        self._unique_key = unique_key

    @property
    def updated_date(self):
        """
        Gets the updated_date of this ActivityResource.
        The date/time this resource was last updated in seconds since unix epoch

        :return: The updated_date of this ActivityResource.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this ActivityResource.
        The date/time this resource was last updated in seconds since unix epoch

        :param updated_date: The updated_date of this ActivityResource.
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
        if not isinstance(other, ActivityResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
