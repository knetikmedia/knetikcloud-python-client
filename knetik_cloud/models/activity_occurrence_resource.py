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


class ActivityOccurrenceResource(object):
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
        'activity_id': 'int',
        'challenge_activity_id': 'int',
        'created_date': 'int',
        'entitlement': 'ActivityEntitlementResource',
        'event_id': 'int',
        'id': 'int',
        'reward_status': 'str',
        'settings': 'list[SelectedSettingResource]',
        'simulated': 'bool',
        'start_date': 'int',
        'status': 'str',
        'updated_date': 'int',
        'users': 'list[ActivityUserResource]'
    }

    attribute_map = {
        'activity_id': 'activity_id',
        'challenge_activity_id': 'challenge_activity_id',
        'created_date': 'created_date',
        'entitlement': 'entitlement',
        'event_id': 'event_id',
        'id': 'id',
        'reward_status': 'reward_status',
        'settings': 'settings',
        'simulated': 'simulated',
        'start_date': 'start_date',
        'status': 'status',
        'updated_date': 'updated_date',
        'users': 'users'
    }

    def __init__(self, activity_id=None, challenge_activity_id=None, created_date=None, entitlement=None, event_id=None, id=None, reward_status=None, settings=None, simulated=None, start_date=None, status=None, updated_date=None, users=None):
        """
        ActivityOccurrenceResource - a model defined in Swagger
        """

        self._activity_id = None
        self._challenge_activity_id = None
        self._created_date = None
        self._entitlement = None
        self._event_id = None
        self._id = None
        self._reward_status = None
        self._settings = None
        self._simulated = None
        self._start_date = None
        self._status = None
        self._updated_date = None
        self._users = None
        self.discriminator = None

        self.activity_id = activity_id
        if challenge_activity_id is not None:
          self.challenge_activity_id = challenge_activity_id
        if created_date is not None:
          self.created_date = created_date
        if entitlement is not None:
          self.entitlement = entitlement
        if event_id is not None:
          self.event_id = event_id
        if id is not None:
          self.id = id
        if reward_status is not None:
          self.reward_status = reward_status
        if settings is not None:
          self.settings = settings
        if simulated is not None:
          self.simulated = simulated
        if start_date is not None:
          self.start_date = start_date
        if status is not None:
          self.status = status
        if updated_date is not None:
          self.updated_date = updated_date
        if users is not None:
          self.users = users

    @property
    def activity_id(self):
        """
        Gets the activity_id of this ActivityOccurrenceResource.
        The id of the activity

        :return: The activity_id of this ActivityOccurrenceResource.
        :rtype: int
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """
        Sets the activity_id of this ActivityOccurrenceResource.
        The id of the activity

        :param activity_id: The activity_id of this ActivityOccurrenceResource.
        :type: int
        """
        if activity_id is None:
            raise ValueError("Invalid value for `activity_id`, must not be `None`")

        self._activity_id = activity_id

    @property
    def challenge_activity_id(self):
        """
        Gets the challenge_activity_id of this ActivityOccurrenceResource.
        The id of the challenge activity (as part of the event, required if eventId set)

        :return: The challenge_activity_id of this ActivityOccurrenceResource.
        :rtype: int
        """
        return self._challenge_activity_id

    @challenge_activity_id.setter
    def challenge_activity_id(self, challenge_activity_id):
        """
        Sets the challenge_activity_id of this ActivityOccurrenceResource.
        The id of the challenge activity (as part of the event, required if eventId set)

        :param challenge_activity_id: The challenge_activity_id of this ActivityOccurrenceResource.
        :type: int
        """

        self._challenge_activity_id = challenge_activity_id

    @property
    def created_date(self):
        """
        Gets the created_date of this ActivityOccurrenceResource.
        The date this occurrence was created, unix timestamp in seconds

        :return: The created_date of this ActivityOccurrenceResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this ActivityOccurrenceResource.
        The date this occurrence was created, unix timestamp in seconds

        :param created_date: The created_date of this ActivityOccurrenceResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def entitlement(self):
        """
        Gets the entitlement of this ActivityOccurrenceResource.
        The entitlement item required to enter the occurrence. Required if not part of an event. Must come from the set of entitlement items listed in the activity

        :return: The entitlement of this ActivityOccurrenceResource.
        :rtype: ActivityEntitlementResource
        """
        return self._entitlement

    @entitlement.setter
    def entitlement(self, entitlement):
        """
        Sets the entitlement of this ActivityOccurrenceResource.
        The entitlement item required to enter the occurrence. Required if not part of an event. Must come from the set of entitlement items listed in the activity

        :param entitlement: The entitlement of this ActivityOccurrenceResource.
        :type: ActivityEntitlementResource
        """

        self._entitlement = entitlement

    @property
    def event_id(self):
        """
        Gets the event_id of this ActivityOccurrenceResource.
        The id of the event

        :return: The event_id of this ActivityOccurrenceResource.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this ActivityOccurrenceResource.
        The id of the event

        :param event_id: The event_id of this ActivityOccurrenceResource.
        :type: int
        """

        self._event_id = event_id

    @property
    def id(self):
        """
        Gets the id of this ActivityOccurrenceResource.
        The id of the activity occurrence

        :return: The id of this ActivityOccurrenceResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ActivityOccurrenceResource.
        The id of the activity occurrence

        :param id: The id of this ActivityOccurrenceResource.
        :type: int
        """

        self._id = id

    @property
    def reward_status(self):
        """
        Gets the reward_status of this ActivityOccurrenceResource.
        Indicate if the rewards have been given out already

        :return: The reward_status of this ActivityOccurrenceResource.
        :rtype: str
        """
        return self._reward_status

    @reward_status.setter
    def reward_status(self, reward_status):
        """
        Sets the reward_status of this ActivityOccurrenceResource.
        Indicate if the rewards have been given out already

        :param reward_status: The reward_status of this ActivityOccurrenceResource.
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
    def settings(self):
        """
        Gets the settings of this ActivityOccurrenceResource.
        The values selected from the available settings defined for the activity. Ex: difficulty: hard. Can be left out if the activity is played during an event and the settings are already set at the event level. Ex: every monday, difficulty: hard, number of questions: 10, category: sport. Otherwise, the set must exactly match those of the activity.

        :return: The settings of this ActivityOccurrenceResource.
        :rtype: list[SelectedSettingResource]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """
        Sets the settings of this ActivityOccurrenceResource.
        The values selected from the available settings defined for the activity. Ex: difficulty: hard. Can be left out if the activity is played during an event and the settings are already set at the event level. Ex: every monday, difficulty: hard, number of questions: 10, category: sport. Otherwise, the set must exactly match those of the activity.

        :param settings: The settings of this ActivityOccurrenceResource.
        :type: list[SelectedSettingResource]
        """

        self._settings = settings

    @property
    def simulated(self):
        """
        Gets the simulated of this ActivityOccurrenceResource.
        Whether this occurrence will be ran as a simulation. Simulations will not be rewarded. Useful for bot play or trials

        :return: The simulated of this ActivityOccurrenceResource.
        :rtype: bool
        """
        return self._simulated

    @simulated.setter
    def simulated(self, simulated):
        """
        Sets the simulated of this ActivityOccurrenceResource.
        Whether this occurrence will be ran as a simulation. Simulations will not be rewarded. Useful for bot play or trials

        :param simulated: The simulated of this ActivityOccurrenceResource.
        :type: bool
        """

        self._simulated = simulated

    @property
    def start_date(self):
        """
        Gets the start_date of this ActivityOccurrenceResource.
        The date this occurrence was started, unix timestamp in seconds. null if not yet started

        :return: The start_date of this ActivityOccurrenceResource.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this ActivityOccurrenceResource.
        The date this occurrence was started, unix timestamp in seconds. null if not yet started

        :param start_date: The start_date of this ActivityOccurrenceResource.
        :type: int
        """

        self._start_date = start_date

    @property
    def status(self):
        """
        Gets the status of this ActivityOccurrenceResource.
        The current status of the occurrence (default: OPEN)

        :return: The status of this ActivityOccurrenceResource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ActivityOccurrenceResource.
        The current status of the occurrence (default: OPEN)

        :param status: The status of this ActivityOccurrenceResource.
        :type: str
        """
        allowed_values = ["SETUP", "OPEN", "PLAYING", "FINISHED", "ABANDONED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def updated_date(self):
        """
        Gets the updated_date of this ActivityOccurrenceResource.
        The date this occurrence was last updated, unix timestamp in seconds

        :return: The updated_date of this ActivityOccurrenceResource.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this ActivityOccurrenceResource.
        The date this occurrence was last updated, unix timestamp in seconds

        :param updated_date: The updated_date of this ActivityOccurrenceResource.
        :type: int
        """

        self._updated_date = updated_date

    @property
    def users(self):
        """
        Gets the users of this ActivityOccurrenceResource.
        The list of users participating in this occurrence. Can only be set directly with ACTIVITIES_ADMIN permission

        :return: The users of this ActivityOccurrenceResource.
        :rtype: list[ActivityUserResource]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this ActivityOccurrenceResource.
        The list of users participating in this occurrence. Can only be set directly with ACTIVITIES_ADMIN permission

        :param users: The users of this ActivityOccurrenceResource.
        :type: list[ActivityUserResource]
        """

        self._users = users

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
        if not isinstance(other, ActivityOccurrenceResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
