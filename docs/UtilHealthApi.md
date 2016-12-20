# swagger_client.UtilHealthApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_info_using_get**](UtilHealthApi.md#get_health_info_using_get) | **GET** /health | Get health info


# **get_health_info_using_get**
> object get_health_info_using_get()

Get health info

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilHealthApi()

try: 
    # Get health info
    api_response = api_instance.get_health_info_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilHealthApi->get_health_info_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

