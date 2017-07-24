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


class BreRule(object):
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
        'actions': 'ActionResource',
        'condition': 'PredicateOperation',
        'condition_text': 'str',
        'description': 'str',
        'enabled': 'bool',
        'end_date': 'int',
        'event_name': 'str',
        'id': 'str',
        'name': 'str',
        'sort': 'int',
        'start_date': 'int',
        'system_rule': 'bool'
    }

    attribute_map = {
        'actions': 'actions',
        'condition': 'condition',
        'condition_text': 'condition_text',
        'description': 'description',
        'enabled': 'enabled',
        'end_date': 'end_date',
        'event_name': 'event_name',
        'id': 'id',
        'name': 'name',
        'sort': 'sort',
        'start_date': 'start_date',
        'system_rule': 'system_rule'
    }

    def __init__(self, actions=None, condition=None, condition_text=None, description=None, enabled=None, end_date=None, event_name=None, id=None, name=None, sort=None, start_date=None, system_rule=None):
        """
        BreRule - a model defined in Swagger
        """

        self._actions = None
        self._condition = None
        self._condition_text = None
        self._description = None
        self._enabled = None
        self._end_date = None
        self._event_name = None
        self._id = None
        self._name = None
        self._sort = None
        self._start_date = None
        self._system_rule = None

        self.actions = actions
        if condition is not None:
          self.condition = condition
        if condition_text is not None:
          self.condition_text = condition_text
        if description is not None:
          self.description = description
        if enabled is not None:
          self.enabled = enabled
        if end_date is not None:
          self.end_date = end_date
        self.event_name = event_name
        if id is not None:
          self.id = id
        self.name = name
        if sort is not None:
          self.sort = sort
        if start_date is not None:
          self.start_date = start_date
        if system_rule is not None:
          self.system_rule = system_rule

    @property
    def actions(self):
        """
        Gets the actions of this BreRule.
        A list of actions to execute, and the mapping for their parameters, when the rule runs. Minimum 1

        :return: The actions of this BreRule.
        :rtype: ActionResource
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this BreRule.
        A list of actions to execute, and the mapping for their parameters, when the rule runs. Minimum 1

        :param actions: The actions of this BreRule.
        :type: ActionResource
        """
        if actions is None:
            raise ValueError("Invalid value for `actions`, must not be `None`")

        self._actions = actions

    @property
    def condition(self):
        """
        Gets the condition of this BreRule.
        A condition expression that must be met in a given event for the rule to run. Empty to always run

        :return: The condition of this BreRule.
        :rtype: PredicateOperation
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this BreRule.
        A condition expression that must be met in a given event for the rule to run. Empty to always run

        :param condition: The condition of this BreRule.
        :type: PredicateOperation
        """

        self._condition = condition

    @property
    def condition_text(self):
        """
        Gets the condition_text of this BreRule.
        The condition as a readable string. Filled in by the system from the condition

        :return: The condition_text of this BreRule.
        :rtype: str
        """
        return self._condition_text

    @condition_text.setter
    def condition_text(self, condition_text):
        """
        Sets the condition_text of this BreRule.
        The condition as a readable string. Filled in by the system from the condition

        :param condition_text: The condition_text of this BreRule.
        :type: str
        """

        self._condition_text = condition_text

    @property
    def description(self):
        """
        Gets the description of this BreRule.
        The human readable description of the rule

        :return: The description of this BreRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BreRule.
        The human readable description of the rule

        :param description: The description of this BreRule.
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """
        Gets the enabled of this BreRule.
        Whether the rule is enabled to run (in conjunction with dates). Default true

        :return: The enabled of this BreRule.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this BreRule.
        Whether the rule is enabled to run (in conjunction with dates). Default true

        :param enabled: The enabled of this BreRule.
        :type: bool
        """

        self._enabled = enabled

    @property
    def end_date(self):
        """
        Gets the end_date of this BreRule.
        The date the rule ceases to take effect, or null if never. Unix timestamp in seconds

        :return: The end_date of this BreRule.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this BreRule.
        The date the rule ceases to take effect, or null if never. Unix timestamp in seconds

        :param end_date: The end_date of this BreRule.
        :type: int
        """

        self._end_date = end_date

    @property
    def event_name(self):
        """
        Gets the event_name of this BreRule.
        The event name of the trigger this rule runs for. Affects which parameters are available

        :return: The event_name of this BreRule.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this BreRule.
        The event name of the trigger this rule runs for. Affects which parameters are available

        :param event_name: The event_name of this BreRule.
        :type: str
        """
        if event_name is None:
            raise ValueError("Invalid value for `event_name`, must not be `None`")

        self._event_name = event_name

    @property
    def id(self):
        """
        Gets the id of this BreRule.
        The id of the rule for later references. If left null a random guid will be generated. Must be unique. Cannot be changed

        :return: The id of this BreRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BreRule.
        The id of the rule for later references. If left null a random guid will be generated. Must be unique. Cannot be changed

        :param id: The id of this BreRule.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this BreRule.
        The human readable name of the rule

        :return: The name of this BreRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BreRule.
        The human readable name of the rule

        :param name: The name of this BreRule.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def sort(self):
        """
        Gets the sort of this BreRule.
        Used to sort rules to control the order they run in. Larger numbered sort values run first.  Default 500

        :return: The sort of this BreRule.
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this BreRule.
        Used to sort rules to control the order they run in. Larger numbered sort values run first.  Default 500

        :param sort: The sort of this BreRule.
        :type: int
        """

        self._sort = sort

    @property
    def start_date(self):
        """
        Gets the start_date of this BreRule.
        The date the rule begins to take effect, or null if always. Unix timestamp in seconds

        :return: The start_date of this BreRule.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this BreRule.
        The date the rule begins to take effect, or null if always. Unix timestamp in seconds

        :param start_date: The start_date of this BreRule.
        :type: int
        """

        self._start_date = start_date

    @property
    def system_rule(self):
        """
        Gets the system_rule of this BreRule.
        Whether the rule is a default part of the system. System rules cannot be edited or deleted, but may be disabled

        :return: The system_rule of this BreRule.
        :rtype: bool
        """
        return self._system_rule

    @system_rule.setter
    def system_rule(self, system_rule):
        """
        Sets the system_rule of this BreRule.
        Whether the rule is a default part of the system. System rules cannot be edited or deleted, but may be disabled

        :param system_rule: The system_rule of this BreRule.
        :type: bool
        """

        self._system_rule = system_rule

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
        if not isinstance(other, BreRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other