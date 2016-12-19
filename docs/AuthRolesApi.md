# swagger_client.AuthRolesApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_client_roles_using_put**](AuthRolesApi.md#assign_client_roles_using_put) | **PUT** /auth/clients/{client_key}/roles | Set roles for a client
[**assign_permissions_using_put**](AuthRolesApi.md#assign_permissions_using_put) | **PUT** /auth/roles/{role}/permissions | Set permissions for a role
[**assign_user_roles_external_using_put**](AuthRolesApi.md#assign_user_roles_external_using_put) | **PUT** /auth/users/{user_id}/roles | Set roles for a user
[**create_role_using_post**](AuthRolesApi.md#create_role_using_post) | **POST** /auth/roles | Create a new role
[**delete_role_using_delete**](AuthRolesApi.md#delete_role_using_delete) | **DELETE** /auth/roles/{role} | Delete a role
[**get_client_roles_using_get**](AuthRolesApi.md#get_client_roles_using_get) | **GET** /auth/clients/{client_key}/roles | Get roles for a client
[**get_role_using_get**](AuthRolesApi.md#get_role_using_get) | **GET** /auth/roles/{role} | Get a single role
[**get_roles_using_get**](AuthRolesApi.md#get_roles_using_get) | **GET** /auth/roles | List and search roles
[**get_user_roles_using_get**](AuthRolesApi.md#get_user_roles_using_get) | **GET** /auth/users/{user_id}/roles | Get roles for a user
[**update_role_using_put**](AuthRolesApi.md#update_role_using_put) | **PUT** /auth/roles/{role} | Update a role


# **assign_client_roles_using_put**
> assign_client_roles_using_put(client_key, roles_list=roles_list)

Set roles for a client

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
api_instance = swagger_client.AuthRolesApi()
client_key = 'client_key_example' # str | The client key
roles_list = [swagger_client.list[str]()] # list[str] | The list of unique roles (optional)

try: 
    # Set roles for a client
    api_instance.assign_client_roles_using_put(client_key, roles_list=roles_list)
except ApiException as e:
    print("Exception when calling AuthRolesApi->assign_client_roles_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| The client key | 
 **roles_list** | **list[str]**| The list of unique roles | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_permissions_using_put**
> assign_permissions_using_put(role, permissions_list=permissions_list)

Set permissions for a role

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
api_instance = swagger_client.AuthRolesApi()
role = 'role_example' # str | The role value
permissions_list = [swagger_client.list[str]()] # list[str] | The list of unique permissions (optional)

try: 
    # Set permissions for a role
    api_instance.assign_permissions_using_put(role, permissions_list=permissions_list)
except ApiException as e:
    print("Exception when calling AuthRolesApi->assign_permissions_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The role value | 
 **permissions_list** | **list[str]**| The list of unique permissions | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_user_roles_external_using_put**
> assign_user_roles_external_using_put(user_id, roles_list=roles_list)

Set roles for a user

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
api_instance = swagger_client.AuthRolesApi()
user_id = 56 # int | The user's id
roles_list = [swagger_client.list[str]()] # list[str] | The list of unique roles (optional)

try: 
    # Set roles for a user
    api_instance.assign_user_roles_external_using_put(user_id, roles_list=roles_list)
except ApiException as e:
    print("Exception when calling AuthRolesApi->assign_user_roles_external_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user&#39;s id | 
 **roles_list** | **list[str]**| The list of unique roles | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role_using_post**
> RoleResource create_role_using_post(role_resource=role_resource)

Create a new role

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
api_instance = swagger_client.AuthRolesApi()
role_resource = swagger_client.RoleResource() # RoleResource | The role resource object (optional)

try: 
    # Create a new role
    api_response = api_instance.create_role_using_post(role_resource=role_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->create_role_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_resource** | [**RoleResource**](RoleResource.md)| The role resource object | [optional] 

### Return type

[**RoleResource**](RoleResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_using_delete**
> delete_role_using_delete(role, force=force)

Delete a role

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
api_instance = swagger_client.AuthRolesApi()
role = 'role_example' # str | The role value
force = true # bool | If true, removes role from users/clients (optional)

try: 
    # Delete a role
    api_instance.delete_role_using_delete(role, force=force)
except ApiException as e:
    print("Exception when calling AuthRolesApi->delete_role_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The role value | 
 **force** | **bool**| If true, removes role from users/clients | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_roles_using_get**
> list[RoleResource] get_client_roles_using_get(client_key)

Get roles for a client

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
api_instance = swagger_client.AuthRolesApi()
client_key = 'client_key_example' # str | The client key

try: 
    # Get roles for a client
    api_response = api_instance.get_client_roles_using_get(client_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->get_client_roles_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| The client key | 

### Return type

[**list[RoleResource]**](RoleResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_using_get**
> RoleResource get_role_using_get(role)

Get a single role

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
api_instance = swagger_client.AuthRolesApi()
role = 'role_example' # str | The role value

try: 
    # Get a single role
    api_response = api_instance.get_role_using_get(role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->get_role_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The role value | 

### Return type

[**RoleResource**](RoleResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles_using_get**
> PageRoleResource get_roles_using_get(size=size, page=page, order=order)

List and search roles

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
api_instance = swagger_client.AuthRolesApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = '1' # str | a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to 1)

try: 
    # List and search roles
    api_response = api_instance.get_roles_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->get_roles_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to 1]

### Return type

[**PageRoleResource**](PageRoleResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles_using_get**
> list[RoleResource] get_user_roles_using_get(user_id)

Get roles for a user

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
api_instance = swagger_client.AuthRolesApi()
user_id = 56 # int | The user's id

try: 
    # Get roles for a user
    api_response = api_instance.get_user_roles_using_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->get_user_roles_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user&#39;s id | 

### Return type

[**list[RoleResource]**](RoleResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role_using_put**
> update_role_using_put(role, role_resource=role_resource)

Update a role

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
api_instance = swagger_client.AuthRolesApi()
role = 'role_example' # str | The role value
role_resource = swagger_client.RoleResource() # RoleResource | The role resource object (optional)

try: 
    # Update a role
    api_instance.update_role_using_put(role, role_resource=role_resource)
except ApiException as e:
    print("Exception when calling AuthRolesApi->update_role_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The role value | 
 **role_resource** | [**RoleResource**](RoleResource.md)| The role resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

