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


class ArtistResource(object):
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
        'born': 'str',
        'contribution_count': 'int',
        'contributions': 'list[ContributionResource]',
        'created_date': 'int',
        'died': 'str',
        'id': 'int',
        'long_description': 'str',
        'name': 'str',
        'priority': 'int',
        'short_description': 'str',
        'template': 'str',
        'updated_date': 'int'
    }

    attribute_map = {
        'additional_properties': 'additional_properties',
        'born': 'born',
        'contribution_count': 'contribution_count',
        'contributions': 'contributions',
        'created_date': 'created_date',
        'died': 'died',
        'id': 'id',
        'long_description': 'long_description',
        'name': 'name',
        'priority': 'priority',
        'short_description': 'short_description',
        'template': 'template',
        'updated_date': 'updated_date'
    }

    def __init__(self, additional_properties=None, born=None, contribution_count=None, contributions=None, created_date=None, died=None, id=None, long_description=None, name=None, priority=None, short_description=None, template=None, updated_date=None):
        """
        ArtistResource - a model defined in Swagger
        """

        self._additional_properties = None
        self._born = None
        self._contribution_count = None
        self._contributions = None
        self._created_date = None
        self._died = None
        self._id = None
        self._long_description = None
        self._name = None
        self._priority = None
        self._short_description = None
        self._template = None
        self._updated_date = None
        self.discriminator = None

        if additional_properties is not None:
          self.additional_properties = additional_properties
        if born is not None:
          self.born = born
        if contribution_count is not None:
          self.contribution_count = contribution_count
        if contributions is not None:
          self.contributions = contributions
        if created_date is not None:
          self.created_date = created_date
        if died is not None:
          self.died = died
        if id is not None:
          self.id = id
        if long_description is not None:
          self.long_description = long_description
        self.name = name
        if priority is not None:
          self.priority = priority
        if short_description is not None:
          self.short_description = short_description
        if template is not None:
          self.template = template
        if updated_date is not None:
          self.updated_date = updated_date

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this ArtistResource.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type

        :return: The additional_properties of this ArtistResource.
        :rtype: dict(str, ModelProperty)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this ArtistResource.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type

        :param additional_properties: The additional_properties of this ArtistResource.
        :type: dict(str, ModelProperty)
        """

        self._additional_properties = additional_properties

    @property
    def born(self):
        """
        Gets the born of this ArtistResource.
        YYYY/MM/DD when this artist was born

        :return: The born of this ArtistResource.
        :rtype: str
        """
        return self._born

    @born.setter
    def born(self, born):
        """
        Sets the born of this ArtistResource.
        YYYY/MM/DD when this artist was born

        :param born: The born of this ArtistResource.
        :type: str
        """

        self._born = born

    @property
    def contribution_count(self):
        """
        Gets the contribution_count of this ArtistResource.
        The current number of contributions the artist has made

        :return: The contribution_count of this ArtistResource.
        :rtype: int
        """
        return self._contribution_count

    @contribution_count.setter
    def contribution_count(self, contribution_count):
        """
        Sets the contribution_count of this ArtistResource.
        The current number of contributions the artist has made

        :param contribution_count: The contribution_count of this ArtistResource.
        :type: int
        """

        self._contribution_count = contribution_count

    @property
    def contributions(self):
        """
        Gets the contributions of this ArtistResource.
        The list of media this artist has contributed to as well as role(s) during contribution.  Use media endpoint to add contributions

        :return: The contributions of this ArtistResource.
        :rtype: list[ContributionResource]
        """
        return self._contributions

    @contributions.setter
    def contributions(self, contributions):
        """
        Sets the contributions of this ArtistResource.
        The list of media this artist has contributed to as well as role(s) during contribution.  Use media endpoint to add contributions

        :param contributions: The contributions of this ArtistResource.
        :type: list[ContributionResource]
        """

        self._contributions = contributions

    @property
    def created_date(self):
        """
        Gets the created_date of this ArtistResource.
        The date/time this resource was created in seconds since unix epoch

        :return: The created_date of this ArtistResource.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this ArtistResource.
        The date/time this resource was created in seconds since unix epoch

        :param created_date: The created_date of this ArtistResource.
        :type: int
        """

        self._created_date = created_date

    @property
    def died(self):
        """
        Gets the died of this ArtistResource.
        YYYY/MM/DD when this artist died

        :return: The died of this ArtistResource.
        :rtype: str
        """
        return self._died

    @died.setter
    def died(self, died):
        """
        Sets the died of this ArtistResource.
        YYYY/MM/DD when this artist died

        :param died: The died of this ArtistResource.
        :type: str
        """

        self._died = died

    @property
    def id(self):
        """
        Gets the id of this ArtistResource.
        The unique ID for that resource

        :return: The id of this ArtistResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ArtistResource.
        The unique ID for that resource

        :param id: The id of this ArtistResource.
        :type: int
        """

        self._id = id

    @property
    def long_description(self):
        """
        Gets the long_description of this ArtistResource.
        The user friendly name of that resource. Defaults to blank string

        :return: The long_description of this ArtistResource.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this ArtistResource.
        The user friendly name of that resource. Defaults to blank string

        :param long_description: The long_description of this ArtistResource.
        :type: str
        """

        self._long_description = long_description

    @property
    def name(self):
        """
        Gets the name of this ArtistResource.
        The user friendly name of that resource

        :return: The name of this ArtistResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ArtistResource.
        The user friendly name of that resource

        :param name: The name of this ArtistResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def priority(self):
        """
        Gets the priority of this ArtistResource.
        The sort order priority ofr the artist.  Default 100

        :return: The priority of this ArtistResource.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this ArtistResource.
        The sort order priority ofr the artist.  Default 100

        :param priority: The priority of this ArtistResource.
        :type: int
        """

        self._priority = priority

    @property
    def short_description(self):
        """
        Gets the short_description of this ArtistResource.
        The user friendly name of that resource. Defaults to blank string

        :return: The short_description of this ArtistResource.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this ArtistResource.
        The user friendly name of that resource. Defaults to blank string

        :param short_description: The short_description of this ArtistResource.
        :type: str
        """

        self._short_description = short_description

    @property
    def template(self):
        """
        Gets the template of this ArtistResource.
        An artist template this artist is validated against (private). May be null and no validation of additional_properties will be done

        :return: The template of this ArtistResource.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this ArtistResource.
        An artist template this artist is validated against (private). May be null and no validation of additional_properties will be done

        :param template: The template of this ArtistResource.
        :type: str
        """

        self._template = template

    @property
    def updated_date(self):
        """
        Gets the updated_date of this ArtistResource.
        The date/time this resource was last updated in seconds since unix epoch

        :return: The updated_date of this ArtistResource.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this ArtistResource.
        The date/time this resource was last updated in seconds since unix epoch

        :param updated_date: The updated_date of this ArtistResource.
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
        if not isinstance(other, ArtistResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
