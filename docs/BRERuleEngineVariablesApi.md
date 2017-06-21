# knetik_cloud.BRERuleEngineVariablesApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bre_variable_types**](BRERuleEngineVariablesApi.md#get_bre_variable_types) | **GET** /bre/variable-types | Get a list of variable types available
[**get_bre_variable_values**](BRERuleEngineVariablesApi.md#get_bre_variable_values) | **GET** /bre/variable-types/{name}/values | List valid values for a type


# **get_bre_variable_types**
> list[VariableTypeResource] get_bre_variable_types()

Get a list of variable types available

Types include integer, string, user and invoice. These are used to qualify trigger parameters and action variables with strong typing.

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.BRERuleEngineVariablesApi()

try: 
    # Get a list of variable types available
    api_response = api_instance.get_bre_variable_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineVariablesApi->get_bre_variable_types: %s\n" % e)
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

# **get_bre_variable_values**
> PageResourceSimpleReferenceResourceobject get_bre_variable_values(name, filter_name=filter_name, size=size, page=page)

List valid values for a type

Used to lookup users to fill in a user constant for example. Only types marked as enumerable are suppoorted here.

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.BRERuleEngineVariablesApi()
name = 'name_example' # str | The name of the type
filter_name = 'filter_name_example' # str | Filter results by those with names starting with this string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # List valid values for a type
    api_response = api_instance.get_bre_variable_values(name, filter_name=filter_name, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineVariablesApi->get_bre_variable_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the type | 
 **filter_name** | **str**| Filter results by those with names starting with this string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceSimpleReferenceResourceobject**](PageResourceSimpleReferenceResourceobject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

