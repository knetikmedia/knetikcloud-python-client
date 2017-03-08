# knetik_cloud.PaymentsXsollaApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_xsolla_token_url**](PaymentsXsollaApi.md#create_xsolla_token_url) | **POST** /payment/provider/xsolla/payment | Create a payment token that should be used to forward the user to Xsolla so they can complete payment
[**receive_xsolla_notification**](PaymentsXsollaApi.md#receive_xsolla_notification) | **POST** /payment/provider/xsolla/notifications | Receives payment response from Xsolla


# **create_xsolla_token_url**
> str create_xsolla_token_url(request=request)

Create a payment token that should be used to forward the user to Xsolla so they can complete payment

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.PaymentsXsollaApi()
request = knetik_cloud.XsollaPaymentRequest() # XsollaPaymentRequest | The payment request to be sent to XSolla (optional)

try: 
    # Create a payment token that should be used to forward the user to Xsolla so they can complete payment
    api_response = api_instance.create_xsolla_token_url(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsXsollaApi->create_xsolla_token_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**XsollaPaymentRequest**](XsollaPaymentRequest.md)| The payment request to be sent to XSolla | [optional] 

### Return type

**str**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive_xsolla_notification**
> receive_xsolla_notification()

Receives payment response from Xsolla

Only used by Xsolla to call back to JSAPI after processing user payment action

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.PaymentsXsollaApi()

try: 
    # Receives payment response from Xsolla
    api_instance.receive_xsolla_notification()
except ApiException as e:
    print("Exception when calling PaymentsXsollaApi->receive_xsolla_notification: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

