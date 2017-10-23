# knetik_cloud.PaymentsXsollaApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_xsolla_token_url**](PaymentsXsollaApi.md#create_xsolla_token_url) | **POST** /payment/provider/xsolla/payment | Create a payment token that should be used to forward the user to Xsolla so they can complete payment


# **create_xsolla_token_url**
> str create_xsolla_token_url(request=request)

Create a payment token that should be used to forward the user to Xsolla so they can complete payment

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
api_instance = knetik_cloud.PaymentsXsollaApi(knetik_cloud.ApiClient(configuration))
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

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

