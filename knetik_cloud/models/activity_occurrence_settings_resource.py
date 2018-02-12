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


class ActivityOccurrenceSettingsResource(object):
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
        'core_settings': 'CoreActivityOccurrenceSettings',
        'settings': 'list[SelectedSettingRequest]'
    }

    attribute_map = {
        'core_settings': 'core_settings',
        'settings': 'settings'
    }

    def __init__(self, core_settings=None, settings=None):
        """
        ActivityOccurrenceSettingsResource - a model defined in Swagger
        """

        self._core_settings = None
        self._settings = None
        self.discriminator = None

        if core_settings is not None:
          self.core_settings = core_settings
        if settings is not None:
          self.settings = settings

    @property
    def core_settings(self):
        """
        Gets the core_settings of this ActivityOccurrenceSettingsResource.
        Defines core settings about the activity occurrence that affect how it behaves in the system. Validated against core settings in activity/challenge-activity.

        :return: The core_settings of this ActivityOccurrenceSettingsResource.
        :rtype: CoreActivityOccurrenceSettings
        """
        return self._core_settings

    @core_settings.setter
    def core_settings(self, core_settings):
        """
        Sets the core_settings of this ActivityOccurrenceSettingsResource.
        Defines core settings about the activity occurrence that affect how it behaves in the system. Validated against core settings in activity/challenge-activity.

        :param core_settings: The core_settings of this ActivityOccurrenceSettingsResource.
        :type: CoreActivityOccurrenceSettings
        """

        self._core_settings = core_settings

    @property
    def settings(self):
        """
        Gets the settings of this ActivityOccurrenceSettingsResource.
        The values selected from the available settings defined for the activity. Ex: difficulty: hard. Can be left out if the activity is played during an event and the settings are already set at the event level. Ex: every monday, difficulty: hard, number of questions: 10, category: sport. Otherwise, the set must exactly match those of the activity.

        :return: The settings of this ActivityOccurrenceSettingsResource.
        :rtype: list[SelectedSettingRequest]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """
        Sets the settings of this ActivityOccurrenceSettingsResource.
        The values selected from the available settings defined for the activity. Ex: difficulty: hard. Can be left out if the activity is played during an event and the settings are already set at the event level. Ex: every monday, difficulty: hard, number of questions: 10, category: sport. Otherwise, the set must exactly match those of the activity.

        :param settings: The settings of this ActivityOccurrenceSettingsResource.
        :type: list[SelectedSettingRequest]
        """

        self._settings = settings

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
        if not isinstance(other, ActivityOccurrenceSettingsResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
