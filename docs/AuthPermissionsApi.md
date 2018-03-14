# knetik_cloud.AuthPermissionsApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_permission**](AuthPermissionsApi.md#create_permission) | **POST** /auth/permissions | Create a new permission
[**delete_permission**](AuthPermissionsApi.md#delete_permission) | **DELETE** /auth/permissions/{permission} | Delete a permission
[**get_permission**](AuthPermissionsApi.md#get_permission) | **GET** /auth/permissions/{permission} | Get a single permission
[**get_permissions**](AuthPermissionsApi.md#get_permissions) | **GET** /auth/permissions | List and search permissions
[**update_permission**](AuthPermissionsApi.md#update_permission) | **PUT** /auth/permissions/{permission} | Update a permission


# **create_permission**
> PermissionResource create_permission(permission_resource=permission_resource)

Create a new permission

<b>Permissions Needed:</b> PERMISSIONS_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.AuthPermissionsApi(knetik_cloud.ApiClient(configuration))
permission_resource = knetik_cloud.PermissionResource() # PermissionResource | The permission resource object (optional)

try: 
    # Create a new permission
    api_response = api_instance.create_permission(permission_resource=permission_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthPermissionsApi->create_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission_resource** | [**PermissionResource**](PermissionResource.md)| The permission resource object | [optional] 

### Return type

[**PermissionResource**](PermissionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_permission**
> delete_permission(permission, force=force)

Delete a permission

<b>Permissions Needed:</b> PERMISSIONS_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.AuthPermissionsApi(knetik_cloud.ApiClient(configuration))
permission = 'permission_example' # str | The permission value
force = true # bool | If true, removes permission assigned to roles (optional)

try: 
    # Delete a permission
    api_instance.delete_permission(permission, force=force)
except ApiException as e:
    print("Exception when calling AuthPermissionsApi->delete_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| The permission value | 
 **force** | **bool**| If true, removes permission assigned to roles | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permission**
> PermissionResource get_permission(permission)

Get a single permission

<b>Permissions Needed:</b> PERMISSIONS_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.AuthPermissionsApi(knetik_cloud.ApiClient(configuration))
permission = 'permission_example' # str | The permission value

try: 
    # Get a single permission
    api_response = api_instance.get_permission(permission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthPermissionsApi->get_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| The permission value | 

### Return type

[**PermissionResource**](PermissionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permissions**
> PageResourcePermissionResource get_permissions(size=size, page=page, order=order)

List and search permissions

<b>Permissions Needed:</b> PERMISSIONS_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.AuthPermissionsApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'permission:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to permission:ASC)

try: 
    # List and search permissions
    api_response = api_instance.get_permissions(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthPermissionsApi->get_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to permission:ASC]

### Return type

[**PageResourcePermissionResource**](PageResourcePermissionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permission**
> PermissionResource update_permission(permission, permission_resource=permission_resource)

Update a permission

<b>Permissions Needed:</b> PERMISSIONS_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.AuthPermissionsApi(knetik_cloud.ApiClient(configuration))
permission = 'permission_example' # str | The permission value
permission_resource = knetik_cloud.PermissionResource() # PermissionResource | The permission resource object (optional)

try: 
    # Update a permission
    api_response = api_instance.update_permission(permission, permission_resource=permission_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthPermissionsApi->update_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | **str**| The permission value | 
 **permission_resource** | [**PermissionResource**](PermissionResource.md)| The permission resource object | [optional] 

### Return type

[**PermissionResource**](PermissionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

