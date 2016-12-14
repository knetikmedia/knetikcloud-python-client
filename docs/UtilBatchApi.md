# swagger_client.UtilBatchApi

All URIs are relative to *https://devsandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_batch_post_using_post**](UtilBatchApi.md#get_batch_post_using_post) | **POST** /batch | Request to run API call given the method, content type, path url, and body of request


# **get_batch_post_using_post**
> get_batch_post_using_post(batch=batch)

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
    api_instance.get_batch_post_using_post(batch=batch)
except ApiException as e:
    print("Exception when calling UtilBatchApi->get_batch_post_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch** | [**Batch**](Batch.md)| The batch object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

