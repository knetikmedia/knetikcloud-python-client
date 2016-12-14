# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CouponItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, additional_properties=None, behaviors=None, category=None, coupon_type_hint=None, created_date=None, discount_max=None, discount_min_cart_value=None, discount_type=None, discount_value=None, displayable=None, exclusive=None, geo_country_list=None, geo_policy_type=None, id=None, item_id=None, long_description=None, max_quantity=None, name=None, shipping_tier=None, short_description=None, skus=None, sort=None, store_end=None, store_start=None, tags=None, template=None, type_hint=None, unique_key=None, updated_date=None, valid_for_tags=None, vendor_id=None):
        """
        CouponItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'additional_properties': 'dict(str, ModelProperty)',
            'behaviors': 'list[Behavior]',
            'category': 'str',
            'coupon_type_hint': 'str',
            'created_date': 'int',
            'discount_max': 'float',
            'discount_min_cart_value': 'float',
            'discount_type': 'str',
            'discount_value': 'float',
            'displayable': 'bool',
            'exclusive': 'bool',
            'geo_country_list': 'list[str]',
            'geo_policy_type': 'str',
            'id': 'int',
            'item_id': 'int',
            'long_description': 'str',
            'max_quantity': 'int',
            'name': 'str',
            'shipping_tier': 'int',
            'short_description': 'str',
            'skus': 'list[Sku]',
            'sort': 'int',
            'store_end': 'int',
            'store_start': 'int',
            'tags': 'list[str]',
            'template': 'str',
            'type_hint': 'str',
            'unique_key': 'str',
            'updated_date': 'int',
            'valid_for_tags': 'list[str]',
            'vendor_id': 'int'
        }

        self.attribute_map = {
            'additional_properties': 'additional_properties',
            'behaviors': 'behaviors',
            'category': 'category',
            'coupon_type_hint': 'coupon_type_hint',
            'created_date': 'created_date',
            'discount_max': 'discount_max',
            'discount_min_cart_value': 'discount_min_cart_value',
            'discount_type': 'discount_type',
            'discount_value': 'discount_value',
            'displayable': 'displayable',
            'exclusive': 'exclusive',
            'geo_country_list': 'geo_country_list',
            'geo_policy_type': 'geo_policy_type',
            'id': 'id',
            'item_id': 'item_id',
            'long_description': 'long_description',
            'max_quantity': 'max_quantity',
            'name': 'name',
            'shipping_tier': 'shipping_tier',
            'short_description': 'short_description',
            'skus': 'skus',
            'sort': 'sort',
            'store_end': 'store_end',
            'store_start': 'store_start',
            'tags': 'tags',
            'template': 'template',
            'type_hint': 'type_hint',
            'unique_key': 'unique_key',
            'updated_date': 'updated_date',
            'valid_for_tags': 'valid_for_tags',
            'vendor_id': 'vendor_id'
        }

        self._additional_properties = additional_properties
        self._behaviors = behaviors
        self._category = category
        self._coupon_type_hint = coupon_type_hint
        self._created_date = created_date
        self._discount_max = discount_max
        self._discount_min_cart_value = discount_min_cart_value
        self._discount_type = discount_type
        self._discount_value = discount_value
        self._displayable = displayable
        self._exclusive = exclusive
        self._geo_country_list = geo_country_list
        self._geo_policy_type = geo_policy_type
        self._id = id
        self._item_id = item_id
        self._long_description = long_description
        self._max_quantity = max_quantity
        self._name = name
        self._shipping_tier = shipping_tier
        self._short_description = short_description
        self._skus = skus
        self._sort = sort
        self._store_end = store_end
        self._store_start = store_start
        self._tags = tags
        self._template = template
        self._type_hint = type_hint
        self._unique_key = unique_key
        self._updated_date = updated_date
        self._valid_for_tags = valid_for_tags
        self._vendor_id = vendor_id

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this CouponItem.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type, or be an extra not from the template

        :return: The additional_properties of this CouponItem.
        :rtype: dict(str, ModelProperty)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this CouponItem.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type, or be an extra not from the template

        :param additional_properties: The additional_properties of this CouponItem.
        :type: dict(str, ModelProperty)
        """

        self._additional_properties = additional_properties

    @property
    def behaviors(self):
        """
        Gets the behaviors of this CouponItem.
        The behaviors linked to the item, describing various options and interactions. May not be included in item lists

        :return: The behaviors of this CouponItem.
        :rtype: list[Behavior]
        """
        return self._behaviors

    @behaviors.setter
    def behaviors(self, behaviors):
        """
        Sets the behaviors of this CouponItem.
        The behaviors linked to the item, describing various options and interactions. May not be included in item lists

        :param behaviors: The behaviors of this CouponItem.
        :type: list[Behavior]
        """

        self._behaviors = behaviors

    @property
    def category(self):
        """
        Gets the category of this CouponItem.
        A category for filtering items

        :return: The category of this CouponItem.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this CouponItem.
        A category for filtering items

        :param category: The category of this CouponItem.
        :type: str
        """

        self._category = category

    @property
    def coupon_type_hint(self):
        """
        Gets the coupon_type_hint of this CouponItem.
        The type of coupon

        :return: The coupon_type_hint of this CouponItem.
        :rtype: str
        """
        return self._coupon_type_hint

    @coupon_type_hint.setter
    def coupon_type_hint(self, coupon_type_hint):
        """
        Sets the coupon_type_hint of this CouponItem.
        The type of coupon

        :param coupon_type_hint: The coupon_type_hint of this CouponItem.
        :type: str
        """
        allowed_values = ["coupon_cart", "coupon_single_item", "coupon_voucher", "coupon_vendor", "coupon_tag"]
        if coupon_type_hint not in allowed_values:
            raise ValueError(
                "Invalid value for `coupon_type_hint` ({0}), must be one of {1}"
                .format(coupon_type_hint, allowed_values)
            )

        self._coupon_type_hint = coupon_type_hint

    @property
    def created_date(self):
        """
        Gets the created_date of this CouponItem.
        The date the item was created, unix timestamp in seconds

        :return: The created_date of this CouponItem.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this CouponItem.
        The date the item was created, unix timestamp in seconds

        :param created_date: The created_date of this CouponItem.
        :type: int
        """

        self._created_date = created_date

    @property
    def discount_max(self):
        """
        Gets the discount_max of this CouponItem.
        The amount this coupon is maxed out at.  Applies if coupon_type_hint is coupon_cart

        :return: The discount_max of this CouponItem.
        :rtype: float
        """
        return self._discount_max

    @discount_max.setter
    def discount_max(self, discount_max):
        """
        Sets the discount_max of this CouponItem.
        The amount this coupon is maxed out at.  Applies if coupon_type_hint is coupon_cart

        :param discount_max: The discount_max of this CouponItem.
        :type: float
        """

        self._discount_max = discount_max

    @property
    def discount_min_cart_value(self):
        """
        Gets the discount_min_cart_value of this CouponItem.
        The minimium amount needed in the cart for the coupon to apply.  Applies if coupon_type_hint is coupon_cart

        :return: The discount_min_cart_value of this CouponItem.
        :rtype: float
        """
        return self._discount_min_cart_value

    @discount_min_cart_value.setter
    def discount_min_cart_value(self, discount_min_cart_value):
        """
        Sets the discount_min_cart_value of this CouponItem.
        The minimium amount needed in the cart for the coupon to apply.  Applies if coupon_type_hint is coupon_cart

        :param discount_min_cart_value: The discount_min_cart_value of this CouponItem.
        :type: float
        """

        self._discount_min_cart_value = discount_min_cart_value

    @property
    def discount_type(self):
        """
        Gets the discount_type of this CouponItem.
        The type of coupon discount

        :return: The discount_type of this CouponItem.
        :rtype: str
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """
        Sets the discount_type of this CouponItem.
        The type of coupon discount

        :param discount_type: The discount_type of this CouponItem.
        :type: str
        """
        allowed_values = ["value", "percentage"]
        if discount_type not in allowed_values:
            raise ValueError(
                "Invalid value for `discount_type` ({0}), must be one of {1}"
                .format(discount_type, allowed_values)
            )

        self._discount_type = discount_type

    @property
    def discount_value(self):
        """
        Gets the discount_value of this CouponItem.
        The amount the coupon will discount the item

        :return: The discount_value of this CouponItem.
        :rtype: float
        """
        return self._discount_value

    @discount_value.setter
    def discount_value(self, discount_value):
        """
        Sets the discount_value of this CouponItem.
        The amount the coupon will discount the item

        :param discount_value: The discount_value of this CouponItem.
        :type: float
        """
        if discount_value is None:
            raise ValueError("Invalid value for `discount_value`, must not be `None`")

        self._discount_value = discount_value

    @property
    def displayable(self):
        """
        Gets the displayable of this CouponItem.
        Whether or not the item is currently displayable.  Default = true

        :return: The displayable of this CouponItem.
        :rtype: bool
        """
        return self._displayable

    @displayable.setter
    def displayable(self, displayable):
        """
        Sets the displayable of this CouponItem.
        Whether or not the item is currently displayable.  Default = true

        :param displayable: The displayable of this CouponItem.
        :type: bool
        """

        self._displayable = displayable

    @property
    def exclusive(self):
        """
        Gets the exclusive of this CouponItem.
        Whether this coupon is exclusive or not.  Default = false

        :return: The exclusive of this CouponItem.
        :rtype: bool
        """
        return self._exclusive

    @exclusive.setter
    def exclusive(self, exclusive):
        """
        Sets the exclusive of this CouponItem.
        Whether this coupon is exclusive or not.  Default = false

        :param exclusive: The exclusive of this CouponItem.
        :type: bool
        """

        self._exclusive = exclusive

    @property
    def geo_country_list(self):
        """
        Gets the geo_country_list of this CouponItem.
        A list of country ID to include in the blacklist/whitelist geo policy

        :return: The geo_country_list of this CouponItem.
        :rtype: list[str]
        """
        return self._geo_country_list

    @geo_country_list.setter
    def geo_country_list(self, geo_country_list):
        """
        Sets the geo_country_list of this CouponItem.
        A list of country ID to include in the blacklist/whitelist geo policy

        :param geo_country_list: The geo_country_list of this CouponItem.
        :type: list[str]
        """

        self._geo_country_list = geo_country_list

    @property
    def geo_policy_type(self):
        """
        Gets the geo_policy_type of this CouponItem.
        Whether to use the geo_country_list as a black list or white list for item geographical availability

        :return: The geo_policy_type of this CouponItem.
        :rtype: str
        """
        return self._geo_policy_type

    @geo_policy_type.setter
    def geo_policy_type(self, geo_policy_type):
        """
        Sets the geo_policy_type of this CouponItem.
        Whether to use the geo_country_list as a black list or white list for item geographical availability

        :param geo_policy_type: The geo_policy_type of this CouponItem.
        :type: str
        """
        allowed_values = ["whitelist", "blacklist"]
        if geo_policy_type not in allowed_values:
            raise ValueError(
                "Invalid value for `geo_policy_type` ({0}), must be one of {1}"
                .format(geo_policy_type, allowed_values)
            )

        self._geo_policy_type = geo_policy_type

    @property
    def id(self):
        """
        Gets the id of this CouponItem.
        The id of the item

        :return: The id of this CouponItem.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CouponItem.
        The id of the item

        :param id: The id of this CouponItem.
        :type: int
        """

        self._id = id

    @property
    def item_id(self):
        """
        Gets the item_id of this CouponItem.
        The id of the item the coupon is applied to.  Applies if coupon_type_hint is coupon_single_item or coupon_voucher

        :return: The item_id of this CouponItem.
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        Sets the item_id of this CouponItem.
        The id of the item the coupon is applied to.  Applies if coupon_type_hint is coupon_single_item or coupon_voucher

        :param item_id: The item_id of this CouponItem.
        :type: int
        """

        self._item_id = item_id

    @property
    def long_description(self):
        """
        Gets the long_description of this CouponItem.
        A long description of the item

        :return: The long_description of this CouponItem.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this CouponItem.
        A long description of the item

        :param long_description: The long_description of this CouponItem.
        :type: str
        """

        self._long_description = long_description

    @property
    def max_quantity(self):
        """
        Gets the max_quantity of this CouponItem.
        The maximum quantity of items the coupon can apply to, null if no limit and minimum 1 otherwise.  Applies if coupon_type_hint is coupon_single_item or coupon_voucher

        :return: The max_quantity of this CouponItem.
        :rtype: int
        """
        return self._max_quantity

    @max_quantity.setter
    def max_quantity(self, max_quantity):
        """
        Sets the max_quantity of this CouponItem.
        The maximum quantity of items the coupon can apply to, null if no limit and minimum 1 otherwise.  Applies if coupon_type_hint is coupon_single_item or coupon_voucher

        :param max_quantity: The max_quantity of this CouponItem.
        :type: int
        """

        self._max_quantity = max_quantity

    @property
    def name(self):
        """
        Gets the name of this CouponItem.
        The name of the item

        :return: The name of this CouponItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CouponItem.
        The name of the item

        :param name: The name of this CouponItem.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def shipping_tier(self):
        """
        Gets the shipping_tier of this CouponItem.
        Provides the abstract shipping needs if this item is physical and can be shipped.  A value of zero means no shipping needed.  Default = 0

        :return: The shipping_tier of this CouponItem.
        :rtype: int
        """
        return self._shipping_tier

    @shipping_tier.setter
    def shipping_tier(self, shipping_tier):
        """
        Sets the shipping_tier of this CouponItem.
        Provides the abstract shipping needs if this item is physical and can be shipped.  A value of zero means no shipping needed.  Default = 0

        :param shipping_tier: The shipping_tier of this CouponItem.
        :type: int
        """

        self._shipping_tier = shipping_tier

    @property
    def short_description(self):
        """
        Gets the short_description of this CouponItem.
        A short description of the item, max 255 chars

        :return: The short_description of this CouponItem.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this CouponItem.
        A short description of the item, max 255 chars

        :param short_description: The short_description of this CouponItem.
        :type: str
        """

        self._short_description = short_description

    @property
    def skus(self):
        """
        Gets the skus of this CouponItem.
        The skus for the item. Each defines a unique configuration for the item to be purchased (Large-Blue, Small-Green, etc). These are what is ultimately selected in the store and added to the cart

        :return: The skus of this CouponItem.
        :rtype: list[Sku]
        """
        return self._skus

    @skus.setter
    def skus(self, skus):
        """
        Sets the skus of this CouponItem.
        The skus for the item. Each defines a unique configuration for the item to be purchased (Large-Blue, Small-Green, etc). These are what is ultimately selected in the store and added to the cart

        :param skus: The skus of this CouponItem.
        :type: list[Sku]
        """
        if skus is None:
            raise ValueError("Invalid value for `skus`, must not be `None`")

        self._skus = skus

    @property
    def sort(self):
        """
        Gets the sort of this CouponItem.
        A number to use in sorting items.  Default 500

        :return: The sort of this CouponItem.
        :rtype: int
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this CouponItem.
        A number to use in sorting items.  Default 500

        :param sort: The sort of this CouponItem.
        :type: int
        """

        self._sort = sort

    @property
    def store_end(self):
        """
        Gets the store_end of this CouponItem.
        The date the item will leave the store, unix timestamp in seconds.  If set to null, item will never leave the store

        :return: The store_end of this CouponItem.
        :rtype: int
        """
        return self._store_end

    @store_end.setter
    def store_end(self, store_end):
        """
        Sets the store_end of this CouponItem.
        The date the item will leave the store, unix timestamp in seconds.  If set to null, item will never leave the store

        :param store_end: The store_end of this CouponItem.
        :type: int
        """

        self._store_end = store_end

    @property
    def store_start(self):
        """
        Gets the store_start of this CouponItem.
        The date the item will appear in the store, unix timestamp in seconds.  If set to null, item will appear in store immediately

        :return: The store_start of this CouponItem.
        :rtype: int
        """
        return self._store_start

    @store_start.setter
    def store_start(self, store_start):
        """
        Sets the store_start of this CouponItem.
        The date the item will appear in the store, unix timestamp in seconds.  If set to null, item will appear in store immediately

        :param store_start: The store_start of this CouponItem.
        :type: int
        """

        self._store_start = store_start

    @property
    def tags(self):
        """
        Gets the tags of this CouponItem.
        List of tags used for filtering items

        :return: The tags of this CouponItem.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this CouponItem.
        List of tags used for filtering items

        :param tags: The tags of this CouponItem.
        :type: list[str]
        """

        self._tags = tags

    @property
    def template(self):
        """
        Gets the template of this CouponItem.
        An item template this item is validated against.  May be null and no validation of additional_properties will be done.  Default = null

        :return: The template of this CouponItem.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this CouponItem.
        An item template this item is validated against.  May be null and no validation of additional_properties will be done.  Default = null

        :param template: The template of this CouponItem.
        :type: str
        """

        self._template = template

    @property
    def type_hint(self):
        """
        Gets the type_hint of this CouponItem.
        The type of the item

        :return: The type_hint of this CouponItem.
        :rtype: str
        """
        return self._type_hint

    @type_hint.setter
    def type_hint(self, type_hint):
        """
        Sets the type_hint of this CouponItem.
        The type of the item

        :param type_hint: The type_hint of this CouponItem.
        :type: str
        """
        if type_hint is None:
            raise ValueError("Invalid value for `type_hint`, must not be `None`")

        self._type_hint = type_hint

    @property
    def unique_key(self):
        """
        Gets the unique_key of this CouponItem.
        The unique key for the item

        :return: The unique_key of this CouponItem.
        :rtype: str
        """
        return self._unique_key

    @unique_key.setter
    def unique_key(self, unique_key):
        """
        Sets the unique_key of this CouponItem.
        The unique key for the item

        :param unique_key: The unique_key of this CouponItem.
        :type: str
        """

        self._unique_key = unique_key

    @property
    def updated_date(self):
        """
        Gets the updated_date of this CouponItem.
        The date the item was last updated, unix timestamp in seconds

        :return: The updated_date of this CouponItem.
        :rtype: int
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """
        Sets the updated_date of this CouponItem.
        The date the item was last updated, unix timestamp in seconds

        :param updated_date: The updated_date of this CouponItem.
        :type: int
        """

        self._updated_date = updated_date

    @property
    def valid_for_tags(self):
        """
        Gets the valid_for_tags of this CouponItem.
        A list of tags for a coupon.  The coupon can only apply to an item that has at least one of these tags.  Applies if coupon_type_hint is coupon_tag

        :return: The valid_for_tags of this CouponItem.
        :rtype: list[str]
        """
        return self._valid_for_tags

    @valid_for_tags.setter
    def valid_for_tags(self, valid_for_tags):
        """
        Sets the valid_for_tags of this CouponItem.
        A list of tags for a coupon.  The coupon can only apply to an item that has at least one of these tags.  Applies if coupon_type_hint is coupon_tag

        :param valid_for_tags: The valid_for_tags of this CouponItem.
        :type: list[str]
        """

        self._valid_for_tags = valid_for_tags

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this CouponItem.
        The vendor who provides the item

        :return: The vendor_id of this CouponItem.
        :rtype: int
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this CouponItem.
        The vendor who provides the item

        :param vendor_id: The vendor_id of this CouponItem.
        :type: int
        """
        if vendor_id is None:
            raise ValueError("Invalid value for `vendor_id`, must not be `None`")

        self._vendor_id = vendor_id

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
