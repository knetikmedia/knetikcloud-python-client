# StripeCreatePaymentMethod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**PaymentMethodDetails**](PaymentMethodDetails.md) | Additional optional details to store on the payment method. If included, all fields in the details will override any defaults | [optional] 
**token** | **str** | A token from Stripe to identify payment info to be tied to the customer | 
**user_id** | **int** | The id of the user, if null the logged in user is used. Admin privilege need to specify other users | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


