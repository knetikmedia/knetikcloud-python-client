# swagger_client.BRERuleEngineGlobalsApi

All URIs are relative to *https://sandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bre_global**](BRERuleEngineGlobalsApi.md#create_bre_global) | **POST** /bre/globals/definitions | Create a global definition
[**delete_bre_global**](BRERuleEngineGlobalsApi.md#delete_bre_global) | **DELETE** /bre/globals/definitions/{id} | Delete a global
[**get_bre_global**](BRERuleEngineGlobalsApi.md#get_bre_global) | **GET** /bre/globals/definitions/{id} | Get a single global definition
[**get_bre_globals**](BRERuleEngineGlobalsApi.md#get_bre_globals) | **GET** /bre/globals/definitions | List global definitions
[**update_bre_global**](BRERuleEngineGlobalsApi.md#update_bre_global) | **PUT** /bre/globals/definitions/{id} | Update a global definition


# **create_bre_global**
> BreGlobalResource create_bre_global(bre_global_resource=bre_global_resource)

Create a global definition

Once created you can then use in a custom rule. Note that global definitions cannot be modified or deleted if in use.

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
api_instance = swagger_client.BRERuleEngineGlobalsApi()
bre_global_resource = swagger_client.BreGlobalResource() # BreGlobalResource | The BRE global resource object (optional)

try: 
    # Create a global definition
    api_response = api_instance.create_bre_global(bre_global_resource=bre_global_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineGlobalsApi->create_bre_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bre_global_resource** | [**BreGlobalResource**](BreGlobalResource.md)| The BRE global resource object | [optional] 

### Return type

[**BreGlobalResource**](BreGlobalResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bre_global**
> delete_bre_global(id)

Delete a global

May fail if there are existing rules against it. Cannot delete core globals

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
api_instance = swagger_client.BRERuleEngineGlobalsApi()
id = 'id_example' # str | The id of the global definition

try: 
    # Delete a global
    api_instance.delete_bre_global(id)
except ApiException as e:
    print("Exception when calling BRERuleEngineGlobalsApi->delete_bre_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the global definition | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bre_global**
> BreGlobalResource get_bre_global(id)

Get a single global definition

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
api_instance = swagger_client.BRERuleEngineGlobalsApi()
id = 'id_example' # str | The id of the global definition

try: 
    # Get a single global definition
    api_response = api_instance.get_bre_global(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineGlobalsApi->get_bre_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the global definition | 

### Return type

[**BreGlobalResource**](BreGlobalResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bre_globals**
> PageResourceBreGlobalResource get_bre_globals(filter_system=filter_system, size=size, page=page)

List global definitions

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
api_instance = swagger_client.BRERuleEngineGlobalsApi()
filter_system = true # bool | Filter for globals that are system globals when true, or not when false. Leave off for both mixed (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # List global definitions
    api_response = api_instance.get_bre_globals(filter_system=filter_system, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineGlobalsApi->get_bre_globals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_system** | **bool**| Filter for globals that are system globals when true, or not when false. Leave off for both mixed | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceBreGlobalResource**](PageResourceBreGlobalResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bre_global**
> BreGlobalResource update_bre_global(id, bre_global_resource=bre_global_resource)

Update a global definition

May fail if new parameters mismatch requirements of existing rules. Cannot update core globals

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
api_instance = swagger_client.BRERuleEngineGlobalsApi()
id = 'id_example' # str | The id of the global definition
bre_global_resource = swagger_client.BreGlobalResource() # BreGlobalResource | The BRE global resource object (optional)

try: 
    # Update a global definition
    api_response = api_instance.update_bre_global(id, bre_global_resource=bre_global_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineGlobalsApi->update_bre_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the global definition | 
 **bre_global_resource** | [**BreGlobalResource**](BreGlobalResource.md)| The BRE global resource object | [optional] 

### Return type

[**BreGlobalResource**](BreGlobalResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
