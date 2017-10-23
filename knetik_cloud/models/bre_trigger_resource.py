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


class BreTriggerResource(object):
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
        'category': 'str',
        'event_name': 'str',
        'parameters': 'list[BreTriggerParameterDefinition]',
        'system_trigger': 'bool',
        'tags': 'list[str]',
        'trigger_description': 'str',
        'trigger_name': 'str'
    }

    attribute_map = {
        'category': 'category',
        'event_name': 'event_name',
        'parameters': 'parameters',
        'system_trigger': 'system_trigger',
        'tags': 'tags',
        'trigger_description': 'trigger_description',
        'trigger_name': 'trigger_name'
    }

    def __init__(self, category=None, event_name=None, parameters=None, system_trigger=None, tags=None, trigger_description=None, trigger_name=None):
        """
        BreTriggerResource - a model defined in Swagger
        """

        self._category = None
        self._event_name = None
        self._parameters = None
        self._system_trigger = None
        self._tags = None
        self._trigger_description = None
        self._trigger_name = None
        self.discriminator = None

        if category is not None:
          self.category = category
        self.event_name = event_name
        if parameters is not None:
          self.parameters = parameters
        if system_trigger is not None:
          self.system_trigger = system_trigger
        if tags is not None:
          self.tags = tags
        self.trigger_description = trigger_description
        self.trigger_name = trigger_name

    @property
    def category(self):
        """
        Gets the category of this BreTriggerResource.
        The category this trigger belongs to. See endpoints for related asset information. All new triggers are in category 'custom'

        :return: The category of this BreTriggerResource.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this BreTriggerResource.
        The category this trigger belongs to. See endpoints for related asset information. All new triggers are in category 'custom'

        :param category: The category of this BreTriggerResource.
        :type: str
        """
        allowed_values = ["achievement", "behavior", "comment", "disposition", "device", "entitlement", "friends", "fulfillment", "gamification", "inventory", "invoice", "media", "scheduler", "store", "subscription", "user", "wallet", "custom", "challenge", "activity", "campaign", "event"]
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def event_name(self):
        """
        Gets the event_name of this BreTriggerResource.
        The unique name for the event. This serves as the unique identifier. Cannot be changed after creation

        :return: The event_name of this BreTriggerResource.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this BreTriggerResource.
        The unique name for the event. This serves as the unique identifier. Cannot be changed after creation

        :param event_name: The event_name of this BreTriggerResource.
        :type: str
        """
        if event_name is None:
            raise ValueError("Invalid value for `event_name`, must not be `None`")

        self._event_name = event_name

    @property
    def parameters(self):
        """
        Gets the parameters of this BreTriggerResource.
        A list of parameters that will be sent with the event when the trigger is fired. These must be included in the event and match the described types

        :return: The parameters of this BreTriggerResource.
        :rtype: list[BreTriggerParameterDefinition]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this BreTriggerResource.
        A list of parameters that will be sent with the event when the trigger is fired. These must be included in the event and match the described types

        :param parameters: The parameters of this BreTriggerResource.
        :type: list[BreTriggerParameterDefinition]
        """

        self._parameters = parameters

    @property
    def system_trigger(self):
        """
        Gets the system_trigger of this BreTriggerResource.
        Where this trigger came from. System triggers cannot be removed or updated

        :return: The system_trigger of this BreTriggerResource.
        :rtype: bool
        """
        return self._system_trigger

    @system_trigger.setter
    def system_trigger(self, system_trigger):
        """
        Sets the system_trigger of this BreTriggerResource.
        Where this trigger came from. System triggers cannot be removed or updated

        :param system_trigger: The system_trigger of this BreTriggerResource.
        :type: bool
        """

        self._system_trigger = system_trigger

    @property
    def tags(self):
        """
        Gets the tags of this BreTriggerResource.
        A list of tags for filtering

        :return: The tags of this BreTriggerResource.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this BreTriggerResource.
        A list of tags for filtering

        :param tags: The tags of this BreTriggerResource.
        :type: list[str]
        """

        self._tags = tags

    @property
    def trigger_description(self):
        """
        Gets the trigger_description of this BreTriggerResource.
        A description of the trigger

        :return: The trigger_description of this BreTriggerResource.
        :rtype: str
        """
        return self._trigger_description

    @trigger_description.setter
    def trigger_description(self, trigger_description):
        """
        Sets the trigger_description of this BreTriggerResource.
        A description of the trigger

        :param trigger_description: The trigger_description of this BreTriggerResource.
        :type: str
        """
        if trigger_description is None:
            raise ValueError("Invalid value for `trigger_description`, must not be `None`")

        self._trigger_description = trigger_description

    @property
    def trigger_name(self):
        """
        Gets the trigger_name of this BreTriggerResource.
        A human readable name for this trigger

        :return: The trigger_name of this BreTriggerResource.
        :rtype: str
        """
        return self._trigger_name

    @trigger_name.setter
    def trigger_name(self, trigger_name):
        """
        Sets the trigger_name of this BreTriggerResource.
        A human readable name for this trigger

        :param trigger_name: The trigger_name of this BreTriggerResource.
        :type: str
        """
        if trigger_name is None:
            raise ValueError("Invalid value for `trigger_name`, must not be `None`")

        self._trigger_name = trigger_name

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
        if not isinstance(other, BreTriggerResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
