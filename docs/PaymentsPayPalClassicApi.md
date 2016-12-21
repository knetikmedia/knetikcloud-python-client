# swagger_client.PaymentsPayPalClassicApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_billing_agreement_url_using_post**](PaymentsPayPalClassicApi.md#create_billing_agreement_url_using_post) | **POST** /payment/provider/paypal/classic/agreements/start | Create a PayPal Classic billing agreement for the user
[**express_checkout_using_post**](PaymentsPayPalClassicApi.md#express_checkout_using_post) | **POST** /payment/provider/paypal/classic/checkout/start | Create a payment token for PayPal express checkout
[**finalize_billing_agreement_using_post**](PaymentsPayPalClassicApi.md#finalize_billing_agreement_using_post) | **POST** /payment/provider/paypal/classic/agreements/finish | Finalizes a billing agreement after the user has accepted through PayPal
[**finalize_checkout_using_post**](PaymentsPayPalClassicApi.md#finalize_checkout_using_post) | **POST** /payment/provider/paypal/classic/checkout/finish | Finalizes a payment after the user has completed checkout with PayPal


# **create_billing_agreement_url_using_post**
> str create_billing_agreement_url_using_post(request=request)

Create a PayPal Classic billing agreement for the user

Returns the token that should be used to forward the user to PayPal so they can accept the agreement.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PaymentsPayPalClassicApi()
request = swagger_client.CreateBillingAgreementRequest() # CreateBillingAgreementRequest | The request to create a PayPal billing agreement (optional)

try: 
    # Create a PayPal Classic billing agreement for the user
    api_response = api_instance.create_billing_agreement_url_using_post(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsPayPalClassicApi->create_billing_agreement_url_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateBillingAgreementRequest**](CreateBillingAgreementRequest.md)| The request to create a PayPal billing agreement | [optional] 

### Return type

**str**

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **express_checkout_using_post**
> str express_checkout_using_post(request=request)

Create a payment token for PayPal express checkout

Returns the token that should be used to forward the user to PayPal so they can complete the checkout.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PaymentsPayPalClassicApi()
request = swagger_client.CreatePayPalPaymentRequest() # CreatePayPalPaymentRequest | The request to create a PayPal payment token (optional)

try: 
    # Create a payment token for PayPal express checkout
    api_response = api_instance.express_checkout_using_post(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsPayPalClassicApi->express_checkout_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreatePayPalPaymentRequest**](CreatePayPalPaymentRequest.md)| The request to create a PayPal payment token | [optional] 

### Return type

**str**

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finalize_billing_agreement_using_post**
> int finalize_billing_agreement_using_post(request=request)

Finalizes a billing agreement after the user has accepted through PayPal

Returns the ID of the new payment method created for the user for the billing agreement.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PaymentsPayPalClassicApi()
request = swagger_client.FinalizeBillingAgreementRequest() # FinalizeBillingAgreementRequest | The request to finalize a PayPal billing agreement (optional)

try: 
    # Finalizes a billing agreement after the user has accepted through PayPal
    api_response = api_instance.finalize_billing_agreement_using_post(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsPayPalClassicApi->finalize_billing_agreement_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**FinalizeBillingAgreementRequest**](FinalizeBillingAgreementRequest.md)| The request to finalize a PayPal billing agreement | [optional] 

### Return type

**int**

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finalize_checkout_using_post**
> finalize_checkout_using_post(request=request)

Finalizes a payment after the user has completed checkout with PayPal

The invoice will be marked paid/failed by asynchronous IPN callback.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PaymentsPayPalClassicApi()
request = swagger_client.FinalizePayPalPaymentRequest() # FinalizePayPalPaymentRequest | The request to finalize the payment (optional)

try: 
    # Finalizes a payment after the user has completed checkout with PayPal
    api_instance.finalize_checkout_using_post(request=request)
except ApiException as e:
    print("Exception when calling PaymentsPayPalClassicApi->finalize_checkout_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**FinalizePayPalPaymentRequest**](FinalizePayPalPaymentRequest.md)| The request to finalize the payment | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

