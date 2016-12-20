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


class ArticleResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active=None, additional_properties=None, body=None, category=None, created_date=None, id=None, tags=None, template=None, title=None, updated_date=None):
        """
        ArticleResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active': 'bool',
            'additional_properties': 'dict(str, ModelProperty)',
            'body': 'str',
            'category': 'NestedCategory',
            'created_date': 'int',
            'id': 'str',
            'tags': 'list[str]',
            'template': 'str',
            'title': 'str',
            'updated_date': 'int'
        }

        self.attribute_map = {
            'active': 'active',
            'additional_properties': 'additional_properties',
            'body': 'body',
            'category': 'category',
            'created_date': 'created_date',
            'id': 'id',
            'tags': 'tags',
            'template': 'template',
            'title': 'title',
            'updated_date': 'updated_date'
        }

        self._active = active
        self._additional_properties = additional_properties
        self._body = body
        self._category = category
        self._created_date = created_date
        self._id = id
        self._tags = tags
        self._template = template
        self._title = title
        self._updated_date = updated_date

    @property
    def active(self):
        """
        Gets the active of this ArticleResource.
        Whether the article is active

        :return: The active of this ArticleResource.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this ArticleResource.
        Whether the article is active

        :param active: The active of this ArticleResource.
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")

        self._active = active

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this ArticleResource.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type

        :return: The additional_properties of this ArticleResource.
        :rtype: dict(str, ModelProperty)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this ArticleResource.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type

        :param additional_properties: The additional_properties of this ArticleResource.
        :type: dict(str, ModelProperty)
        """

        self._additional_properties = additional_properties

    @property
    def body(self):
        """
        Gets the body of this ArticleResource.
        The body of the article

        :return: The body of this ArticleResource.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this ArticleResource.
        The body of the article

        :param body: The body of this ArticleResource.
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")

        self._body = body

    @property
    def category(self):
        """
        Gets the category of this ArticleResource.
        The category for the article

        :return: The category of this ArticleResource.
        :rtype: NestedCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this ArticleResource.
        The category for the article

        :param category: The category of this ArticleResource.
        :type: NestedCategory
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")

        self._category = category

    @property
    def created_date(self):
        """
        Gets the created_date of this ArticleResource.
        The date/time this resource was created in seconds since unix epoch

        :return: The created_date of this ArticleResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this ArticleResource.
        The date/time this resource was created in seconds since unix epoch

        :param created_date: The created_date of this ArticleResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def id(self):
        """
        Gets the id of this ArticleResource.
        The id of the article

        :return: The id of this ArticleResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ArticleResource.
        The id of the article

        :param id: The id of this ArticleResource.
        :type: str
        """

        self._id = id

    @property
    def tags(self):
        """
        Gets the tags of this ArticleResource.
        The tags for the article

        :return: The tags of this ArticleResource.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ArticleResource.
        The tags for the article

        :param tags: The tags of this ArticleResource.
        :type: list[str]
        """

        self._tags = tags

    @property
    def template(self):
        """
        Gets the template of this ArticleResource.
        An article template this article is validated against (private). May be null and no validation of additional_properties will be done

        :return: The template of this ArticleResource.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this ArticleResource.
        An article template this article is validated against (private). May be null and no validation of additional_properties will be done

        :param template: The template of this ArticleResource.
        :type: str
        """

        self._template = template

    @property
    def title(self):
        """
        Gets the title of this ArticleResource.
        The title of the article

        :return: The title of this ArticleResource.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ArticleResource.
        The title of the article

        :param title: The title of this ArticleResource.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def updated_date(self):
        """
        Gets the updated_date of this ArticleResource.
        The date/time this resource was last updated in seconds since unix epoch

        :return: The updated_date of this ArticleResource.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this ArticleResource.
        The date/time this resource was last updated in seconds since unix epoch

        :param updated_date: The updated_date of this ArticleResource.
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
