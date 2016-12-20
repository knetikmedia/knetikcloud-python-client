# swagger_client.UsersGroupsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_using_post**](UsersGroupsApi.md#add_group_using_post) | **POST** /users/groups | Adds a new group in the system
[**add_member_using_post**](UsersGroupsApi.md#add_member_using_post) | **POST** /users/groups/{unique_name}/members | Adds a new member to the group
[**create_group_template_using_post**](UsersGroupsApi.md#create_group_template_using_post) | **POST** /users/groups/templates | Create a group template
[**delete_group_template_using_delete**](UsersGroupsApi.md#delete_group_template_using_delete) | **DELETE** /users/groups/templates/{id} | Delete a group template
[**delete_group_using_delete**](UsersGroupsApi.md#delete_group_using_delete) | **DELETE** /users/groups/{unique_name}/members/{user_id} | Removes a user from a group
[**delete_group_using_delete1**](UsersGroupsApi.md#delete_group_using_delete1) | **DELETE** /users/groups/{unique_name} | Removes a group from the system IF no resources are attached to it
[**get_group_template_using_get**](UsersGroupsApi.md#get_group_template_using_get) | **GET** /users/groups/templates/{id} | Get a single group template
[**get_group_templates_using_get**](UsersGroupsApi.md#get_group_templates_using_get) | **GET** /users/groups/templates | List and search group templates
[**get_group_using_get**](UsersGroupsApi.md#get_group_using_get) | **GET** /users/groups/{unique_name} | Loads a specific group&#39;s details
[**search_groups_using_get**](UsersGroupsApi.md#search_groups_using_get) | **GET** /users/groups/{unique_name}/members | Lists members of the group
[**search_groups_using_get1**](UsersGroupsApi.md#search_groups_using_get1) | **GET** /users/groups | List and search groups
[**update_group_template_using_put**](UsersGroupsApi.md#update_group_template_using_put) | **PUT** /users/groups/templates/{id} | Update a group template
[**update_group_using_put**](UsersGroupsApi.md#update_group_using_put) | **PUT** /users/groups/{unique_name} | Modifies a group&#39;s details
[**update_member_status_using_put**](UsersGroupsApi.md#update_member_status_using_put) | **PUT** /users/groups/{unique_name}/members/{user_id}/status | Change a user&#39;s status


# **add_group_using_post**
> GroupResource add_group_using_post(group_resource=group_resource)

Adds a new group in the system

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
api_instance = swagger_client.UsersGroupsApi()
group_resource = swagger_client.GroupResource() # GroupResource | The new group (optional)

try: 
    # Adds a new group in the system
    api_response = api_instance.add_group_using_post(group_resource=group_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->add_group_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_resource** | [**GroupResource**](GroupResource.md)| The new group | [optional] 

### Return type

[**GroupResource**](GroupResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_member_using_post**
> GroupMemberResource add_member_using_post(unique_name, username)

Adds a new member to the group

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
api_instance = swagger_client.UsersGroupsApi()
unique_name = 'unique_name_example' # str | The group unique name
username = swagger_client.GroupMemberResource() # GroupMemberResource | The username of a user to add to the group

try: 
    # Adds a new member to the group
    api_response = api_instance.add_member_using_post(unique_name, username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->add_member_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **username** | [**GroupMemberResource**](GroupMemberResource.md)| The username of a user to add to the group | 

### Return type

[**GroupMemberResource**](GroupMemberResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_template_using_post**
> TemplateResource create_group_template_using_post(group_template_resource=group_template_resource)

Create a group template

Group Templates define a type of group and the properties they have

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
api_instance = swagger_client.UsersGroupsApi()
group_template_resource = swagger_client.TemplateResource() # TemplateResource | The group template resource object (optional)

try: 
    # Create a group template
    api_response = api_instance.create_group_template_using_post(group_template_resource=group_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->create_group_template_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_template_resource** | [**TemplateResource**](TemplateResource.md)| The group template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_template_using_delete**
> delete_group_template_using_delete(id, cascade=cascade)

Delete a group template

If cascade = 'detach', it will force delete the template even if it's attached to other objects

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
api_instance = swagger_client.UsersGroupsApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a group template
    api_instance.delete_group_template_using_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->delete_group_template_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| The value needed to delete used templates | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_using_delete**
> delete_group_using_delete(unique_name, user_id)

Removes a user from a group

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
api_instance = swagger_client.UsersGroupsApi()
unique_name = 'unique_name_example' # str | The group unique name
user_id = 56 # int | The id of the user to remove

try: 
    # Removes a user from a group
    api_instance.delete_group_using_delete(unique_name, user_id)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->delete_group_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **user_id** | **int**| The id of the user to remove | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_using_delete1**
> delete_group_using_delete1(unique_name)

Removes a group from the system IF no resources are attached to it

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
api_instance = swagger_client.UsersGroupsApi()
unique_name = 'unique_name_example' # str | The group unique name

try: 
    # Removes a group from the system IF no resources are attached to it
    api_instance.delete_group_using_delete1(unique_name)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->delete_group_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_template_using_get**
> TemplateResource get_group_template_using_get(id)

Get a single group template

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
api_instance = swagger_client.UsersGroupsApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single group template
    api_response = api_instance.get_group_template_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->get_group_template_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_templates_using_get**
> PageTemplateResource get_group_templates_using_get(size=size, page=page, order=order)

List and search group templates

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
api_instance = swagger_client.UsersGroupsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search group templates
    api_response = api_instance.get_group_templates_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->get_group_templates_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageTemplateResource**](PageTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_using_get**
> GroupResource get_group_using_get(unique_name)

Loads a specific group's details

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersGroupsApi()
unique_name = 'unique_name_example' # str | The group unique name

try: 
    # Loads a specific group's details
    api_response = api_instance.get_group_using_get(unique_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->get_group_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 

### Return type

[**GroupResource**](GroupResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_groups_using_get**
> PageGroupMemberResource search_groups_using_get(unique_name, size=size, page=page, order=order)

Lists members of the group

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersGroupsApi()
unique_name = 'unique_name_example' # str | The group unique name
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Lists members of the group
    api_response = api_instance.search_groups_using_get(unique_name, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->search_groups_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageGroupMemberResource**](PageGroupMemberResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_groups_using_get1**
> PageGroupResource search_groups_using_get1(size=size, page=page, order=order)

List and search groups

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersGroupsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'name:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to name:ASC)

try: 
    # List and search groups
    api_response = api_instance.search_groups_using_get1(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->search_groups_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to name:ASC]

### Return type

[**PageGroupResource**](PageGroupResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_template_using_put**
> update_group_template_using_put(id, group_template_resource=group_template_resource)

Update a group template

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
api_instance = swagger_client.UsersGroupsApi()
id = 'id_example' # str | The id of the template
group_template_resource = swagger_client.TemplateResource() # TemplateResource | The group template resource object (optional)

try: 
    # Update a group template
    api_instance.update_group_template_using_put(id, group_template_resource=group_template_resource)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->update_group_template_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **group_template_resource** | [**TemplateResource**](TemplateResource.md)| The group template resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_using_put**
> update_group_using_put(unique_name, group_resource=group_resource)

Modifies a group's details

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
api_instance = swagger_client.UsersGroupsApi()
unique_name = 'unique_name_example' # str | The group unique name
group_resource = swagger_client.GroupResource() # GroupResource | The updated group (optional)

try: 
    # Modifies a group's details
    api_instance.update_group_using_put(unique_name, group_resource=group_resource)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->update_group_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **group_resource** | [**GroupResource**](GroupResource.md)| The updated group | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member_status_using_put**
> update_member_status_using_put(unique_name, user_id, status)

Change a user's status

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
api_instance = swagger_client.UsersGroupsApi()
unique_name = 'unique_name_example' # str | The group unique name
user_id = 56 # int | The user id of the member to modify
status = 'status_example' # str | The new status for the user

try: 
    # Change a user's status
    api_instance.update_member_status_using_put(unique_name, user_id, status)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->update_member_status_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **user_id** | **int**| The user id of the member to modify | 
 **status** | **str**| The new status for the user | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

