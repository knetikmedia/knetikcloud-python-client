# knetik_cloud.AuthRolesApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](AuthRolesApi.md#create_role) | **POST** /auth/roles | Create a new role
[**delete_role**](AuthRolesApi.md#delete_role) | **DELETE** /auth/roles/{role} | Delete a role
[**get_client_roles**](AuthRolesApi.md#get_client_roles) | **GET** /auth/clients/{client_key}/roles | Get roles for a client
[**get_role**](AuthRolesApi.md#get_role) | **GET** /auth/roles/{role} | Get a single role
[**get_roles**](AuthRolesApi.md#get_roles) | **GET** /auth/roles | List and search roles
[**get_user_roles**](AuthRolesApi.md#get_user_roles) | **GET** /auth/users/{user_id}/roles | Get roles for a user
[**set_client_roles**](AuthRolesApi.md#set_client_roles) | **PUT** /auth/clients/{client_key}/roles | Set roles for a client
[**set_permissions_for_role**](AuthRolesApi.md#set_permissions_for_role) | **PUT** /auth/roles/{role}/permissions | Set permissions for a role
[**set_user_roles**](AuthRolesApi.md#set_user_roles) | **PUT** /auth/users/{user_id}/roles | Set roles for a user
[**update_role**](AuthRolesApi.md#update_role) | **PUT** /auth/roles/{role} | Update a role


# **create_role**
> RoleResource create_role(role_resource=role_resource)

Create a new role

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
api_instance = knetik_cloud.AuthRolesApi()
role_resource = knetik_cloud.RoleResource() # RoleResource | The role resource object (optional)

try: 
    # Create a new role
    api_response = api_instance.create_role(role_resource=role_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->create_role: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(role, force=force)

Delete a role

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
api_instance = knetik_cloud.AuthRolesApi()
role = 'role_example' # str | The role value
force = true # bool | If true, removes role from users/clients (optional)

try: 
    # Delete a role
    api_instance.delete_role(role, force=force)
except ApiException as e:
    print("Exception when calling AuthRolesApi->delete_role: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_roles**
> list[RoleResource] get_client_roles(client_key)

Get roles for a client

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
api_instance = knetik_cloud.AuthRolesApi()
client_key = 'client_key_example' # str | The client key

try: 
    # Get roles for a client
    api_response = api_instance.get_client_roles(client_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->get_client_roles: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleResource get_role(role)

Get a single role

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
api_instance = knetik_cloud.AuthRolesApi()
role = 'role_example' # str | The role value

try: 
    # Get a single role
    api_response = api_instance.get_role(role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->get_role: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> PageResourceRoleResource get_roles(size=size, page=page, order=order)

List and search roles

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
api_instance = knetik_cloud.AuthRolesApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'name:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to name:ASC)

try: 
    # List and search roles
    api_response = api_instance.get_roles(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->get_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to name:ASC]

### Return type

[**PageResourceRoleResource**](PageResourceRoleResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> list[RoleResource] get_user_roles(user_id)

Get roles for a user

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
api_instance = knetik_cloud.AuthRolesApi()
user_id = 56 # int | The user's id

try: 
    # Get roles for a user
    api_response = api_instance.get_user_roles(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->get_user_roles: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_client_roles**
> ClientResource set_client_roles(client_key, roles_list=roles_list)

Set roles for a client

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
api_instance = knetik_cloud.AuthRolesApi()
client_key = 'client_key_example' # str | The client key
roles_list = [knetik_cloud.list[str]()] # list[str] | The list of unique roles (optional)

try: 
    # Set roles for a client
    api_response = api_instance.set_client_roles(client_key, roles_list=roles_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->set_client_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| The client key | 
 **roles_list** | **list[str]**| The list of unique roles | [optional] 

### Return type

[**ClientResource**](ClientResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_permissions_for_role**
> RoleResource set_permissions_for_role(role, permissions_list=permissions_list)

Set permissions for a role

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
api_instance = knetik_cloud.AuthRolesApi()
role = 'role_example' # str | The role value
permissions_list = [knetik_cloud.list[str]()] # list[str] | The list of unique permissions (optional)

try: 
    # Set permissions for a role
    api_response = api_instance.set_permissions_for_role(role, permissions_list=permissions_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->set_permissions_for_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The role value | 
 **permissions_list** | **list[str]**| The list of unique permissions | [optional] 

### Return type

[**RoleResource**](RoleResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_roles**
> UserResource set_user_roles(user_id, roles_list=roles_list)

Set roles for a user

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
api_instance = knetik_cloud.AuthRolesApi()
user_id = 56 # int | The user's id
roles_list = [knetik_cloud.list[str]()] # list[str] | The list of unique roles (optional)

try: 
    # Set roles for a user
    api_response = api_instance.set_user_roles(user_id, roles_list=roles_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->set_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user&#39;s id | 
 **roles_list** | **list[str]**| The list of unique roles | [optional] 

### Return type

[**UserResource**](UserResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> RoleResource update_role(role, role_resource=role_resource)

Update a role

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
api_instance = knetik_cloud.AuthRolesApi()
role = 'role_example' # str | The role value
role_resource = knetik_cloud.RoleResource() # RoleResource | The role resource object (optional)

try: 
    # Update a role
    api_response = api_instance.update_role(role, role_resource=role_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The role value | 
 **role_resource** | [**RoleResource**](RoleResource.md)| The role resource object | [optional] 

### Return type

[**RoleResource**](RoleResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

