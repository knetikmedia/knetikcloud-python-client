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


class CouponDefinition(object):
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
        'code': 'str',
        'description': 'str',
        'discount_type': 'str',
        'exclusive': 'bool',
        'max_discount': 'float',
        'max_quantity': 'int',
        'min_cart_total': 'float',
        'name': 'str',
        'self_exclusive': 'bool',
        'target_item_id': 'int',
        'type': 'str',
        'unique_key': 'str',
        'valid_for_tags': 'list[str]',
        'value': 'float',
        'vendor_id': 'int'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description',
        'discount_type': 'discount_type',
        'exclusive': 'exclusive',
        'max_discount': 'max_discount',
        'max_quantity': 'max_quantity',
        'min_cart_total': 'min_cart_total',
        'name': 'name',
        'self_exclusive': 'self_exclusive',
        'target_item_id': 'target_item_id',
        'type': 'type',
        'unique_key': 'unique_key',
        'valid_for_tags': 'valid_for_tags',
        'value': 'value',
        'vendor_id': 'vendor_id'
    }

    def __init__(self, code=None, description=None, discount_type=None, exclusive=None, max_discount=None, max_quantity=None, min_cart_total=None, name=None, self_exclusive=None, target_item_id=None, type=None, unique_key=None, valid_for_tags=None, value=None, vendor_id=None):
        """
        CouponDefinition - a model defined in Swagger
        """

        self._code = None
        self._description = None
        self._discount_type = None
        self._exclusive = None
        self._max_discount = None
        self._max_quantity = None
        self._min_cart_total = None
        self._name = None
        self._self_exclusive = None
        self._target_item_id = None
        self._type = None
        self._unique_key = None
        self._valid_for_tags = None
        self._value = None
        self._vendor_id = None

        self.code = code
        if description is not None:
          self.description = description
        self.discount_type = discount_type
        if exclusive is not None:
          self.exclusive = exclusive
        if max_discount is not None:
          self.max_discount = max_discount
        if max_quantity is not None:
          self.max_quantity = max_quantity
        if min_cart_total is not None:
          self.min_cart_total = min_cart_total
        self.name = name
        if self_exclusive is not None:
          self.self_exclusive = self_exclusive
        if target_item_id is not None:
          self.target_item_id = target_item_id
        self.type = type
        self.unique_key = unique_key
        if valid_for_tags is not None:
          self.valid_for_tags = valid_for_tags
        self.value = value
        if vendor_id is not None:
          self.vendor_id = vendor_id

    @property
    def code(self):
        """
        Gets the code of this CouponDefinition.
        A unique identifier for the discount. Can be used to remove the discount, and uniqueness within the cart will be enforced.

        :return: The code of this CouponDefinition.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this CouponDefinition.
        A unique identifier for the discount. Can be used to remove the discount, and uniqueness within the cart will be enforced.

        :param code: The code of this CouponDefinition.
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def description(self):
        """
        Gets the description of this CouponDefinition.
        A description for the discount.

        :return: The description of this CouponDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CouponDefinition.
        A description for the discount.

        :param description: The description of this CouponDefinition.
        :type: str
        """

        self._description = description

    @property
    def discount_type(self):
        """
        Gets the discount_type of this CouponDefinition.
        The type of discount in terms of how it deducts price.

        :return: The discount_type of this CouponDefinition.
        :rtype: str
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """
        Sets the discount_type of this CouponDefinition.
        The type of discount in terms of how it deducts price.

        :param discount_type: The discount_type of this CouponDefinition.
        :type: str
        """
        if discount_type is None:
            raise ValueError("Invalid value for `discount_type`, must not be `None`")
        allowed_values = ["value", "percentage"]
        if discount_type not in allowed_values:
            raise ValueError(
                "Invalid value for `discount_type` ({0}), must be one of {1}"
                .format(discount_type, allowed_values)
            )

        self._discount_type = discount_type

    @property
    def exclusive(self):
        """
        Gets the exclusive of this CouponDefinition.
        Whether this discount is exclusive and cannot be used in conjunction with other discounts/coupons. default=false

        :return: The exclusive of this CouponDefinition.
        :rtype: bool
        """
        return self._exclusive

    @exclusive.setter
    def exclusive(self, exclusive):
        """
        Sets the exclusive of this CouponDefinition.
        Whether this discount is exclusive and cannot be used in conjunction with other discounts/coupons. default=false

        :param exclusive: The exclusive of this CouponDefinition.
        :type: bool
        """

        self._exclusive = exclusive

    @property
    def max_discount(self):
        """
        Gets the max_discount of this CouponDefinition.
        For coupon_cart, a minimum total price that the cart must meet to be valid.

        :return: The max_discount of this CouponDefinition.
        :rtype: float
        """
        return self._max_discount

    @max_discount.setter
    def max_discount(self, max_discount):
        """
        Sets the max_discount of this CouponDefinition.
        For coupon_cart, a minimum total price that the cart must meet to be valid.

        :param max_discount: The max_discount of this CouponDefinition.
        :type: float
        """

        self._max_discount = max_discount

    @property
    def max_quantity(self):
        """
        Gets the max_quantity of this CouponDefinition.
        The maximum number of items to count this discount for (not for cart_coupon).

        :return: The max_quantity of this CouponDefinition.
        :rtype: int
        """
        return self._max_quantity

    @max_quantity.setter
    def max_quantity(self, max_quantity):
        """
        Sets the max_quantity of this CouponDefinition.
        The maximum number of items to count this discount for (not for cart_coupon).

        :param max_quantity: The max_quantity of this CouponDefinition.
        :type: int
        """

        self._max_quantity = max_quantity

    @property
    def min_cart_total(self):
        """
        Gets the min_cart_total of this CouponDefinition.
        For coupon_cart, a minimum total price that the cart must meet to be valid.

        :return: The min_cart_total of this CouponDefinition.
        :rtype: float
        """
        return self._min_cart_total

    @min_cart_total.setter
    def min_cart_total(self, min_cart_total):
        """
        Sets the min_cart_total of this CouponDefinition.
        For coupon_cart, a minimum total price that the cart must meet to be valid.

        :param min_cart_total: The min_cart_total of this CouponDefinition.
        :type: float
        """

        self._min_cart_total = min_cart_total

    @property
    def name(self):
        """
        Gets the name of this CouponDefinition.
        A name for the discount.

        :return: The name of this CouponDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CouponDefinition.
        A name for the discount.

        :param name: The name of this CouponDefinition.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def self_exclusive(self):
        """
        Gets the self_exclusive of this CouponDefinition.
        Whether this coupon is exclusive to itself or not (true means cannot add two of this same coupon to the same cart).  Default = false

        :return: The self_exclusive of this CouponDefinition.
        :rtype: bool
        """
        return self._self_exclusive

    @self_exclusive.setter
    def self_exclusive(self, self_exclusive):
        """
        Sets the self_exclusive of this CouponDefinition.
        Whether this coupon is exclusive to itself or not (true means cannot add two of this same coupon to the same cart).  Default = false

        :param self_exclusive: The self_exclusive of this CouponDefinition.
        :type: bool
        """

        self._self_exclusive = self_exclusive

    @property
    def target_item_id(self):
        """
        Gets the target_item_id of this CouponDefinition.
        The id of the item this discount applies to, which must be present in the cart. Applies if coupon_type_hint is coupon_single_item or coupon_voucher.

        :return: The target_item_id of this CouponDefinition.
        :rtype: int
        """
        return self._target_item_id

    @target_item_id.setter
    def target_item_id(self, target_item_id):
        """
        Sets the target_item_id of this CouponDefinition.
        The id of the item this discount applies to, which must be present in the cart. Applies if coupon_type_hint is coupon_single_item or coupon_voucher.

        :param target_item_id: The target_item_id of this CouponDefinition.
        :type: int
        """

        self._target_item_id = target_item_id

    @property
    def type(self):
        """
        Gets the type of this CouponDefinition.
        The type of discount in terms of what it applies to. coupon_cart applies to the cart as a whole, other types apply to specific items based on different criteria.

        :return: The type of this CouponDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CouponDefinition.
        The type of discount in terms of what it applies to. coupon_cart applies to the cart as a whole, other types apply to specific items based on different criteria.

        :param type: The type of this CouponDefinition.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["coupon_cart", "coupon_single_item", "coupon_voucher", "coupon_vendor", "coupon_tag"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def unique_key(self):
        """
        Gets the unique_key of this CouponDefinition.
        A unique identifier string for the discount.

        :return: The unique_key of this CouponDefinition.
        :rtype: str
        """
        return self._unique_key

    @unique_key.setter
    def unique_key(self, unique_key):
        """
        Sets the unique_key of this CouponDefinition.
        A unique identifier string for the discount.

        :param unique_key: The unique_key of this CouponDefinition.
        :type: str
        """
        if unique_key is None:
            raise ValueError("Invalid value for `unique_key`, must not be `None`")

        self._unique_key = unique_key

    @property
    def valid_for_tags(self):
        """
        Gets the valid_for_tags of this CouponDefinition.
        Which tags this applies for (item must have at least one of them), if coupon_type is coupon_tag.

        :return: The valid_for_tags of this CouponDefinition.
        :rtype: list[str]
        """
        return self._valid_for_tags

    @valid_for_tags.setter
    def valid_for_tags(self, valid_for_tags):
        """
        Sets the valid_for_tags of this CouponDefinition.
        Which tags this applies for (item must have at least one of them), if coupon_type is coupon_tag.

        :param valid_for_tags: The valid_for_tags of this CouponDefinition.
        :type: list[str]
        """

        self._valid_for_tags = valid_for_tags

    @property
    def value(self):
        """
        Gets the value of this CouponDefinition.
        The amount of the discount. If discount_type is value then this is the raw currency amount to remove. If discount_type is percentage then this will be multiplied by the cart total or item price to get the discount amount (0.5 is half price).

        :return: The value of this CouponDefinition.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CouponDefinition.
        The amount of the discount. If discount_type is value then this is the raw currency amount to remove. If discount_type is percentage then this will be multiplied by the cart total or item price to get the discount amount (0.5 is half price).

        :param value: The value of this CouponDefinition.
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this CouponDefinition.
        Which vendor this applies for, if coupon_type is coupon_vendor.

        :return: The vendor_id of this CouponDefinition.
        :rtype: int
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this CouponDefinition.
        Which vendor this applies for, if coupon_type is coupon_vendor.

        :param vendor_id: The vendor_id of this CouponDefinition.
        :type: int
        """

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
        if not isinstance(other, CouponDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
