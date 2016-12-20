# swagger_client.PaymentsStripeApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_using_post1**](PaymentsStripeApi.md#create_customer_using_post1) | **POST** /payment/provider/stripe/payment-methods | Create a Stripe payment method for a user
[**pay_invoice_using_post1**](PaymentsStripeApi.md#pay_invoice_using_post1) | **POST** /payment/provider/stripe/payments | Pay with a single use token


# **create_customer_using_post1**
> PaymentMethodResource create_customer_using_post1(request=request)

Create a Stripe payment method for a user

Stores customer information and creates a payment method that can be used to pay invoices through the payments endpoints.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PaymentsStripeApi()
request = swagger_client.StripeCreatePaymentMethod() # StripeCreatePaymentMethod | The request to create a Stripe customer with payment info (optional)

try: 
    # Create a Stripe payment method for a user
    api_response = api_instance.create_customer_using_post1(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsStripeApi->create_customer_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**StripeCreatePaymentMethod**](StripeCreatePaymentMethod.md)| The request to create a Stripe customer with payment info | [optional] 

### Return type

[**PaymentMethodResource**](PaymentMethodResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_invoice_using_post1**
> pay_invoice_using_post1(request=request)

Pay with a single use token

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsStripeApi()
request = swagger_client.StripePaymentRequest() # StripePaymentRequest | The request to pay an invoice (optional)

try: 
    # Pay with a single use token
    api_instance.pay_invoice_using_post1(request=request)
except ApiException as e:
    print("Exception when calling PaymentsStripeApi->pay_invoice_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**StripePaymentRequest**](StripePaymentRequest.md)| The request to pay an invoice | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

