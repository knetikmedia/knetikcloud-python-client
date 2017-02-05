# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, additional_properties=None, address=None, address2=None, affiliate=None, avatar_url=None, children=None, city=None, country=None, currency=None, date_created=None, date_of_birth=None, date_updated=None, description=None, display_name=None, email=None, first_name=None, fullname=None, gender=None, groups=None, guest=None, id=None, invite_token=None, lang=None, last_activity=None, last_login=None, last_name=None, lockout_attempts=None, lockout_date=None, mobile_number=None, old_id=None, parents=None, password=None, postal_code=None, properties_string=None, roles=None, state=None, status=None, tag_strings=None, tags=None, template=None, timezone=None, token=None, type_hint=None, username=None):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'additional_properties': 'dict(str, ModelProperty)',
            'address': 'str',
            'address2': 'str',
            'affiliate': 'Affiliate',
            'avatar_url': 'str',
            'children': 'list[UserRelationship]',
            'city': 'str',
            'country': 'Country',
            'currency': 'Currency',
            'date_created': 'int',
            'date_of_birth': 'int',
            'date_updated': 'int',
            'description': 'str',
            'display_name': 'str',
            'email': 'str',
            'first_name': 'str',
            'fullname': 'str',
            'gender': 'str',
            'groups': 'list[GroupMember]',
            'guest': 'bool',
            'id': 'int',
            'invite_token': 'str',
            'lang': 'Language',
            'last_activity': 'int',
            'last_login': 'int',
            'last_name': 'str',
            'lockout_attempts': 'int',
            'lockout_date': 'int',
            'mobile_number': 'str',
            'old_id': 'int',
            'parents': 'list[UserRelationship]',
            'password': 'str',
            'postal_code': 'str',
            'properties_string': 'str',
            'roles': 'list[Role]',
            'state': 'str',
            'status': 'str',
            'tag_strings': 'list[str]',
            'tags': 'list[UserTag]',
            'template': 'str',
            'timezone': 'Timezone',
            'token': 'str',
            'type_hint': 'str',
            'username': 'str'
        }

        self.attribute_map = {
            'additional_properties': 'additional_properties',
            'address': 'address',
            'address2': 'address2',
            'affiliate': 'affiliate',
            'avatar_url': 'avatar_url',
            'children': 'children',
            'city': 'city',
            'country': 'country',
            'currency': 'currency',
            'date_created': 'date_created',
            'date_of_birth': 'date_of_birth',
            'date_updated': 'date_updated',
            'description': 'description',
            'display_name': 'display_name',
            'email': 'email',
            'first_name': 'first_name',
            'fullname': 'fullname',
            'gender': 'gender',
            'groups': 'groups',
            'guest': 'guest',
            'id': 'id',
            'invite_token': 'invite_token',
            'lang': 'lang',
            'last_activity': 'last_activity',
            'last_login': 'last_login',
            'last_name': 'last_name',
            'lockout_attempts': 'lockout_attempts',
            'lockout_date': 'lockout_date',
            'mobile_number': 'mobile_number',
            'old_id': 'old_id',
            'parents': 'parents',
            'password': 'password',
            'postal_code': 'postal_code',
            'properties_string': 'properties_string',
            'roles': 'roles',
            'state': 'state',
            'status': 'status',
            'tag_strings': 'tag_strings',
            'tags': 'tags',
            'template': 'template',
            'timezone': 'timezone',
            'token': 'token',
            'type_hint': 'type_hint',
            'username': 'username'
        }

        self._additional_properties = additional_properties
        self._address = address
        self._address2 = address2
        self._affiliate = affiliate
        self._avatar_url = avatar_url
        self._children = children
        self._city = city
        self._country = country
        self._currency = currency
        self._date_created = date_created
        self._date_of_birth = date_of_birth
        self._date_updated = date_updated
        self._description = description
        self._display_name = display_name
        self._email = email
        self._first_name = first_name
        self._fullname = fullname
        self._gender = gender
        self._groups = groups
        self._guest = guest
        self._id = id
        self._invite_token = invite_token
        self._lang = lang
        self._last_activity = last_activity
        self._last_login = last_login
        self._last_name = last_name
        self._lockout_attempts = lockout_attempts
        self._lockout_date = lockout_date
        self._mobile_number = mobile_number
        self._old_id = old_id
        self._parents = parents
        self._password = password
        self._postal_code = postal_code
        self._properties_string = properties_string
        self._roles = roles
        self._state = state
        self._status = status
        self._tag_strings = tag_strings
        self._tags = tags
        self._template = template
        self._timezone = timezone
        self._token = token
        self._type_hint = type_hint
        self._username = username

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this User.

        :return: The additional_properties of this User.
        :rtype: dict(str, ModelProperty)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this User.

        :param additional_properties: The additional_properties of this User.
        :type: dict(str, ModelProperty)
        """

        self._additional_properties = additional_properties

    @property
    def address(self):
        """
        Gets the address of this User.

        :return: The address of this User.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this User.

        :param address: The address of this User.
        :type: str
        """

        self._address = address

    @property
    def address2(self):
        """
        Gets the address2 of this User.

        :return: The address2 of this User.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this User.

        :param address2: The address2 of this User.
        :type: str
        """

        self._address2 = address2

    @property
    def affiliate(self):
        """
        Gets the affiliate of this User.

        :return: The affiliate of this User.
        :rtype: Affiliate
        """
        return self._affiliate

    @affiliate.setter
    def affiliate(self, affiliate):
        """
        Sets the affiliate of this User.

        :param affiliate: The affiliate of this User.
        :type: Affiliate
        """

        self._affiliate = affiliate

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this User.

        :return: The avatar_url of this User.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this User.

        :param avatar_url: The avatar_url of this User.
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def children(self):
        """
        Gets the children of this User.

        :return: The children of this User.
        :rtype: list[UserRelationship]
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this User.

        :param children: The children of this User.
        :type: list[UserRelationship]
        """

        self._children = children

    @property
    def city(self):
        """
        Gets the city of this User.

        :return: The city of this User.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this User.

        :param city: The city of this User.
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """
        Gets the country of this User.

        :return: The country of this User.
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this User.

        :param country: The country of this User.
        :type: Country
        """

        self._country = country

    @property
    def currency(self):
        """
        Gets the currency of this User.

        :return: The currency of this User.
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this User.

        :param currency: The currency of this User.
        :type: Currency
        """

        self._currency = currency

    @property
    def date_created(self):
        """
        Gets the date_created of this User.

        :return: The date_created of this User.
        :rtype: int
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this User.

        :param date_created: The date_created of this User.
        :type: int
        """

        self._date_created = date_created

    @property
    def date_of_birth(self):
        """
        Gets the date_of_birth of this User.

        :return: The date_of_birth of this User.
        :rtype: int
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """
        Sets the date_of_birth of this User.

        :param date_of_birth: The date_of_birth of this User.
        :type: int
        """

        self._date_of_birth = date_of_birth

    @property
    def date_updated(self):
        """
        Gets the date_updated of this User.

        :return: The date_updated of this User.
        :rtype: int
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """
        Sets the date_updated of this User.

        :param date_updated: The date_updated of this User.
        :type: int
        """

        self._date_updated = date_updated

    @property
    def description(self):
        """
        Gets the description of this User.

        :return: The description of this User.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this User.

        :param description: The description of this User.
        :type: str
        """

        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this User.

        :return: The display_name of this User.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this User.

        :param display_name: The display_name of this User.
        :type: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """
        Gets the email of this User.

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.

        :param email: The email of this User.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this User.

        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this User.

        :param first_name: The first_name of this User.
        :type: str
        """

        self._first_name = first_name

    @property
    def fullname(self):
        """
        Gets the fullname of this User.

        :return: The fullname of this User.
        :rtype: str
        """
        return self._fullname

    @fullname.setter
    def fullname(self, fullname):
        """
        Sets the fullname of this User.

        :param fullname: The fullname of this User.
        :type: str
        """

        self._fullname = fullname

    @property
    def gender(self):
        """
        Gets the gender of this User.

        :return: The gender of this User.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """
        Sets the gender of this User.

        :param gender: The gender of this User.
        :type: str
        """

        self._gender = gender

    @property
    def groups(self):
        """
        Gets the groups of this User.

        :return: The groups of this User.
        :rtype: list[GroupMember]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this User.

        :param groups: The groups of this User.
        :type: list[GroupMember]
        """

        self._groups = groups

    @property
    def guest(self):
        """
        Gets the guest of this User.

        :return: The guest of this User.
        :rtype: bool
        """
        return self._guest

    @guest.setter
    def guest(self, guest):
        """
        Sets the guest of this User.

        :param guest: The guest of this User.
        :type: bool
        """

        self._guest = guest

    @property
    def id(self):
        """
        Gets the id of this User.

        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.

        :param id: The id of this User.
        :type: int
        """

        self._id = id

    @property
    def invite_token(self):
        """
        Gets the invite_token of this User.

        :return: The invite_token of this User.
        :rtype: str
        """
        return self._invite_token

    @invite_token.setter
    def invite_token(self, invite_token):
        """
        Sets the invite_token of this User.

        :param invite_token: The invite_token of this User.
        :type: str
        """

        self._invite_token = invite_token

    @property
    def lang(self):
        """
        Gets the lang of this User.

        :return: The lang of this User.
        :rtype: Language
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """
        Sets the lang of this User.

        :param lang: The lang of this User.
        :type: Language
        """

        self._lang = lang

    @property
    def last_activity(self):
        """
        Gets the last_activity of this User.

        :return: The last_activity of this User.
        :rtype: int
        """
        return self._last_activity

    @last_activity.setter
    def last_activity(self, last_activity):
        """
        Sets the last_activity of this User.

        :param last_activity: The last_activity of this User.
        :type: int
        """

        self._last_activity = last_activity

    @property
    def last_login(self):
        """
        Gets the last_login of this User.

        :return: The last_login of this User.
        :rtype: int
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """
        Sets the last_login of this User.

        :param last_login: The last_login of this User.
        :type: int
        """

        self._last_login = last_login

    @property
    def last_name(self):
        """
        Gets the last_name of this User.

        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this User.

        :param last_name: The last_name of this User.
        :type: str
        """

        self._last_name = last_name

    @property
    def lockout_attempts(self):
        """
        Gets the lockout_attempts of this User.

        :return: The lockout_attempts of this User.
        :rtype: int
        """
        return self._lockout_attempts

    @lockout_attempts.setter
    def lockout_attempts(self, lockout_attempts):
        """
        Sets the lockout_attempts of this User.

        :param lockout_attempts: The lockout_attempts of this User.
        :type: int
        """

        self._lockout_attempts = lockout_attempts

    @property
    def lockout_date(self):
        """
        Gets the lockout_date of this User.

        :return: The lockout_date of this User.
        :rtype: int
        """
        return self._lockout_date

    @lockout_date.setter
    def lockout_date(self, lockout_date):
        """
        Sets the lockout_date of this User.

        :param lockout_date: The lockout_date of this User.
        :type: int
        """

        self._lockout_date = lockout_date

    @property
    def mobile_number(self):
        """
        Gets the mobile_number of this User.

        :return: The mobile_number of this User.
        :rtype: str
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        """
        Sets the mobile_number of this User.

        :param mobile_number: The mobile_number of this User.
        :type: str
        """

        self._mobile_number = mobile_number

    @property
    def old_id(self):
        """
        Gets the old_id of this User.

        :return: The old_id of this User.
        :rtype: int
        """
        return self._old_id

    @old_id.setter
    def old_id(self, old_id):
        """
        Sets the old_id of this User.

        :param old_id: The old_id of this User.
        :type: int
        """

        self._old_id = old_id

    @property
    def parents(self):
        """
        Gets the parents of this User.

        :return: The parents of this User.
        :rtype: list[UserRelationship]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """
        Sets the parents of this User.

        :param parents: The parents of this User.
        :type: list[UserRelationship]
        """

        self._parents = parents

    @property
    def password(self):
        """
        Gets the password of this User.

        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this User.

        :param password: The password of this User.
        :type: str
        """

        self._password = password

    @property
    def postal_code(self):
        """
        Gets the postal_code of this User.

        :return: The postal_code of this User.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this User.

        :param postal_code: The postal_code of this User.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def properties_string(self):
        """
        Gets the properties_string of this User.

        :return: The properties_string of this User.
        :rtype: str
        """
        return self._properties_string

    @properties_string.setter
    def properties_string(self, properties_string):
        """
        Sets the properties_string of this User.

        :param properties_string: The properties_string of this User.
        :type: str
        """

        self._properties_string = properties_string

    @property
    def roles(self):
        """
        Gets the roles of this User.

        :return: The roles of this User.
        :rtype: list[Role]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this User.

        :param roles: The roles of this User.
        :type: list[Role]
        """

        self._roles = roles

    @property
    def state(self):
        """
        Gets the state of this User.

        :return: The state of this User.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this User.

        :param state: The state of this User.
        :type: str
        """

        self._state = state

    @property
    def status(self):
        """
        Gets the status of this User.

        :return: The status of this User.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this User.

        :param status: The status of this User.
        :type: str
        """

        self._status = status

    @property
    def tag_strings(self):
        """
        Gets the tag_strings of this User.

        :return: The tag_strings of this User.
        :rtype: list[str]
        """
        return self._tag_strings

    @tag_strings.setter
    def tag_strings(self, tag_strings):
        """
        Sets the tag_strings of this User.

        :param tag_strings: The tag_strings of this User.
        :type: list[str]
        """

        self._tag_strings = tag_strings

    @property
    def tags(self):
        """
        Gets the tags of this User.

        :return: The tags of this User.
        :rtype: list[UserTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this User.

        :param tags: The tags of this User.
        :type: list[UserTag]
        """

        self._tags = tags

    @property
    def template(self):
        """
        Gets the template of this User.

        :return: The template of this User.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this User.

        :param template: The template of this User.
        :type: str
        """

        self._template = template

    @property
    def timezone(self):
        """
        Gets the timezone of this User.

        :return: The timezone of this User.
        :rtype: Timezone
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this User.

        :param timezone: The timezone of this User.
        :type: Timezone
        """

        self._timezone = timezone

    @property
    def token(self):
        """
        Gets the token of this User.

        :return: The token of this User.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this User.

        :param token: The token of this User.
        :type: str
        """

        self._token = token

    @property
    def type_hint(self):
        """
        Gets the type_hint of this User.

        :return: The type_hint of this User.
        :rtype: str
        """
        return self._type_hint

    @type_hint.setter
    def type_hint(self, type_hint):
        """
        Sets the type_hint of this User.

        :param type_hint: The type_hint of this User.
        :type: str
        """

        self._type_hint = type_hint

    @property
    def username(self):
        """
        Gets the username of this User.

        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this User.

        :param username: The username of this User.
        :type: str
        """

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
