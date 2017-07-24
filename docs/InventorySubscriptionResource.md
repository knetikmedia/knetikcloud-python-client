# InventorySubscriptionResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill_date** | **int** | The date the subscription will be billed | [optional] 
**credit** | **float** | A credit of money already applied to a subscription for the next bill, or a debt if negative | [optional] 
**credit_log** | [**list[SubscriptionCreditResource]**](SubscriptionCreditResource.md) | A record of past and present credit/debt changes | [optional] 
**grace_end** | **int** | The date the grace period ends | [optional] 
**inventory_id** | **int** | The id of the inventory | [optional] 
**inventory_status** | **str** | The inventory status object | [optional] 
**item_id** | **int** | The id of the item | [optional] 
**payment_method** | [**PaymentMethodResource**](PaymentMethodResource.md) | The payment method object | [optional] 
**price_override** | **float** | The recurring price that has been set to override the base price. Null if not overriding | [optional] 
**price_override_reason** | **str** | An explanation for the reason the price is being overridden | [optional] 
**recurring_price** | **float** | The default recurring price | [optional] 
**sku** | **str** | The recurring sku of the subscription | [optional] 
**start_date** | **int** | The date the subscription will start | [optional] 
**subscription_status** | **int** | The status of the subscription | [optional] 
**user** | [**SimpleUserResource**](SimpleUserResource.md) | The user | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


