# swagger_client.UtilBatchApi

All URIs are relative to *https://sandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_batch**](UtilBatchApi.md#send_batch) | **POST** /batch | Request to run API call given the method, content type, path url, and body of request


# **send_batch**
> list[BatchReturn] send_batch(batch=batch)

Request to run API call given the method, content type, path url, and body of request

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilBatchApi()
batch = swagger_client.Batch() # Batch | The batch object (optional)

try: 
    # Request to run API call given the method, content type, path url, and body of request
    api_response = api_instance.send_batch(batch=batch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilBatchApi->send_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch** | [**Batch**](Batch.md)| The batch object | [optional] 

### Return type

[**list[BatchReturn]**](BatchReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

