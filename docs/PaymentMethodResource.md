# PaymentMethodResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **int** | The date/time this resource was created in seconds since unix epoch | [optional] 
**default** | **bool** |  | [optional] 
**disabled** | **bool** | Whether this payment method is disabled or not | [optional] 
**expiration_date** | **int** | The expiration date for the payment method, expressed as seconds since epoch. Typically used for credit card payment methods | [optional] 
**expiration_month** | **int** | The expiration month (1 - 12) for the payment method. Typically used for credit card payment methods | [optional] 
**expiration_year** | **int** | The expiration year for the payment method. Typically used for credit card payment methods | [optional] 
**id** | **int** | The unique ID for that resource | [optional] 
**last4** | **str** | The last 4 digits of the account number for the payment method. Typically used for credit card payment methods | [optional] 
**long_description** | **str** | The user friendly name of that resource. Defaults to blank string | [optional] 
**name** | **str** | The user friendly name of that resource | 
**payment_method_type** | [**PaymentMethodTypeResource**](PaymentMethodTypeResource.md) | The type of payment method. Must be a pre-existing value | 
**payment_type** | **str** | The generic payment type. Default is card | [optional] 
**short_description** | **str** | The user friendly name of that resource. Defaults to blank string | [optional] 
**sort** | **int** | The sort value for the payment method | [optional] 
**token** | **str** | The unique token for the payment method | [optional] 
**unique_key** | **str** | An optional unique identifier | [optional] 
**updated_date** | **int** | The date/time this resource was last updated in seconds since unix epoch | [optional] 
**user_id** | **int** | The user&#39;s id. If null, indicates a shared payment method that any user can use (i.e., &#39;wallet&#39;) | [optional] 
**verified** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


