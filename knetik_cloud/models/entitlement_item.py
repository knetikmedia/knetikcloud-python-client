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


class EntitlementItem(object):
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
        'behaviors': 'list[Behavior]',
        'category': 'str',
        'created_date': 'int',
        'id': 'int',
        'long_description': 'str',
        'name': 'str',
        'short_description': 'str',
        'sort': 'int',
        'tags': 'list[str]',
        'template': 'str',
        'type_hint': 'str',
        'unique_key': 'str',
        'updated_date': 'int'
    }

    attribute_map = {
        'additional_properties': 'additional_properties',
        'behaviors': 'behaviors',
        'category': 'category',
        'created_date': 'created_date',
        'id': 'id',
        'long_description': 'long_description',
        'name': 'name',
        'short_description': 'short_description',
        'sort': 'sort',
        'tags': 'tags',
        'template': 'template',
        'type_hint': 'type_hint',
        'unique_key': 'unique_key',
        'updated_date': 'updated_date'
    }

    def __init__(self, additional_properties=None, behaviors=None, category=None, created_date=None, id=None, long_description=None, name=None, short_description=None, sort=None, tags=None, template=None, type_hint=None, unique_key=None, updated_date=None):
        """
        EntitlementItem - a model defined in Swagger
        """

        self._additional_properties = None
        self._behaviors = None
        self._category = None
        self._created_date = None
        self._id = None
        self._long_description = None
        self._name = None
        self._short_description = None
        self._sort = None
        self._tags = None
        self._template = None
        self._type_hint = None
        self._unique_key = None
        self._updated_date = None

        if additional_properties is not None:
          self.additional_properties = additional_properties
        if behaviors is not None:
          self.behaviors = behaviors
        if category is not None:
          self.category = category
        if created_date is not None:
          self.created_date = created_date
        if id is not None:
          self.id = id
        if long_description is not None:
          self.long_description = long_description
        self.name = name
        if short_description is not None:
          self.short_description = short_description
        if sort is not None:
          self.sort = sort
        if tags is not None:
          self.tags = tags
        if template is not None:
          self.template = template
        self.type_hint = type_hint
        if unique_key is not None:
          self.unique_key = unique_key
        if updated_date is not None:
          self.updated_date = updated_date

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this EntitlementItem.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type, or be an extra not from the template

        :return: The additional_properties of this EntitlementItem.
        :rtype: dict(str, ModelProperty)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this EntitlementItem.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type, or be an extra not from the template

        :param additional_properties: The additional_properties of this EntitlementItem.
        :type: dict(str, ModelProperty)
        """

        self._additional_properties = additional_properties

    @property
    def behaviors(self):
        """
        Gets the behaviors of this EntitlementItem.
        The behaviors linked to the item, describing various options and interactions. May not be included in item lists

        :return: The behaviors of this EntitlementItem.
        :rtype: list[Behavior]
        """
        return self._behaviors

    @behaviors.setter
    def behaviors(self, behaviors):
        """
        Sets the behaviors of this EntitlementItem.
        The behaviors linked to the item, describing various options and interactions. May not be included in item lists

        :param behaviors: The behaviors of this EntitlementItem.
        :type: list[Behavior]
        """

        self._behaviors = behaviors

    @property
    def category(self):
        """
        Gets the category of this EntitlementItem.
        A category for filtering items

        :return: The category of this EntitlementItem.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this EntitlementItem.
        A category for filtering items

        :param category: The category of this EntitlementItem.
        :type: str
        """

        self._category = category

    @property
    def created_date(self):
        """
        Gets the created_date of this EntitlementItem.
        The date the item was created, unix timestamp in seconds

        :return: The created_date of this EntitlementItem.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this EntitlementItem.
        The date the item was created, unix timestamp in seconds

        :param created_date: The created_date of this EntitlementItem.
        :type: int
        """

        self._created_date = created_date

    @property
    def id(self):
        """
        Gets the id of this EntitlementItem.
        The id of the item

        :return: The id of this EntitlementItem.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EntitlementItem.
        The id of the item

        :param id: The id of this EntitlementItem.
        :type: int
        """

        self._id = id

    @property
    def long_description(self):
        """
        Gets the long_description of this EntitlementItem.
        A long description of the item

        :return: The long_description of this EntitlementItem.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this EntitlementItem.
        A long description of the item

        :param long_description: The long_description of this EntitlementItem.
        :type: str
        """

        self._long_description = long_description

    @property
    def name(self):
        """
        Gets the name of this EntitlementItem.
        The name of the item

        :return: The name of this EntitlementItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EntitlementItem.
        The name of the item

        :param name: The name of this EntitlementItem.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def short_description(self):
        """
        Gets the short_description of this EntitlementItem.
        A short description of the item, max 255 chars

        :return: The short_description of this EntitlementItem.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this EntitlementItem.
        A short description of the item, max 255 chars

        :param short_description: The short_description of this EntitlementItem.
        :type: str
        """

        self._short_description = short_description

    @property
    def sort(self):
        """
        Gets the sort of this EntitlementItem.
        A number to use in sorting items.  Default 500

        :return: The sort of this EntitlementItem.
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this EntitlementItem.
        A number to use in sorting items.  Default 500

        :param sort: The sort of this EntitlementItem.
        :type: int
        """

        self._sort = sort

    @property
    def tags(self):
        """
        Gets the tags of this EntitlementItem.
        List of tags used for filtering items

        :return: The tags of this EntitlementItem.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this EntitlementItem.
        List of tags used for filtering items

        :param tags: The tags of this EntitlementItem.
        :type: list[str]
        """

        self._tags = tags

    @property
    def template(self):
        """
        Gets the template of this EntitlementItem.
        An item template this item is validated against.  May be null and no validation of additional_properties will be done.  Default = null

        :return: The template of this EntitlementItem.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this EntitlementItem.
        An item template this item is validated against.  May be null and no validation of additional_properties will be done.  Default = null

        :param template: The template of this EntitlementItem.
        :type: str
        """

        self._template = template

    @property
    def type_hint(self):
        """
        Gets the type_hint of this EntitlementItem.
        The type of the item

        :return: The type_hint of this EntitlementItem.
        :rtype: str
        """
        return self._type_hint

    @type_hint.setter
    def type_hint(self, type_hint):
        """
        Sets the type_hint of this EntitlementItem.
        The type of the item

        :param type_hint: The type_hint of this EntitlementItem.
        :type: str
        """
        if type_hint is None:
            raise ValueError("Invalid value for `type_hint`, must not be `None`")

        self._type_hint = type_hint

    @property
    def unique_key(self):
        """
        Gets the unique_key of this EntitlementItem.
        The unique key for the item

        :return: The unique_key of this EntitlementItem.
        :rtype: str
        """
        return self._unique_key

    @unique_key.setter
    def unique_key(self, unique_key):
        """
        Sets the unique_key of this EntitlementItem.
        The unique key for the item

        :param unique_key: The unique_key of this EntitlementItem.
        :type: str
        """

        self._unique_key = unique_key

    @property
    def updated_date(self):
        """
        Gets the updated_date of this EntitlementItem.
        The date the item was last updated, unix timestamp in seconds

        :return: The updated_date of this EntitlementItem.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this EntitlementItem.
        The date the item was last updated, unix timestamp in seconds

        :param updated_date: The updated_date of this EntitlementItem.
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
        if not isinstance(other, EntitlementItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
