# swagger_client.BRERuleEngineVariablesApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_using_get**](BRERuleEngineVariablesApi.md#get_list_using_get) | **GET** /bre/variable-types | Get a list of variable types available


# **get_list_using_get**
> list[VariableTypeResource] get_list_using_get()

Get a list of variable types available

Types include integer, string, user and invoice. These are used to qualify trigger parameters and action variables with strong typing.

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
api_instance = swagger_client.BRERuleEngineVariablesApi()

try: 
    # Get a list of variable types available
    api_response = api_instance.get_list_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineVariablesApi->get_list_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VariableTypeResource]**](VariableTypeResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

