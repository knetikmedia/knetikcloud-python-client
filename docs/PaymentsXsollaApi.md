# swagger_client.PaymentsXsollaApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token_url_using_post**](PaymentsXsollaApi.md#create_token_url_using_post) | **POST** /payment/provider/xsolla/payment | Create a payment token that should be used to forward the user to Xsolla so they can complete payment
[**receive_notification_using_post**](PaymentsXsollaApi.md#receive_notification_using_post) | **POST** /payment/provider/xsolla/notifications | Receives payment response from Xsolla


# **create_token_url_using_post**
> str create_token_url_using_post(request=request)

Create a payment token that should be used to forward the user to Xsolla so they can complete payment

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
api_instance = swagger_client.PaymentsXsollaApi()
request = swagger_client.XsollaPaymentRequest() # XsollaPaymentRequest | The payment request to be sent to XSolla (optional)

try: 
    # Create a payment token that should be used to forward the user to Xsolla so they can complete payment
    api_response = api_instance.create_token_url_using_post(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsXsollaApi->create_token_url_using_post: %s\n" % e)
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

# **receive_notification_using_post**
> receive_notification_using_post()

Receives payment response from Xsolla

Only used by XSolla to call back to JSAPI after processing user payment action

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsXsollaApi()

try: 
    # Receives payment response from Xsolla
    api_instance.receive_notification_using_post()
except ApiException as e:
    print("Exception when calling PaymentsXsollaApi->receive_notification_using_post: %s\n" % e)
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
