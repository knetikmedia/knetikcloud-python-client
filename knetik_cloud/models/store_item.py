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


class StoreItem(object):
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
        'displayable': 'bool',
        'geo_country_list': 'list[str]',
        'geo_policy_type': 'str',
        'shipping_tier': 'int',
        'skus': 'list[Sku]',
        'store_end': 'int',
        'store_start': 'int',
        'vendor_id': 'int'
    }

    attribute_map = {
        'displayable': 'displayable',
        'geo_country_list': 'geo_country_list',
        'geo_policy_type': 'geo_policy_type',
        'shipping_tier': 'shipping_tier',
        'skus': 'skus',
        'store_end': 'store_end',
        'store_start': 'store_start',
        'vendor_id': 'vendor_id'
    }

    def __init__(self, displayable=None, geo_country_list=None, geo_policy_type=None, shipping_tier=None, skus=None, store_end=None, store_start=None, vendor_id=None):
        """
        StoreItem - a model defined in Swagger
        """

        self._displayable = None
        self._geo_country_list = None
        self._geo_policy_type = None
        self._shipping_tier = None
        self._skus = None
        self._store_end = None
        self._store_start = None
        self._vendor_id = None
        self.discriminator = None

        if displayable is not None:
          self.displayable = displayable
        if geo_country_list is not None:
          self.geo_country_list = geo_country_list
        if geo_policy_type is not None:
          self.geo_policy_type = geo_policy_type
        if shipping_tier is not None:
          self.shipping_tier = shipping_tier
        self.skus = skus
        if store_end is not None:
          self.store_end = store_end
        if store_start is not None:
          self.store_start = store_start
        self.vendor_id = vendor_id

    @property
    def displayable(self):
        """
        Gets the displayable of this StoreItem.
        Whether or not the item is currently visible to users. Does not block purchase; Use store_start or store_end to block purchase.  Default = true

        :return: The displayable of this StoreItem.
        :rtype: bool
        """
        return self._displayable

    @displayable.setter
    def displayable(self, displayable):
        """
        Sets the displayable of this StoreItem.
        Whether or not the item is currently visible to users. Does not block purchase; Use store_start or store_end to block purchase.  Default = true

        :param displayable: The displayable of this StoreItem.
        :type: bool
        """

        self._displayable = displayable

    @property
    def geo_country_list(self):
        """
        Gets the geo_country_list of this StoreItem.
        A list of country ID to include in the blacklist/whitelist geo policy

        :return: The geo_country_list of this StoreItem.
        :rtype: list[str]
        """
        return self._geo_country_list

    @geo_country_list.setter
    def geo_country_list(self, geo_country_list):
        """
        Sets the geo_country_list of this StoreItem.
        A list of country ID to include in the blacklist/whitelist geo policy

        :param geo_country_list: The geo_country_list of this StoreItem.
        :type: list[str]
        """

        self._geo_country_list = geo_country_list

    @property
    def geo_policy_type(self):
        """
        Gets the geo_policy_type of this StoreItem.
        Whether to use the geo_country_list as a black list or white list for item geographical availability

        :return: The geo_policy_type of this StoreItem.
        :rtype: str
        """
        return self._geo_policy_type

    @geo_policy_type.setter
    def geo_policy_type(self, geo_policy_type):
        """
        Sets the geo_policy_type of this StoreItem.
        Whether to use the geo_country_list as a black list or white list for item geographical availability

        :param geo_policy_type: The geo_policy_type of this StoreItem.
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
    def shipping_tier(self):
        """
        Gets the shipping_tier of this StoreItem.
        Provides the abstract shipping needs if this item is physical and can be shipped.  A value of zero means no shipping needed.  Default = 0

        :return: The shipping_tier of this StoreItem.
        :rtype: int
        """
        return self._shipping_tier

    @shipping_tier.setter
    def shipping_tier(self, shipping_tier):
        """
        Sets the shipping_tier of this StoreItem.
        Provides the abstract shipping needs if this item is physical and can be shipped.  A value of zero means no shipping needed.  Default = 0

        :param shipping_tier: The shipping_tier of this StoreItem.
        :type: int
        """

        self._shipping_tier = shipping_tier

    @property
    def skus(self):
        """
        Gets the skus of this StoreItem.
        The skus for the item. Each defines a unique configuration for the item to be purchased (Large-Blue, Small-Green, etc). These are what is ultimately selected in the store and added to the cart

        :return: The skus of this StoreItem.
        :rtype: list[Sku]
        """
        return self._skus

    @skus.setter
    def skus(self, skus):
        """
        Sets the skus of this StoreItem.
        The skus for the item. Each defines a unique configuration for the item to be purchased (Large-Blue, Small-Green, etc). These are what is ultimately selected in the store and added to the cart

        :param skus: The skus of this StoreItem.
        :type: list[Sku]
        """
        if skus is None:
            raise ValueError("Invalid value for `skus`, must not be `None`")

        self._skus = skus

    @property
    def store_end(self):
        """
        Gets the store_end of this StoreItem.
        The date the item will become hidden and unavailable for purchase, unix timestamp in seconds.  If set to null, item will never leave the store

        :return: The store_end of this StoreItem.
        :rtype: int
        """
        return self._store_end

    @store_end.setter
    def store_end(self, store_end):
        """
        Sets the store_end of this StoreItem.
        The date the item will become hidden and unavailable for purchase, unix timestamp in seconds.  If set to null, item will never leave the store

        :param store_end: The store_end of this StoreItem.
        :type: int
        """

        self._store_end = store_end

    @property
    def store_start(self):
        """
        Gets the store_start of this StoreItem.
        The date the item will become visible (if displayable) and available for purchase, unix timestamp in seconds.  If set to null, item will appear in store immediately

        :return: The store_start of this StoreItem.
        :rtype: int
        """
        return self._store_start

    @store_start.setter
    def store_start(self, store_start):
        """
        Sets the store_start of this StoreItem.
        The date the item will become visible (if displayable) and available for purchase, unix timestamp in seconds.  If set to null, item will appear in store immediately

        :param store_start: The store_start of this StoreItem.
        :type: int
        """

        self._store_start = store_start

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this StoreItem.
        The vendor who provides the item

        :return: The vendor_id of this StoreItem.
        :rtype: int
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this StoreItem.
        The vendor who provides the item

        :param vendor_id: The vendor_id of this StoreItem.
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
        if not isinstance(other, StoreItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
