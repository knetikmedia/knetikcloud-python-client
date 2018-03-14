# knetik_cloud.UsersGroupsApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member_to_group**](UsersGroupsApi.md#add_member_to_group) | **POST** /users/groups/{unique_name}/members | Adds a new member to the group
[**add_members_to_group**](UsersGroupsApi.md#add_members_to_group) | **POST** /users/groups/{unique_name}/members/batch-add | Adds multiple members to the group
[**create_group**](UsersGroupsApi.md#create_group) | **POST** /users/groups | Create a group
[**create_group_member_template**](UsersGroupsApi.md#create_group_member_template) | **POST** /users/groups/members/templates | Create an group member template
[**create_group_template**](UsersGroupsApi.md#create_group_template) | **POST** /users/groups/templates | Create a group template
[**delete_group**](UsersGroupsApi.md#delete_group) | **DELETE** /users/groups/{unique_name} | Removes a group from the system
[**delete_group_member_template**](UsersGroupsApi.md#delete_group_member_template) | **DELETE** /users/groups/members/templates/{id} | Delete an group member template
[**delete_group_template**](UsersGroupsApi.md#delete_group_template) | **DELETE** /users/groups/templates/{id} | Delete a group template
[**disable_group_notification**](UsersGroupsApi.md#disable_group_notification) | **PUT** /users/groups/{unique_name}/members/{user_id}/messages/disabled | Enable or disable notification of group messages
[**get_group**](UsersGroupsApi.md#get_group) | **GET** /users/groups/{unique_name} | Loads a specific group&#39;s details
[**get_group_ancestors**](UsersGroupsApi.md#get_group_ancestors) | **GET** /users/groups/{unique_name}/ancestors | Get group ancestors
[**get_group_member**](UsersGroupsApi.md#get_group_member) | **GET** /users/groups/{unique_name}/members/{user_id} | Get a user from a group
[**get_group_member_template**](UsersGroupsApi.md#get_group_member_template) | **GET** /users/groups/members/templates/{id} | Get a single group member template
[**get_group_member_templates**](UsersGroupsApi.md#get_group_member_templates) | **GET** /users/groups/members/templates | List and search group member templates
[**get_group_members**](UsersGroupsApi.md#get_group_members) | **GET** /users/groups/{unique_name}/members | Lists members of the group
[**get_group_messages**](UsersGroupsApi.md#get_group_messages) | **GET** /users/groups/{unique_name}/messages | Get a list of group messages
[**get_group_template**](UsersGroupsApi.md#get_group_template) | **GET** /users/groups/templates/{id} | Get a single group template
[**get_group_templates**](UsersGroupsApi.md#get_group_templates) | **GET** /users/groups/templates | List and search group templates
[**get_groups_for_user**](UsersGroupsApi.md#get_groups_for_user) | **GET** /users/{user_id}/groups | List groups a user is in
[**list_groups**](UsersGroupsApi.md#list_groups) | **GET** /users/groups | List and search groups
[**post_group_message**](UsersGroupsApi.md#post_group_message) | **POST** /users/groups/{unique_name}/messages | Send a group message
[**remove_group_member**](UsersGroupsApi.md#remove_group_member) | **DELETE** /users/groups/{unique_name}/members/{user_id} | Removes a user from a group
[**update_group**](UsersGroupsApi.md#update_group) | **PUT** /users/groups/{unique_name} | Update a group
[**update_group_member_properties**](UsersGroupsApi.md#update_group_member_properties) | **PUT** /users/groups/{unique_name}/members/{user_id}/order | Change a user&#39;s order
[**update_group_member_properties1**](UsersGroupsApi.md#update_group_member_properties1) | **PUT** /users/groups/{unique_name}/members/{user_id}/properties | Change a user&#39;s membership properties
[**update_group_member_status**](UsersGroupsApi.md#update_group_member_status) | **PUT** /users/groups/{unique_name}/members/{user_id}/status | Change a user&#39;s status
[**update_group_member_template**](UsersGroupsApi.md#update_group_member_template) | **PUT** /users/groups/members/templates/{id} | Update an group member template
[**update_group_template**](UsersGroupsApi.md#update_group_template) | **PUT** /users/groups/templates/{id} | Update a group template


# **add_member_to_group**
> GroupMemberResource add_member_to_group(unique_name, user)

Adds a new member to the group

<b>Permissions Needed:</b> GROUP_ADMIN or self if open

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name
user = knetik_cloud.GroupMemberResource() # GroupMemberResource | The id and status for a user to add to the group

try: 
    # Adds a new member to the group
    api_response = api_instance.add_member_to_group(unique_name, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->add_member_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **user** | [**GroupMemberResource**](GroupMemberResource.md)| The id and status for a user to add to the group | 

### Return type

[**GroupMemberResource**](GroupMemberResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_members_to_group**
> list[GroupMemberResource] add_members_to_group(unique_name, users)

Adds multiple members to the group

<b>Permissions Needed:</b> GROUP_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name
users = [knetik_cloud.GroupMemberResource()] # list[GroupMemberResource] | The id and status for a list of users to add to the group

try: 
    # Adds multiple members to the group
    api_response = api_instance.add_members_to_group(unique_name, users)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->add_members_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **users** | [**list[GroupMemberResource]**](GroupMemberResource.md)| The id and status for a list of users to add to the group | 

### Return type

[**list[GroupMemberResource]**](GroupMemberResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> GroupResource create_group(group_resource=group_resource)

Create a group

<b>Permissions Needed:</b> GROUP_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
group_resource = knetik_cloud.GroupResource() # GroupResource | The new group (optional)

try: 
    # Create a group
    api_response = api_instance.create_group(group_resource=group_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_resource** | [**GroupResource**](GroupResource.md)| The new group | [optional] 

### Return type

[**GroupResource**](GroupResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_member_template**
> TemplateResource create_group_member_template(group_member_template_resource=group_member_template_resource)

Create an group member template

GroupMember Templates define a type of group member and the properties they have. <br><br><b>Permissions Needed:</b> TEMPLATE_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
group_member_template_resource = knetik_cloud.TemplateResource() # TemplateResource | The group member template resource object (optional)

try: 
    # Create an group member template
    api_response = api_instance.create_group_member_template(group_member_template_resource=group_member_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->create_group_member_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_member_template_resource** | [**TemplateResource**](TemplateResource.md)| The group member template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_template**
> TemplateResource create_group_template(group_template_resource=group_template_resource)

Create a group template

Group Templates define a type of group and the properties they have. <br><br><b>Permissions Needed:</b> TEMPLATE_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
group_template_resource = knetik_cloud.TemplateResource() # TemplateResource | The group template resource object (optional)

try: 
    # Create a group template
    api_response = api_instance.create_group_template(group_template_resource=group_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->create_group_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_template_resource** | [**TemplateResource**](TemplateResource.md)| The group template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(unique_name)

Removes a group from the system

All groups listing this as the parent are also removed and users are in turn removed from this and those groups. This may result in users no longer being in this group's parent if they were not added to it directly as well. <br><br><b>Permissions Needed:</b> GROUP_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name

try: 
    # Removes a group from the system
    api_instance.delete_group(unique_name)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_member_template**
> delete_group_member_template(id, cascade=cascade)

Delete an group member template

If cascade = 'detach', it will force delete the template even if it's attached to other objects. <br><br><b>Permissions Needed:</b> TEMPLATE_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete an group member template
    api_instance.delete_group_member_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->delete_group_member_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| The value needed to delete used templates | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_template**
> delete_group_template(id, cascade=cascade)

Delete a group template

If cascade = 'detach', it will force delete the template even if it's attached to other objects. <br><br><b>Permissions Needed:</b> TEMPLATE_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a group template
    api_instance.delete_group_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->delete_group_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| The value needed to delete used templates | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_group_notification**
> disable_group_notification(unique_name, user_id, disabled)

Enable or disable notification of group messages

<b>Permissions Needed:</b> TOPICS_ADMIN or self

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name
user_id = 'user_id_example' # str | The user id of the member or 'me'
disabled = knetik_cloud.ValueWrapperboolean() # ValueWrapperboolean | disabled

try: 
    # Enable or disable notification of group messages
    api_instance.disable_group_notification(unique_name, user_id, disabled)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->disable_group_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **user_id** | **str**| The user id of the member or &#39;me&#39; | 
 **disabled** | [**ValueWrapperboolean**](ValueWrapperboolean.md)| disabled | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> GroupResource get_group(unique_name)

Loads a specific group's details

<b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name

try: 
    # Loads a specific group's details
    api_response = api_instance.get_group(unique_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 

### Return type

[**GroupResource**](GroupResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_ancestors**
> list[GroupResource] get_group_ancestors(unique_name)

Get group ancestors

Returns a list of ancestor groups in reverse order (parent, then grandparent, etc). <br><br><b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name

try: 
    # Get group ancestors
    api_response = api_instance.get_group_ancestors(unique_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->get_group_ancestors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 

### Return type

[**list[GroupResource]**](GroupResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_member**
> GroupMemberResource get_group_member(unique_name, user_id)

Get a user from a group

<b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name
user_id = 56 # int | The id of the user

try: 
    # Get a user from a group
    api_response = api_instance.get_group_member(unique_name, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->get_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **user_id** | **int**| The id of the user | 

### Return type

[**GroupMemberResource**](GroupMemberResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_member_template**
> TemplateResource get_group_member_template(id)

Get a single group member template

<b>Permissions Needed:</b> TEMPLATE_ADMIN or GROUP_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template

try: 
    # Get a single group member template
    api_response = api_instance.get_group_member_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->get_group_member_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_member_templates**
> PageResourceTemplateResource get_group_member_templates(size=size, page=page, order=order)

List and search group member templates

<b>Permissions Needed:</b> TEMPLATE_ADMIN or GROUP_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search group member templates
    api_response = api_instance.get_group_member_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->get_group_member_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceTemplateResource**](PageResourceTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_members**
> PageResourceGroupMemberResource get_group_members(unique_name, size=size, page=page, order=order)

Lists members of the group

<b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'order:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to order:ASC)

try: 
    # Lists members of the group
    api_response = api_instance.get_group_members(unique_name, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->get_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to order:ASC]

### Return type

[**PageResourceGroupMemberResource**](PageResourceGroupMemberResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_messages**
> PageResourceChatMessageResource get_group_messages(unique_name, size=size, page=page)

Get a list of group messages

<b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Get a list of group messages
    api_response = api_instance.get_group_messages(unique_name, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->get_group_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceChatMessageResource**](PageResourceChatMessageResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_template**
> TemplateResource get_group_template(id)

Get a single group template

<b>Permissions Needed:</b> TEMPLATE_ADMIN or GROUP_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template

try: 
    # Get a single group template
    api_response = api_instance.get_group_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->get_group_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_templates**
> PageResourceTemplateResource get_group_templates(size=size, page=page, order=order)

List and search group templates

<b>Permissions Needed:</b> TEMPLATE_ADMIN or GROUP_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search group templates
    api_response = api_instance.get_group_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->get_group_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceTemplateResource**](PageResourceTemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_for_user**
> list[str] get_groups_for_user(user_id, filter_children=filter_children)

List groups a user is in

<b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
user_id = 56 # int | The id of the user
filter_children = true # bool | Whether to limit group list to children of groups only. If true, shows only groups with parents. If false, shows only groups with no parent. (optional)

try: 
    # List groups a user is in
    api_response = api_instance.get_groups_for_user(user_id, filter_children=filter_children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->get_groups_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **filter_children** | **bool**| Whether to limit group list to children of groups only. If true, shows only groups with parents. If false, shows only groups with no parent. | [optional] 

### Return type

**list[str]**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> PageResourceGroupResource list_groups(filter_template=filter_template, filter_member_count=filter_member_count, filter_name=filter_name, filter_unique_name=filter_unique_name, filter_parent=filter_parent, filter_status=filter_status, size=size, page=page, order=order)

List and search groups

<b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
filter_template = 'filter_template_example' # str | Filter for groups using a specific template, by id (optional)
filter_member_count = 'filter_member_count_example' # str | Filters groups by member count. Multiple values possible for range search. Format: filter_member_count=OP,ts&... where OP in (GT, LT, GOE, LOE, EQ). Ex: filter_member_count=GT,14,LT,17 (optional)
filter_name = 'filter_name_example' # str | Filter for groups with names starting with the given string (optional)
filter_unique_name = 'filter_unique_name_example' # str | Filter for groups whose unique_name starts with provided string (optional)
filter_parent = 'filter_parent_example' # str | Filter for groups with a specific parent, by unique name (optional)
filter_status = 'filter_status_example' # str | Filter for groups with a certain status (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'name:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to name:ASC)

try: 
    # List and search groups
    api_response = api_instance.list_groups(filter_template=filter_template, filter_member_count=filter_member_count, filter_name=filter_name, filter_unique_name=filter_unique_name, filter_parent=filter_parent, filter_status=filter_status, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->list_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_template** | **str**| Filter for groups using a specific template, by id | [optional] 
 **filter_member_count** | **str**| Filters groups by member count. Multiple values possible for range search. Format: filter_member_count&#x3D;OP,ts&amp;... where OP in (GT, LT, GOE, LOE, EQ). Ex: filter_member_count&#x3D;GT,14,LT,17 | [optional] 
 **filter_name** | **str**| Filter for groups with names starting with the given string | [optional] 
 **filter_unique_name** | **str**| Filter for groups whose unique_name starts with provided string | [optional] 
 **filter_parent** | **str**| Filter for groups with a specific parent, by unique name | [optional] 
 **filter_status** | **str**| Filter for groups with a certain status | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to name:ASC]

### Return type

[**PageResourceGroupResource**](PageResourceGroupResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_group_message**
> ChatMessageResource post_group_message(unique_name, chat_message_request=chat_message_request)

Send a group message

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersGroupsApi()
unique_name = 'unique_name_example' # str | The group unique name
chat_message_request = knetik_cloud.ChatMessageRequest() # ChatMessageRequest | The chat message request (optional)

try: 
    # Send a group message
    api_response = api_instance.post_group_message(unique_name, chat_message_request=chat_message_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->post_group_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **chat_message_request** | [**ChatMessageRequest**](ChatMessageRequest.md)| The chat message request | [optional] 

### Return type

[**ChatMessageResource**](ChatMessageResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_member**
> remove_group_member(unique_name, user_id)

Removes a user from a group

<b>Permissions Needed:</b> GROUP_ADMIN or self if open

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name
user_id = 56 # int | The id of the user to remove

try: 
    # Removes a user from a group
    api_instance.remove_group_member(unique_name, user_id)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->remove_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **user_id** | **int**| The id of the user to remove | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> update_group(unique_name, group_resource=group_resource)

Update a group

If adding/removing/changing parent, user membership in group/new parent groups may be modified. The parent being removed will remove members from this sub group unless they were added explicitly to the parent and the new parent will gain members unless they were already a part of it. <br><br><b>Permissions Needed:</b> GROUP_ADMIN or admin of the group

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name
group_resource = knetik_cloud.GroupResource() # GroupResource | The updated group (optional)

try: 
    # Update a group
    api_instance.update_group(unique_name, group_resource=group_resource)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **group_resource** | [**GroupResource**](GroupResource.md)| The updated group | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_member_properties**
> update_group_member_properties(unique_name, user_id, order)

Change a user's order

<b>Permissions Needed:</b> GROUP_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name
user_id = 56 # int | The user id of the member to modify
order = knetik_cloud.StringWrapper() # StringWrapper | The new order for the membership

try: 
    # Change a user's order
    api_instance.update_group_member_properties(unique_name, user_id, order)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->update_group_member_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **user_id** | **int**| The user id of the member to modify | 
 **order** | [**StringWrapper**](StringWrapper.md)| The new order for the membership | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_member_properties1**
> update_group_member_properties1(unique_name, user_id, properties)

Change a user's membership properties

<b>Permissions Needed:</b> GROUP_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name
user_id = 56 # int | The user id of the member to modify
properties = NULL # object | The new properties for the membership

try: 
    # Change a user's membership properties
    api_instance.update_group_member_properties1(unique_name, user_id, properties)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->update_group_member_properties1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **user_id** | **int**| The user id of the member to modify | 
 **properties** | **object**| The new properties for the membership | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_member_status**
> update_group_member_status(unique_name, user_id, status)

Change a user's status

<b>Permissions Needed:</b> GROUP_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
unique_name = 'unique_name_example' # str | The group unique name
user_id = 56 # int | The user id of the member to modify
status = knetik_cloud.GroupMemberStatusWrapper() # GroupMemberStatusWrapper | The new status for the user

try: 
    # Change a user's status
    api_instance.update_group_member_status(unique_name, user_id, status)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->update_group_member_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_name** | **str**| The group unique name | 
 **user_id** | **int**| The user id of the member to modify | 
 **status** | [**GroupMemberStatusWrapper**](GroupMemberStatusWrapper.md)| The new status for the user | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_member_template**
> TemplateResource update_group_member_template(id, group_member_template_resource=group_member_template_resource)

Update an group member template

<b>Permissions Needed:</b> TEMPLATE_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
group_member_template_resource = knetik_cloud.TemplateResource() # TemplateResource | The group member template resource object (optional)

try: 
    # Update an group member template
    api_response = api_instance.update_group_member_template(id, group_member_template_resource=group_member_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->update_group_member_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **group_member_template_resource** | [**TemplateResource**](TemplateResource.md)| The group member template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_template**
> TemplateResource update_group_template(id, group_template_resource=group_template_resource)

Update a group template

<b>Permissions Needed:</b> TEMPLATE_ADMIN

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
api_instance = knetik_cloud.UsersGroupsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
group_template_resource = knetik_cloud.TemplateResource() # TemplateResource | The group template resource object (optional)

try: 
    # Update a group template
    api_response = api_instance.update_group_template(id, group_template_resource=group_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersGroupsApi->update_group_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **group_template_resource** | [**TemplateResource**](TemplateResource.md)| The group template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

