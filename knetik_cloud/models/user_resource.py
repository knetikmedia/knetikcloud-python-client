# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, additional_properties=None, address=None, address2=None, avatar_url=None, children=None, city=None, country_code=None, currency_code=None, date_of_birth=None, description=None, display_name=None, email=None, first_name=None, fullname=None, gender=None, id=None, language_code=None, last_name=None, mobile_number=None, parents=None, password=None, postal_code=None, state=None, tags=None, template=None, timezone_code=None, username=None):
        """
        UserResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'additional_properties': 'dict(str, ModelProperty)',
            'address': 'str',
            'address2': 'str',
            'avatar_url': 'str',
            'children': 'list[UserRelationshipReferenceResource]',
            'city': 'str',
            'country_code': 'str',
            'currency_code': 'str',
            'date_of_birth': 'int',
            'description': 'str',
            'display_name': 'str',
            'email': 'str',
            'first_name': 'str',
            'fullname': 'str',
            'gender': 'str',
            'id': 'int',
            'language_code': 'str',
            'last_name': 'str',
            'mobile_number': 'str',
            'parents': 'list[UserRelationshipReferenceResource]',
            'password': 'str',
            'postal_code': 'str',
            'state': 'str',
            'tags': 'list[str]',
            'template': 'str',
            'timezone_code': 'str',
            'username': 'str'
        }

        self.attribute_map = {
            'additional_properties': 'additional_properties',
            'address': 'address',
            'address2': 'address2',
            'avatar_url': 'avatar_url',
            'children': 'children',
            'city': 'city',
            'country_code': 'country_code',
            'currency_code': 'currency_code',
            'date_of_birth': 'date_of_birth',
            'description': 'description',
            'display_name': 'display_name',
            'email': 'email',
            'first_name': 'first_name',
            'fullname': 'fullname',
            'gender': 'gender',
            'id': 'id',
            'language_code': 'language_code',
            'last_name': 'last_name',
            'mobile_number': 'mobile_number',
            'parents': 'parents',
            'password': 'password',
            'postal_code': 'postal_code',
            'state': 'state',
            'tags': 'tags',
            'template': 'template',
            'timezone_code': 'timezone_code',
            'username': 'username'
        }

        self._additional_properties = additional_properties
        self._address = address
        self._address2 = address2
        self._avatar_url = avatar_url
        self._children = children
        self._city = city
        self._country_code = country_code
        self._currency_code = currency_code
        self._date_of_birth = date_of_birth
        self._description = description
        self._display_name = display_name
        self._email = email
        self._first_name = first_name
        self._fullname = fullname
        self._gender = gender
        self._id = id
        self._language_code = language_code
        self._last_name = last_name
        self._mobile_number = mobile_number
        self._parents = parents
        self._password = password
        self._postal_code = postal_code
        self._state = state
        self._tags = tags
        self._template = template
        self._timezone_code = timezone_code
        self._username = username

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this UserResource.
        A map of additional properties, keyed on the property name (private). Must match the names and types defined in the template for this user type, or be an extra not from the template

        :return: The additional_properties of this UserResource.
        :rtype: dict(str, ModelProperty)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this UserResource.
        A map of additional properties, keyed on the property name (private). Must match the names and types defined in the template for this user type, or be an extra not from the template

        :param additional_properties: The additional_properties of this UserResource.
        :type: dict(str, ModelProperty)
        """

        self._additional_properties = additional_properties

    @property
    def address(self):
        """
        Gets the address of this UserResource.
        The first line of the user's address (private)

        :return: The address of this UserResource.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this UserResource.
        The first line of the user's address (private)

        :param address: The address of this UserResource.
        :type: str
        """

        self._address = address

    @property
    def address2(self):
        """
        Gets the address2 of this UserResource.
        The second line of user's address (private)

        :return: The address2 of this UserResource.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this UserResource.
        The second line of user's address (private)

        :param address2: The address2 of this UserResource.
        :type: str
        """

        self._address2 = address2

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this UserResource.
        The url of the user's avatar image

        :return: The avatar_url of this UserResource.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this UserResource.
        The url of the user's avatar image

        :param avatar_url: The avatar_url of this UserResource.
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def children(self):
        """
        Gets the children of this UserResource.
        Relationships where this user is the parent. Read-Only, manage through separate endpoints

        :return: The children of this UserResource.
        :rtype: list[UserRelationshipReferenceResource]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this UserResource.
        Relationships where this user is the parent. Read-Only, manage through separate endpoints

        :param children: The children of this UserResource.
        :type: list[UserRelationshipReferenceResource]
        """

        self._children = children

    @property
    def city(self):
        """
        Gets the city of this UserResource.
        The user's city (private)

        :return: The city of this UserResource.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this UserResource.
        The user's city (private)

        :param city: The city of this UserResource.
        :type: str
        """

        self._city = city

    @property
    def country_code(self):
        """
        Gets the country_code of this UserResource.
        The ISO3 code for the country from the user's address (private). Will be filled in based on GeoIP country at registration if not provided.

        :return: The country_code of this UserResource.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this UserResource.
        The ISO3 code for the country from the user's address (private). Will be filled in based on GeoIP country at registration if not provided.

        :param country_code: The country_code of this UserResource.
        :type: str
        """

        self._country_code = country_code

    @property
    def currency_code(self):
        """
        Gets the currency_code of this UserResource.
        The code for the user's real money currency (private)

        :return: The currency_code of this UserResource.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this UserResource.
        The code for the user's real money currency (private)

        :param currency_code: The currency_code of this UserResource.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def date_of_birth(self):
        """
        Gets the date_of_birth of this UserResource.
        The user's date of birth (private) as a unix timestamp

        :return: The date_of_birth of this UserResource.
        :rtype: int
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """
        Sets the date_of_birth of this UserResource.
        The user's date of birth (private) as a unix timestamp

        :param date_of_birth: The date_of_birth of this UserResource.
        :type: int
        """

        self._date_of_birth = date_of_birth

    @property
    def description(self):
        """
        Gets the description of this UserResource.
        The user's self description (private)

        :return: The description of this UserResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UserResource.
        The user's self description (private)

        :param description: The description of this UserResource.
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this UserResource.
        The chosen display name of the user, defaults to username if not present

        :return: The display_name of this UserResource.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UserResource.
        The chosen display name of the user, defaults to username if not present

        :param display_name: The display_name of this UserResource.
        :type: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """
        Gets the email of this UserResource.
        The user's email address (private). May be required and/or unique depending on system configuration (both on by default). Must match standard email requirements if provided (RFC 2822)

        :return: The email of this UserResource.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserResource.
        The user's email address (private). May be required and/or unique depending on system configuration (both on by default). Must match standard email requirements if provided (RFC 2822)

        :param email: The email of this UserResource.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this UserResource.
        The user's first name (private)

        :return: The first_name of this UserResource.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this UserResource.
        The user's first name (private)

        :param first_name: The first_name of this UserResource.
        :type: str
        """

        self._first_name = first_name

    @property
    def fullname(self):
        """
        Gets the fullname of this UserResource.
        The user's full name (private)

        :return: The fullname of this UserResource.
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """
        Sets the fullname of this UserResource.
        The user's full name (private)

        :param fullname: The fullname of this UserResource.
        :type: str
        """

        self._fullname = fullname

    @property
    def gender(self):
        """
        Gets the gender of this UserResource.
        The user's gender (private)

        :return: The gender of this UserResource.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """
        Sets the gender of this UserResource.
        The user's gender (private)

        :param gender: The gender of this UserResource.
        :type: str
        """

        self._gender = gender

    @property
    def id(self):
        """
        Gets the id of this UserResource.
        The id of the user

        :return: The id of this UserResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserResource.
        The id of the user

        :param id: The id of this UserResource.
        :type: int
        """

        self._id = id

    @property
    def language_code(self):
        """
        Gets the language_code of this UserResource.
        The ISO3 code for the user's currency (private)

        :return: The language_code of this UserResource.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this UserResource.
        The ISO3 code for the user's currency (private)

        :param language_code: The language_code of this UserResource.
        :type: str
        """

        self._language_code = language_code

    @property
    def last_name(self):
        """
        Gets the last_name of this UserResource.
        The user's last name (private)

        :return: The last_name of this UserResource.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this UserResource.
        The user's last name (private)

        :param last_name: The last_name of this UserResource.
        :type: str
        """

        self._last_name = last_name

    @property
    def mobile_number(self):
        """
        Gets the mobile_number of this UserResource.
        The user's mobile phone number (private)

        :return: The mobile_number of this UserResource.
        :rtype: str
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        """
        Sets the mobile_number of this UserResource.
        The user's mobile phone number (private)

        :param mobile_number: The mobile_number of this UserResource.
        :type: str
        """

        self._mobile_number = mobile_number

    @property
    def parents(self):
        """
        Gets the parents of this UserResource.
        Relationships where this user is the child. Read-Only, manage through separate endpoints

        :return: The parents of this UserResource.
        :rtype: list[UserRelationshipReferenceResource]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """
        Sets the parents of this UserResource.
        Relationships where this user is the child. Read-Only, manage through separate endpoints

        :param parents: The parents of this UserResource.
        :type: list[UserRelationshipReferenceResource]
        """

        self._parents = parents

    @property
    def password(self):
        """
        Gets the password of this UserResource.
        The plain text password for the new user account. Required for registration; ignored on profile update.  Use password specific endpoints for editing

        :return: The password of this UserResource.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UserResource.
        The plain text password for the new user account. Required for registration; ignored on profile update.  Use password specific endpoints for editing

        :param password: The password of this UserResource.
        :type: str
        """

        self._password = password

    @property
    def postal_code(self):
        """
        Gets the postal_code of this UserResource.
        The user's postal code (private)

        :return: The postal_code of this UserResource.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this UserResource.
        The user's postal code (private)

        :param postal_code: The postal_code of this UserResource.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def state(self):
        """
        Gets the state of this UserResource.
        The user's state (private)

        :return: The state of this UserResource.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this UserResource.
        The user's state (private)

        :param state: The state of this UserResource.
        :type: str
        """

        self._state = state

    @property
    def tags(self):
        """
        Gets the tags of this UserResource.
        Tags on the user. Can only be set by admin. Max length per tag is 64 characters

        :return: The tags of this UserResource.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this UserResource.
        Tags on the user. Can only be set by admin. Max length per tag is 64 characters

        :param tags: The tags of this UserResource.
        :type: list[str]
        """

        self._tags = tags

    @property
    def template(self):
        """
        Gets the template of this UserResource.
        A user template this user is validated against (private). May be null and no validation of properties will be done

        :return: The template of this UserResource.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this UserResource.
        A user template this user is validated against (private). May be null and no validation of properties will be done

        :param template: The template of this UserResource.
        :type: str
        """

        self._template = template

    @property
    def timezone_code(self):
        """
        Gets the timezone_code of this UserResource.
        The code for the user's timezone (private)

        :return: The timezone_code of this UserResource.
        :rtype: str
        """
        return self._timezone_code

    @timezone_code.setter
    def timezone_code(self, timezone_code):
        """
        Sets the timezone_code of this UserResource.
        The code for the user's timezone (private)

        :param timezone_code: The timezone_code of this UserResource.
        :type: str
        """

        self._timezone_code = timezone_code

    @property
    def username(self):
        """
        Gets the username of this UserResource.
        The login username for the user (private). May be set to match email if system does not require usernames separately.

        :return: The username of this UserResource.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserResource.
        The login username for the user (private). May be set to match email if system does not require usernames separately.

        :param username: The username of this UserResource.
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username

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
        if not isinstance(other, UserResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
