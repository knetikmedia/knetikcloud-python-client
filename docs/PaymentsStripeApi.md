# knetik_cloud.PaymentsStripeApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stripe_payment_method**](PaymentsStripeApi.md#create_stripe_payment_method) | **POST** /payment/provider/stripe/payment-methods | Create a Stripe payment method for a user
[**pay_stripe_invoice**](PaymentsStripeApi.md#pay_stripe_invoice) | **POST** /payment/provider/stripe/payments | Pay with a single use token


# **create_stripe_payment_method**
> PaymentMethodResource create_stripe_payment_method(request=request)

Create a Stripe payment method for a user

Obtain a token from Stripe, following their examples and documentation. Stores customer information and creates a payment method that can be used to pay invoices through the payments endpoints. Ensure that Stripe itself has been configured with the webhook so that invoices are marked paid. <br><br><b>Permissions Needed:</b> STRIPE_ADMIN or owner

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.PaymentsStripeApi(knetik_cloud.ApiClient(configuration))
request = knetik_cloud.StripeCreatePaymentMethod() # StripeCreatePaymentMethod | The request to create a Stripe customer with payment info (optional)

try: 
    # Create a Stripe payment method for a user
    api_response = api_instance.create_stripe_payment_method(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsStripeApi->create_stripe_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**StripeCreatePaymentMethod**](StripeCreatePaymentMethod.md)| The request to create a Stripe customer with payment info | [optional] 

### Return type

[**PaymentMethodResource**](PaymentMethodResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_stripe_invoice**
> pay_stripe_invoice(request=request)

Pay with a single use token

Obtain a token from Stripe, following their examples and documentation. Pays an invoice without creating a payment method. Ensure that Stripe itself has been configured with the webhook so that invoices are marked paid. <br><br><b>Permissions Needed:</b> ANY

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.PaymentsStripeApi(knetik_cloud.ApiClient(configuration))
request = knetik_cloud.StripePaymentRequest() # StripePaymentRequest | The request to pay an invoice (optional)

try: 
    # Pay with a single use token
    api_instance.pay_stripe_invoice(request=request)
except ApiException as e:
    print("Exception when calling PaymentsStripeApi->pay_stripe_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**StripePaymentRequest**](StripePaymentRequest.md)| The request to pay an invoice | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

