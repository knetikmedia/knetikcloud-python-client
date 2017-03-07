# swagger_client.PaymentsOptimalApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**silent_post_optimal**](PaymentsOptimalApi.md#silent_post_optimal) | **POST** /payment/provider/optimal/silent | Initiate silent post with Optimal


# **silent_post_optimal**
> str silent_post_optimal(request=request)

Initiate silent post with Optimal

Will return the url for a hosted payment endpoint to post to. See Optimal documentation for details.

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
api_instance = swagger_client.PaymentsOptimalApi()
request = swagger_client.OptimalPaymentRequest() # OptimalPaymentRequest | The payment request to initiate (optional)

try: 
    # Initiate silent post with Optimal
    api_response = api_instance.silent_post_optimal(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsOptimalApi->silent_post_optimal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**OptimalPaymentRequest**](OptimalPaymentRequest.md)| The payment request to initiate | [optional] 

### Return type

**str**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

