# knetik_cloud.PaymentsFattMerchantApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_fatt_merchant_payment_method**](PaymentsFattMerchantApi.md#create_or_update_fatt_merchant_payment_method) | **PUT** /payment/provider/fattmerchant/payment-methods | Create or update a FattMerchant payment method for a user


# **create_or_update_fatt_merchant_payment_method**
> PaymentMethodResource create_or_update_fatt_merchant_payment_method(request=request)

Create or update a FattMerchant payment method for a user

Stores customer information and creates a payment method that can be used to pay invoices through the payments endpoints. <br><br><b>Permissions Needed:</b> FATTMERCHANT_ADMIN or owner

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
api_instance = knetik_cloud.PaymentsFattMerchantApi(knetik_cloud.ApiClient(configuration))
request = knetik_cloud.FattMerchantPaymentMethodRequest() # FattMerchantPaymentMethodRequest | Request containing payment method information for user (optional)

try: 
    # Create or update a FattMerchant payment method for a user
    api_response = api_instance.create_or_update_fatt_merchant_payment_method(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsFattMerchantApi->create_or_update_fatt_merchant_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**FattMerchantPaymentMethodRequest**](FattMerchantPaymentMethodRequest.md)| Request containing payment method information for user | [optional] 

### Return type

[**PaymentMethodResource**](PaymentMethodResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

