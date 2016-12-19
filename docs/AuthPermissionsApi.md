# swagger_client.AuthPermissionsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_permission_using_post**](AuthPermissionsApi.md#create_permission_using_post) | **POST** /auth/permissions | Create a new permission
[**delete_permission_using_delete**](AuthPermissionsApi.md#delete_permission_using_delete) | **DELETE** /auth/permissions/{permission} | Delete a permission
[**get_permission_using_get**](AuthPermissionsApi.md#get_permission_using_get) | **GET** /auth/permissions/{permission} | Get a single permission
[**get_permission_using_get1**](AuthPermissionsApi.md#get_permission_using_get1) | **GET** /auth/permissions | List and search permissions
[**update_permission_using_put**](AuthPermissionsApi.md#update_permission_using_put) | **PUT** /auth/permissions/{permission} | Update a permission


# **create_permission_using_post**
> PermissionResource create_permission_using_post(permission_resource=permission_resource)

Create a new permission

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
api_instance = swagger_client.AuthPermissionsApi()
permission_resource = swagger_client.PermissionResource() # PermissionResource | The permission resource object (optional)

try: 
    # Create a new permission
    api_response = api_instance.create_permission_using_post(permission_resource=permission_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthPermissionsApi->create_permission_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_resource** | [**PermissionResource**](PermissionResource.md)| The permission resource object | [optional] 

### Return type

[**PermissionResource**](PermissionResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_permission_using_delete**
> delete_permission_using_delete(permission, force=force)

Delete a permission

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
api_instance = swagger_client.AuthPermissionsApi()
permission = 'permission_example' # str | The permission value
force = true # bool | If true, removes permission assigned to roles (optional)

try: 
    # Delete a permission
    api_instance.delete_permission_using_delete(permission, force=force)
except ApiException as e:
    print("Exception when calling AuthPermissionsApi->delete_permission_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| The permission value | 
 **force** | **bool**| If true, removes permission assigned to roles | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permission_using_get**
> PermissionResource get_permission_using_get(permission)

Get a single permission

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
api_instance = swagger_client.AuthPermissionsApi()
permission = 'permission_example' # str | The permission value

try: 
    # Get a single permission
    api_response = api_instance.get_permission_using_get(permission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthPermissionsApi->get_permission_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| The permission value | 

### Return type

[**PermissionResource**](PermissionResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permission_using_get1**
> PagePermissionResource get_permission_using_get1(size=size, page=page, order=order)

List and search permissions

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
api_instance = swagger_client.AuthPermissionsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = '1' # str | a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to 1)

try: 
    # List and search permissions
    api_response = api_instance.get_permission_using_get1(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthPermissionsApi->get_permission_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to 1]

### Return type

[**PagePermissionResource**](PagePermissionResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permission_using_put**
> update_permission_using_put(permission, permission_resource=permission_resource)

Update a permission

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
api_instance = swagger_client.AuthPermissionsApi()
permission = 'permission_example' # str | The permission value
permission_resource = swagger_client.PermissionResource() # PermissionResource | The permission resource object (optional)

try: 
    # Update a permission
    api_instance.update_permission_using_put(permission, permission_resource=permission_resource)
except ApiException as e:
    print("Exception when calling AuthPermissionsApi->update_permission_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| The permission value | 
 **permission_resource** | [**PermissionResource**](PermissionResource.md)| The permission resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

