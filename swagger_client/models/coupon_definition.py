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


class CouponDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code=None, description=None, discount_type=None, exclusive=None, max_discount=None, max_quantity=None, min_cart_total=None, name=None, self_exclusive=None, target_item_id=None, type=None, valid_for_tags=None, value=None, vendor_id=None):
        """
        CouponDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
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
            'valid_for_tags': 'list[str]',
            'value': 'float',
            'vendor_id': 'int'
        }

        self.attribute_map = {
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
            'valid_for_tags': 'valid_for_tags',
            'value': 'value',
            'vendor_id': 'vendor_id'
        }

        self._code = code
        self._description = description
        self._discount_type = discount_type
        self._exclusive = exclusive
        self._max_discount = max_discount
        self._max_quantity = max_quantity
        self._min_cart_total = min_cart_total
        self._name = name
        self._self_exclusive = self_exclusive
        self._target_item_id = target_item_id
        self._type = type
        self._valid_for_tags = valid_for_tags
        self._value = value
        self._vendor_id = vendor_id

    @property
    def code(self):
        """
        Gets the code of this CouponDefinition.

        :return: The code of this CouponDefinition.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this CouponDefinition.

        :param code: The code of this CouponDefinition.
        :type: str
        """

        self._code = code

    @property
    def description(self):
        """
        Gets the description of this CouponDefinition.

        :return: The description of this CouponDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CouponDefinition.

        :param description: The description of this CouponDefinition.
        :type: str
        """

        self._description = description

    @property
    def discount_type(self):
        """
        Gets the discount_type of this CouponDefinition.

        :return: The discount_type of this CouponDefinition.
        :rtype: str
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """
        Sets the discount_type of this CouponDefinition.

        :param discount_type: The discount_type of this CouponDefinition.
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
    def exclusive(self):
        """
        Gets the exclusive of this CouponDefinition.

        :return: The exclusive of this CouponDefinition.
        :rtype: bool
        """
        return self._exclusive

    @exclusive.setter
    def exclusive(self, exclusive):
        """
        Sets the exclusive of this CouponDefinition.

        :param exclusive: The exclusive of this CouponDefinition.
        :type: bool
        """

        self._exclusive = exclusive

    @property
    def max_discount(self):
        """
        Gets the max_discount of this CouponDefinition.

        :return: The max_discount of this CouponDefinition.
        :rtype: float
        """
        return self._max_discount

    @max_discount.setter
    def max_discount(self, max_discount):
        """
        Sets the max_discount of this CouponDefinition.

        :param max_discount: The max_discount of this CouponDefinition.
        :type: float
        """

        self._max_discount = max_discount

    @property
    def max_quantity(self):
        """
        Gets the max_quantity of this CouponDefinition.

        :return: The max_quantity of this CouponDefinition.
        :rtype: int
        """
        return self._max_quantity

    @max_quantity.setter
    def max_quantity(self, max_quantity):
        """
        Sets the max_quantity of this CouponDefinition.

        :param max_quantity: The max_quantity of this CouponDefinition.
        :type: int
        """

        self._max_quantity = max_quantity

    @property
    def min_cart_total(self):
        """
        Gets the min_cart_total of this CouponDefinition.

        :return: The min_cart_total of this CouponDefinition.
        :rtype: float
        """
        return self._min_cart_total

    @min_cart_total.setter
    def min_cart_total(self, min_cart_total):
        """
        Sets the min_cart_total of this CouponDefinition.

        :param min_cart_total: The min_cart_total of this CouponDefinition.
        :type: float
        """

        self._min_cart_total = min_cart_total

    @property
    def name(self):
        """
        Gets the name of this CouponDefinition.

        :return: The name of this CouponDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CouponDefinition.

        :param name: The name of this CouponDefinition.
        :type: str
        """

        self._name = name

    @property
    def self_exclusive(self):
        """
        Gets the self_exclusive of this CouponDefinition.

        :return: The self_exclusive of this CouponDefinition.
        :rtype: bool
        """
        return self._self_exclusive

    @self_exclusive.setter
    def self_exclusive(self, self_exclusive):
        """
        Sets the self_exclusive of this CouponDefinition.

        :param self_exclusive: The self_exclusive of this CouponDefinition.
        :type: bool
        """

        self._self_exclusive = self_exclusive

    @property
    def target_item_id(self):
        """
        Gets the target_item_id of this CouponDefinition.

        :return: The target_item_id of this CouponDefinition.
        :rtype: int
        """
        return self._target_item_id

    @target_item_id.setter
    def target_item_id(self, target_item_id):
        """
        Sets the target_item_id of this CouponDefinition.

        :param target_item_id: The target_item_id of this CouponDefinition.
        :type: int
        """

        self._target_item_id = target_item_id

    @property
    def type(self):
        """
        Gets the type of this CouponDefinition.

        :return: The type of this CouponDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CouponDefinition.

        :param type: The type of this CouponDefinition.
        :type: str
        """
        allowed_values = ["coupon_cart", "coupon_single_item", "coupon_voucher", "coupon_vendor", "coupon_tag"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def valid_for_tags(self):
        """
        Gets the valid_for_tags of this CouponDefinition.

        :return: The valid_for_tags of this CouponDefinition.
        :rtype: list[str]
        """
        return self._valid_for_tags

    @valid_for_tags.setter
    def valid_for_tags(self, valid_for_tags):
        """
        Sets the valid_for_tags of this CouponDefinition.

        :param valid_for_tags: The valid_for_tags of this CouponDefinition.
        :type: list[str]
        """

        self._valid_for_tags = valid_for_tags

    @property
    def value(self):
        """
        Gets the value of this CouponDefinition.

        :return: The value of this CouponDefinition.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CouponDefinition.

        :param value: The value of this CouponDefinition.
        :type: float
        """

        self._value = value

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this CouponDefinition.

        :return: The vendor_id of this CouponDefinition.
        :rtype: int
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this CouponDefinition.

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
