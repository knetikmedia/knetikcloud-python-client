# swagger_client.PaymentsGoogleApi

All URIs are relative to *https://integration.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_payment_using_post**](PaymentsGoogleApi.md#handle_payment_using_post) | **POST** /payment/provider/google/payments | Mark an invoice paid with Google


# **handle_payment_using_post**
> int handle_payment_using_post(request=request)

Mark an invoice paid with Google

Mark an invoice paid with Google. Verifies signature from Google and treats the developerPayload field inside the json payload as the id of the invoice to pay. Returns the transaction ID if successful.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsGoogleApi()
request = swagger_client.GooglePaymentRequest() # GooglePaymentRequest | The request for paying an invoice through a Google in-app payment (optional)

try: 
    # Mark an invoice paid with Google
    api_response = api_instance.handle_payment_using_post(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsGoogleApi->handle_payment_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**GooglePaymentRequest**](GooglePaymentRequest.md)| The request for paying an invoice through a Google in-app payment | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

