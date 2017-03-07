# swagger_client.UtilVersionApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_version**](UtilVersionApi.md#get_version) | **GET** /version | Get current version info


# **get_version**
> Version get_version()

Get current version info

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilVersionApi()

try: 
    # Get current version info
    api_response = api_instance.get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilVersionApi->get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

