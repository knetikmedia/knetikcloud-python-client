# swagger_client.BRERuleEngineGlobalsApi

All URIs are relative to *https://devsandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_global_using_post**](BRERuleEngineGlobalsApi.md#create_global_using_post) | **POST** /bre/globals/definitions | Create a global definition
[**delete_global_using_delete**](BRERuleEngineGlobalsApi.md#delete_global_using_delete) | **DELETE** /bre/globals/definitions/{id} | Delete a global
[**get_global_using_get**](BRERuleEngineGlobalsApi.md#get_global_using_get) | **GET** /bre/globals/definitions/{id} | Get a single global definition
[**get_globals_using_get**](BRERuleEngineGlobalsApi.md#get_globals_using_get) | **GET** /bre/globals/definitions | List global definitions
[**update_global_using_put**](BRERuleEngineGlobalsApi.md#update_global_using_put) | **PUT** /bre/globals/definitions/{id} | Update a global definition


# **create_global_using_post**
> BreGlobalResource create_global_using_post(bre_global_resource=bre_global_resource)

Create a global definition

Once created you can then use in a custom rule. Note that global definitions cannot be modified or deleted if in use.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BRERuleEngineGlobalsApi()
bre_global_resource = swagger_client.BreGlobalResource() # BreGlobalResource | The BRE global resource object (optional)

try: 
    # Create a global definition
    api_response = api_instance.create_global_using_post(bre_global_resource=bre_global_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineGlobalsApi->create_global_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bre_global_resource** | [**BreGlobalResource**](BreGlobalResource.md)| The BRE global resource object | [optional] 

### Return type

[**BreGlobalResource**](BreGlobalResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_global_using_delete**
> delete_global_using_delete(id)

Delete a global

May fail if there are existing rules against it. Cannot delete core globals

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BRERuleEngineGlobalsApi()
id = 'id_example' # str | The id of the global definition

try: 
    # Delete a global
    api_instance.delete_global_using_delete(id)
except ApiException as e:
    print("Exception when calling BRERuleEngineGlobalsApi->delete_global_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the global definition | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_global_using_get**
> BreGlobalResource get_global_using_get(id)

Get a single global definition

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BRERuleEngineGlobalsApi()
id = 'id_example' # str | The id of the global definition

try: 
    # Get a single global definition
    api_response = api_instance.get_global_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineGlobalsApi->get_global_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the global definition | 

### Return type

[**BreGlobalResource**](BreGlobalResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_globals_using_get**
> PageBreGlobalResource get_globals_using_get(filter_system=filter_system, size=size, page=page)

List global definitions

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BRERuleEngineGlobalsApi()
filter_system = true # bool | Filter for globals that are system globals when true, or not when false. Leave off for both mixed (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # List global definitions
    api_response = api_instance.get_globals_using_get(filter_system=filter_system, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineGlobalsApi->get_globals_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_system** | **bool**| Filter for globals that are system globals when true, or not when false. Leave off for both mixed | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageBreGlobalResource**](PageBreGlobalResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_global_using_put**
> update_global_using_put(id, bre_global_resource=bre_global_resource)

Update a global definition

May fail if new parameters mismatch requirements of existing rules. Cannot update core globals

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BRERuleEngineGlobalsApi()
id = 'id_example' # str | The id of the global definition
bre_global_resource = swagger_client.BreGlobalResource() # BreGlobalResource | The BRE global resource object (optional)

try: 
    # Update a global definition
    api_instance.update_global_using_put(id, bre_global_resource=bre_global_resource)
except ApiException as e:
    print("Exception when calling BRERuleEngineGlobalsApi->update_global_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the global definition | 
 **bre_global_resource** | [**BreGlobalResource**](BreGlobalResource.md)| The BRE global resource object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

