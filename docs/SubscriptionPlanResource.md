# SubscriptionPlanResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this subscription | [optional] 
**billing_cycle_length** | **int** | The length of the billing cycle in number of billing cycle unit | 
**billing_cycle_unit** | **str** | The time period unit to apply to the length of billing cycles | 
**consolidated** | **bool** | Whether this plan will be renewed on the consolidated billing cycle | 
**currency_code** | **str** | The ISO3 currency code to use for the fees | 
**end_date** | **int** | Used to schedule plan availability end date | [optional] 
**first_billing_cycle_length** | **int** | Optional override for the length of the first billing cycle before the first recurring billing | [optional] 
**first_billing_cycle_unit** | **str** | The time period unit to apply to the length of the first billing cycle. Required when first_billing_cycle_length is specified | [optional] 
**grace_period** | **int** | The number of late payment days before a subscription is canceled | 
**id** | **str** | The id of the plan used to generate the SKUs | [optional] 
**initial_fee** | **float** | The fee charged when the subscription is purchased | 
**initial_sku** | **str** | The SKU to be used when purchasing the subscription through the cart | [optional] 
**late_payment_fee** | **float** | The fee to add to the bill when an invoice has gone unpaid passed the grace period | 
**late_payment_sku** | **str** | The SKU that will show on the invoice when the subscription is delinquent | [optional] 
**locked** | **bool** | Whether this plan is locked because it has been purchased by at least one user.  When locked, a number of properties can no longer be changed | [optional] 
**max_bill_attempts** | **int** | The number of charge attempts before the subscription becomes delinquent | 
**max_cycles** | **int** | Maximum number of renewals. If a migration plan is provided, the subscription will automatically switch to it when this limit is reached | [optional] 
**migrate_to_plan** | **str** | Automatically migrate to the specified plan when the subscription is first renewed | [optional] 
**min_cycles** | **int** | The minimum number of renewals to charge for | [optional] 
**name** | **str** | The name of the plan used to generate the SKUs | 
**published** | **bool** | Whether this plan is currently available | 
**reactivation_fee** | **float** | The fee to charge when a suspended subscription is to be re-activated | 
**reactivation_sku** | **str** | The SKU that will show on the invoice when the subscription is re-activated after a suspension | [optional] 
**recurring_fee** | **float** | The recurring fee to charge for each renewal | 
**recurring_sku** | **str** | The SKU that will show on the invoice when the subscription is activated | [optional] 
**start_date** | **int** | Used to schedule plan availability start date | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


