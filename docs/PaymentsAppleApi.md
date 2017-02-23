# swagger_client.PaymentsAppleApi

All URIs are relative to *https://sandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_apple_receipt**](PaymentsAppleApi.md#verify_apple_receipt) | **POST** /payment/provider/apple/receipt | Pay invoice with Apple receipt


# **verify_apple_receipt**
> str verify_apple_receipt(request=request)

Pay invoice with Apple receipt

Mark an invoice paid using Apple payment receipt. A receipt will only be accepted once and the details of the transaction must match the invoice, including the product_id matching the sku text of the item in the invoice. Returns the transaction ID if successful.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsAppleApi()
request = swagger_client.ApplyPaymentRequest() # ApplyPaymentRequest | The request for paying an invoice through an Apple receipt (optional)

try: 
    # Pay invoice with Apple receipt
    api_response = api_instance.verify_apple_receipt(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsAppleApi->verify_apple_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ApplyPaymentRequest**](ApplyPaymentRequest.md)| The request for paying an invoice through an Apple receipt | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

