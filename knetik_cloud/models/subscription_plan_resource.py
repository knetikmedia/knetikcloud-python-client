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


class SubscriptionPlanResource(object):
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
        'billing_cycle_length': 'int',
        'billing_cycle_unit': 'str',
        'consolidated': 'bool',
        'currency_code': 'str',
        'end_date': 'int',
        'first_billing_cycle_length': 'int',
        'first_billing_cycle_unit': 'str',
        'grace_period': 'int',
        'id': 'str',
        'initial_fee': 'float',
        'initial_sku': 'str',
        'late_payment_fee': 'float',
        'late_payment_sku': 'str',
        'locked': 'bool',
        'max_bill_attempts': 'int',
        'max_cycles': 'int',
        'migrate_to_plan': 'str',
        'min_cycles': 'int',
        'name': 'str',
        'published': 'bool',
        'reactivation_fee': 'float',
        'reactivation_sku': 'str',
        'recurring_fee': 'float',
        'recurring_sku': 'str',
        'start_date': 'int'
    }

    attribute_map = {
        'additional_properties': 'additional_properties',
        'billing_cycle_length': 'billing_cycle_length',
        'billing_cycle_unit': 'billing_cycle_unit',
        'consolidated': 'consolidated',
        'currency_code': 'currency_code',
        'end_date': 'end_date',
        'first_billing_cycle_length': 'first_billing_cycle_length',
        'first_billing_cycle_unit': 'first_billing_cycle_unit',
        'grace_period': 'grace_period',
        'id': 'id',
        'initial_fee': 'initial_fee',
        'initial_sku': 'initial_sku',
        'late_payment_fee': 'late_payment_fee',
        'late_payment_sku': 'late_payment_sku',
        'locked': 'locked',
        'max_bill_attempts': 'max_bill_attempts',
        'max_cycles': 'max_cycles',
        'migrate_to_plan': 'migrate_to_plan',
        'min_cycles': 'min_cycles',
        'name': 'name',
        'published': 'published',
        'reactivation_fee': 'reactivation_fee',
        'reactivation_sku': 'reactivation_sku',
        'recurring_fee': 'recurring_fee',
        'recurring_sku': 'recurring_sku',
        'start_date': 'start_date'
    }

    def __init__(self, additional_properties=None, billing_cycle_length=None, billing_cycle_unit=None, consolidated=None, currency_code=None, end_date=None, first_billing_cycle_length=None, first_billing_cycle_unit=None, grace_period=None, id=None, initial_fee=None, initial_sku=None, late_payment_fee=None, late_payment_sku=None, locked=None, max_bill_attempts=None, max_cycles=None, migrate_to_plan=None, min_cycles=None, name=None, published=None, reactivation_fee=None, reactivation_sku=None, recurring_fee=None, recurring_sku=None, start_date=None):
        """
        SubscriptionPlanResource - a model defined in Swagger
        """

        self._additional_properties = None
        self._billing_cycle_length = None
        self._billing_cycle_unit = None
        self._consolidated = None
        self._currency_code = None
        self._end_date = None
        self._first_billing_cycle_length = None
        self._first_billing_cycle_unit = None
        self._grace_period = None
        self._id = None
        self._initial_fee = None
        self._initial_sku = None
        self._late_payment_fee = None
        self._late_payment_sku = None
        self._locked = None
        self._max_bill_attempts = None
        self._max_cycles = None
        self._migrate_to_plan = None
        self._min_cycles = None
        self._name = None
        self._published = None
        self._reactivation_fee = None
        self._reactivation_sku = None
        self._recurring_fee = None
        self._recurring_sku = None
        self._start_date = None
        self.discriminator = None

        if additional_properties is not None:
          self.additional_properties = additional_properties
        self.billing_cycle_length = billing_cycle_length
        self.billing_cycle_unit = billing_cycle_unit
        self.consolidated = consolidated
        self.currency_code = currency_code
        if end_date is not None:
          self.end_date = end_date
        if first_billing_cycle_length is not None:
          self.first_billing_cycle_length = first_billing_cycle_length
        if first_billing_cycle_unit is not None:
          self.first_billing_cycle_unit = first_billing_cycle_unit
        self.grace_period = grace_period
        if id is not None:
          self.id = id
        self.initial_fee = initial_fee
        if initial_sku is not None:
          self.initial_sku = initial_sku
        self.late_payment_fee = late_payment_fee
        if late_payment_sku is not None:
          self.late_payment_sku = late_payment_sku
        if locked is not None:
          self.locked = locked
        self.max_bill_attempts = max_bill_attempts
        if max_cycles is not None:
          self.max_cycles = max_cycles
        if migrate_to_plan is not None:
          self.migrate_to_plan = migrate_to_plan
        if min_cycles is not None:
          self.min_cycles = min_cycles
        self.name = name
        self.published = published
        self.reactivation_fee = reactivation_fee
        if reactivation_sku is not None:
          self.reactivation_sku = reactivation_sku
        self.recurring_fee = recurring_fee
        if recurring_sku is not None:
          self.recurring_sku = recurring_sku
        if start_date is not None:
          self.start_date = start_date

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this SubscriptionPlanResource.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this subscription

        :return: The additional_properties of this SubscriptionPlanResource.
        :rtype: dict(str, ModelProperty)
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this SubscriptionPlanResource.
        A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this subscription

        :param additional_properties: The additional_properties of this SubscriptionPlanResource.
        :type: dict(str, ModelProperty)
        """

        self._additional_properties = additional_properties

    @property
    def billing_cycle_length(self):
        """
        Gets the billing_cycle_length of this SubscriptionPlanResource.
        The length of the billing cycle in number of billing cycle unit

        :return: The billing_cycle_length of this SubscriptionPlanResource.
        :rtype: int
        """
        return self._billing_cycle_length

    @billing_cycle_length.setter
    def billing_cycle_length(self, billing_cycle_length):
        """
        Sets the billing_cycle_length of this SubscriptionPlanResource.
        The length of the billing cycle in number of billing cycle unit

        :param billing_cycle_length: The billing_cycle_length of this SubscriptionPlanResource.
        :type: int
        """
        if billing_cycle_length is None:
            raise ValueError("Invalid value for `billing_cycle_length`, must not be `None`")

        self._billing_cycle_length = billing_cycle_length

    @property
    def billing_cycle_unit(self):
        """
        Gets the billing_cycle_unit of this SubscriptionPlanResource.
        The time period unit to apply to the length of billing cycles

        :return: The billing_cycle_unit of this SubscriptionPlanResource.
        :rtype: str
        """
        return self._billing_cycle_unit

    @billing_cycle_unit.setter
    def billing_cycle_unit(self, billing_cycle_unit):
        """
        Sets the billing_cycle_unit of this SubscriptionPlanResource.
        The time period unit to apply to the length of billing cycles

        :param billing_cycle_unit: The billing_cycle_unit of this SubscriptionPlanResource.
        :type: str
        """
        if billing_cycle_unit is None:
            raise ValueError("Invalid value for `billing_cycle_unit`, must not be `None`")
        allowed_values = ["millisecond", "second", "minute", "hour", "day", "week", "month", "year"]
        if billing_cycle_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `billing_cycle_unit` ({0}), must be one of {1}"
                .format(billing_cycle_unit, allowed_values)
            )

        self._billing_cycle_unit = billing_cycle_unit

    @property
    def consolidated(self):
        """
        Gets the consolidated of this SubscriptionPlanResource.
        Whether this plan will be renewed on the consolidated billing cycle

        :return: The consolidated of this SubscriptionPlanResource.
        :rtype: bool
        """
        return self._consolidated

    @consolidated.setter
    def consolidated(self, consolidated):
        """
        Sets the consolidated of this SubscriptionPlanResource.
        Whether this plan will be renewed on the consolidated billing cycle

        :param consolidated: The consolidated of this SubscriptionPlanResource.
        :type: bool
        """
        if consolidated is None:
            raise ValueError("Invalid value for `consolidated`, must not be `None`")

        self._consolidated = consolidated

    @property
    def currency_code(self):
        """
        Gets the currency_code of this SubscriptionPlanResource.
        The ISO3 currency code to use for the fees

        :return: The currency_code of this SubscriptionPlanResource.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this SubscriptionPlanResource.
        The ISO3 currency code to use for the fees

        :param currency_code: The currency_code of this SubscriptionPlanResource.
        :type: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")

        self._currency_code = currency_code

    @property
    def end_date(self):
        """
        Gets the end_date of this SubscriptionPlanResource.
        Used to schedule plan availability end date

        :return: The end_date of this SubscriptionPlanResource.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this SubscriptionPlanResource.
        Used to schedule plan availability end date

        :param end_date: The end_date of this SubscriptionPlanResource.
        :type: int
        """

        self._end_date = end_date

    @property
    def first_billing_cycle_length(self):
        """
        Gets the first_billing_cycle_length of this SubscriptionPlanResource.
        Optional override for the length of the first billing cycle before the first recurring billing

        :return: The first_billing_cycle_length of this SubscriptionPlanResource.
        :rtype: int
        """
        return self._first_billing_cycle_length

    @first_billing_cycle_length.setter
    def first_billing_cycle_length(self, first_billing_cycle_length):
        """
        Sets the first_billing_cycle_length of this SubscriptionPlanResource.
        Optional override for the length of the first billing cycle before the first recurring billing

        :param first_billing_cycle_length: The first_billing_cycle_length of this SubscriptionPlanResource.
        :type: int
        """

        self._first_billing_cycle_length = first_billing_cycle_length

    @property
    def first_billing_cycle_unit(self):
        """
        Gets the first_billing_cycle_unit of this SubscriptionPlanResource.
        The time period unit to apply to the length of the first billing cycle. Required when first_billing_cycle_length is specified

        :return: The first_billing_cycle_unit of this SubscriptionPlanResource.
        :rtype: str
        """
        return self._first_billing_cycle_unit

    @first_billing_cycle_unit.setter
    def first_billing_cycle_unit(self, first_billing_cycle_unit):
        """
        Sets the first_billing_cycle_unit of this SubscriptionPlanResource.
        The time period unit to apply to the length of the first billing cycle. Required when first_billing_cycle_length is specified

        :param first_billing_cycle_unit: The first_billing_cycle_unit of this SubscriptionPlanResource.
        :type: str
        """
        allowed_values = ["millisecond", "second", "minute", "hour", "day", "week", "month", "year"]
        if first_billing_cycle_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `first_billing_cycle_unit` ({0}), must be one of {1}"
                .format(first_billing_cycle_unit, allowed_values)
            )

        self._first_billing_cycle_unit = first_billing_cycle_unit

    @property
    def grace_period(self):
        """
        Gets the grace_period of this SubscriptionPlanResource.
        The number of late payment days before a subscription is canceled

        :return: The grace_period of this SubscriptionPlanResource.
        :rtype: int
        """
        return self._grace_period

    @grace_period.setter
    def grace_period(self, grace_period):
        """
        Sets the grace_period of this SubscriptionPlanResource.
        The number of late payment days before a subscription is canceled

        :param grace_period: The grace_period of this SubscriptionPlanResource.
        :type: int
        """
        if grace_period is None:
            raise ValueError("Invalid value for `grace_period`, must not be `None`")

        self._grace_period = grace_period

    @property
    def id(self):
        """
        Gets the id of this SubscriptionPlanResource.
        The id of the plan used to generate the SKUs

        :return: The id of this SubscriptionPlanResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SubscriptionPlanResource.
        The id of the plan used to generate the SKUs

        :param id: The id of this SubscriptionPlanResource.
        :type: str
        """

        self._id = id

    @property
    def initial_fee(self):
        """
        Gets the initial_fee of this SubscriptionPlanResource.
        The fee charged when the subscription is purchased

        :return: The initial_fee of this SubscriptionPlanResource.
        :rtype: float
        """
        return self._initial_fee

    @initial_fee.setter
    def initial_fee(self, initial_fee):
        """
        Sets the initial_fee of this SubscriptionPlanResource.
        The fee charged when the subscription is purchased

        :param initial_fee: The initial_fee of this SubscriptionPlanResource.
        :type: float
        """
        if initial_fee is None:
            raise ValueError("Invalid value for `initial_fee`, must not be `None`")

        self._initial_fee = initial_fee

    @property
    def initial_sku(self):
        """
        Gets the initial_sku of this SubscriptionPlanResource.
        The SKU to be used when purchasing the subscription through the cart

        :return: The initial_sku of this SubscriptionPlanResource.
        :rtype: str
        """
        return self._initial_sku

    @initial_sku.setter
    def initial_sku(self, initial_sku):
        """
        Sets the initial_sku of this SubscriptionPlanResource.
        The SKU to be used when purchasing the subscription through the cart

        :param initial_sku: The initial_sku of this SubscriptionPlanResource.
        :type: str
        """

        self._initial_sku = initial_sku

    @property
    def late_payment_fee(self):
        """
        Gets the late_payment_fee of this SubscriptionPlanResource.
        The fee to add to the bill when an invoice has gone unpaid passed the grace period

        :return: The late_payment_fee of this SubscriptionPlanResource.
        :rtype: float
        """
        return self._late_payment_fee

    @late_payment_fee.setter
    def late_payment_fee(self, late_payment_fee):
        """
        Sets the late_payment_fee of this SubscriptionPlanResource.
        The fee to add to the bill when an invoice has gone unpaid passed the grace period

        :param late_payment_fee: The late_payment_fee of this SubscriptionPlanResource.
        :type: float
        """
        if late_payment_fee is None:
            raise ValueError("Invalid value for `late_payment_fee`, must not be `None`")

        self._late_payment_fee = late_payment_fee

    @property
    def late_payment_sku(self):
        """
        Gets the late_payment_sku of this SubscriptionPlanResource.
        The SKU that will show on the invoice when the subscription is delinquent

        :return: The late_payment_sku of this SubscriptionPlanResource.
        :rtype: str
        """
        return self._late_payment_sku

    @late_payment_sku.setter
    def late_payment_sku(self, late_payment_sku):
        """
        Sets the late_payment_sku of this SubscriptionPlanResource.
        The SKU that will show on the invoice when the subscription is delinquent

        :param late_payment_sku: The late_payment_sku of this SubscriptionPlanResource.
        :type: str
        """

        self._late_payment_sku = late_payment_sku

    @property
    def locked(self):
        """
        Gets the locked of this SubscriptionPlanResource.
        Whether this plan is locked because it has been purchased by at least one user.  When locked, a number of properties can no longer be changed

        :return: The locked of this SubscriptionPlanResource.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """
        Sets the locked of this SubscriptionPlanResource.
        Whether this plan is locked because it has been purchased by at least one user.  When locked, a number of properties can no longer be changed

        :param locked: The locked of this SubscriptionPlanResource.
        :type: bool
        """

        self._locked = locked

    @property
    def max_bill_attempts(self):
        """
        Gets the max_bill_attempts of this SubscriptionPlanResource.
        The number of charge attempts before the subscription becomes delinquent

        :return: The max_bill_attempts of this SubscriptionPlanResource.
        :rtype: int
        """
        return self._max_bill_attempts

    @max_bill_attempts.setter
    def max_bill_attempts(self, max_bill_attempts):
        """
        Sets the max_bill_attempts of this SubscriptionPlanResource.
        The number of charge attempts before the subscription becomes delinquent

        :param max_bill_attempts: The max_bill_attempts of this SubscriptionPlanResource.
        :type: int
        """
        if max_bill_attempts is None:
            raise ValueError("Invalid value for `max_bill_attempts`, must not be `None`")

        self._max_bill_attempts = max_bill_attempts

    @property
    def max_cycles(self):
        """
        Gets the max_cycles of this SubscriptionPlanResource.
        Maximum number of renewals. If a migration plan is provided, the subscription will automatically switch to it when this limit is reached

        :return: The max_cycles of this SubscriptionPlanResource.
        :rtype: int
        """
        return self._max_cycles

    @max_cycles.setter
    def max_cycles(self, max_cycles):
        """
        Sets the max_cycles of this SubscriptionPlanResource.
        Maximum number of renewals. If a migration plan is provided, the subscription will automatically switch to it when this limit is reached

        :param max_cycles: The max_cycles of this SubscriptionPlanResource.
        :type: int
        """

        self._max_cycles = max_cycles

    @property
    def migrate_to_plan(self):
        """
        Gets the migrate_to_plan of this SubscriptionPlanResource.
        Automatically migrate to the specified plan when the subscription is first renewed

        :return: The migrate_to_plan of this SubscriptionPlanResource.
        :rtype: str
        """
        return self._migrate_to_plan

    @migrate_to_plan.setter
    def migrate_to_plan(self, migrate_to_plan):
        """
        Sets the migrate_to_plan of this SubscriptionPlanResource.
        Automatically migrate to the specified plan when the subscription is first renewed

        :param migrate_to_plan: The migrate_to_plan of this SubscriptionPlanResource.
        :type: str
        """

        self._migrate_to_plan = migrate_to_plan

    @property
    def min_cycles(self):
        """
        Gets the min_cycles of this SubscriptionPlanResource.
        The minimum number of renewals to charge for

        :return: The min_cycles of this SubscriptionPlanResource.
        :rtype: int
        """
        return self._min_cycles

    @min_cycles.setter
    def min_cycles(self, min_cycles):
        """
        Sets the min_cycles of this SubscriptionPlanResource.
        The minimum number of renewals to charge for

        :param min_cycles: The min_cycles of this SubscriptionPlanResource.
        :type: int
        """

        self._min_cycles = min_cycles

    @property
    def name(self):
        """
        Gets the name of this SubscriptionPlanResource.
        The name of the plan used to generate the SKUs

        :return: The name of this SubscriptionPlanResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SubscriptionPlanResource.
        The name of the plan used to generate the SKUs

        :param name: The name of this SubscriptionPlanResource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def published(self):
        """
        Gets the published of this SubscriptionPlanResource.
        Whether this plan is currently available

        :return: The published of this SubscriptionPlanResource.
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """
        Sets the published of this SubscriptionPlanResource.
        Whether this plan is currently available

        :param published: The published of this SubscriptionPlanResource.
        :type: bool
        """
        if published is None:
            raise ValueError("Invalid value for `published`, must not be `None`")

        self._published = published

    @property
    def reactivation_fee(self):
        """
        Gets the reactivation_fee of this SubscriptionPlanResource.
        The fee to charge when a suspended subscription is to be re-activated

        :return: The reactivation_fee of this SubscriptionPlanResource.
        :rtype: float
        """
        return self._reactivation_fee

    @reactivation_fee.setter
    def reactivation_fee(self, reactivation_fee):
        """
        Sets the reactivation_fee of this SubscriptionPlanResource.
        The fee to charge when a suspended subscription is to be re-activated

        :param reactivation_fee: The reactivation_fee of this SubscriptionPlanResource.
        :type: float
        """
        if reactivation_fee is None:
            raise ValueError("Invalid value for `reactivation_fee`, must not be `None`")

        self._reactivation_fee = reactivation_fee

    @property
    def reactivation_sku(self):
        """
        Gets the reactivation_sku of this SubscriptionPlanResource.
        The SKU that will show on the invoice when the subscription is re-activated after a suspension

        :return: The reactivation_sku of this SubscriptionPlanResource.
        :rtype: str
        """
        return self._reactivation_sku

    @reactivation_sku.setter
    def reactivation_sku(self, reactivation_sku):
        """
        Sets the reactivation_sku of this SubscriptionPlanResource.
        The SKU that will show on the invoice when the subscription is re-activated after a suspension

        :param reactivation_sku: The reactivation_sku of this SubscriptionPlanResource.
        :type: str
        """

        self._reactivation_sku = reactivation_sku

    @property
    def recurring_fee(self):
        """
        Gets the recurring_fee of this SubscriptionPlanResource.
        The recurring fee to charge for each renewal

        :return: The recurring_fee of this SubscriptionPlanResource.
        :rtype: float
        """
        return self._recurring_fee

    @recurring_fee.setter
    def recurring_fee(self, recurring_fee):
        """
        Sets the recurring_fee of this SubscriptionPlanResource.
        The recurring fee to charge for each renewal

        :param recurring_fee: The recurring_fee of this SubscriptionPlanResource.
        :type: float
        """
        if recurring_fee is None:
            raise ValueError("Invalid value for `recurring_fee`, must not be `None`")

        self._recurring_fee = recurring_fee

    @property
    def recurring_sku(self):
        """
        Gets the recurring_sku of this SubscriptionPlanResource.
        The SKU that will show on the invoice when the subscription is activated

        :return: The recurring_sku of this SubscriptionPlanResource.
        :rtype: str
        """
        return self._recurring_sku

    @recurring_sku.setter
    def recurring_sku(self, recurring_sku):
        """
        Sets the recurring_sku of this SubscriptionPlanResource.
        The SKU that will show on the invoice when the subscription is activated

        :param recurring_sku: The recurring_sku of this SubscriptionPlanResource.
        :type: str
        """

        self._recurring_sku = recurring_sku

    @property
    def start_date(self):
        """
        Gets the start_date of this SubscriptionPlanResource.
        Used to schedule plan availability start date

        :return: The start_date of this SubscriptionPlanResource.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this SubscriptionPlanResource.
        Used to schedule plan availability start date

        :param start_date: The start_date of this SubscriptionPlanResource.
        :type: int
        """

        self._start_date = start_date

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
        if not isinstance(other, SubscriptionPlanResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
