# knetik_cloud.UsersApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_tag**](UsersApi.md#add_user_tag) | **POST** /users/{user_id}/tags | Add a tag to a user
[**create_user_template**](UsersApi.md#create_user_template) | **POST** /users/templates | Create a user template
[**delete_user_template**](UsersApi.md#delete_user_template) | **DELETE** /users/templates/{id} | Delete a user template
[**get_user**](UsersApi.md#get_user) | **GET** /users/{id} | Get a single user
[**get_user_tags**](UsersApi.md#get_user_tags) | **GET** /users/{user_id}/tags | List tags for a user
[**get_user_template**](UsersApi.md#get_user_template) | **GET** /users/templates/{id} | Get a single user template
[**get_user_templates**](UsersApi.md#get_user_templates) | **GET** /users/templates | List and search user templates
[**get_users**](UsersApi.md#get_users) | **GET** /users | List and search users
[**password_reset**](UsersApi.md#password_reset) | **PUT** /users/{id}/password-reset | Choose a new password after a reset
[**register_user**](UsersApi.md#register_user) | **POST** /users | Register a new user
[**remove_user_tag**](UsersApi.md#remove_user_tag) | **DELETE** /users/{user_id}/tags/{tag} | Remove a tag from a user
[**set_password**](UsersApi.md#set_password) | **PUT** /users/{id}/password | Set a user&#39;s password
[**start_password_reset**](UsersApi.md#start_password_reset) | **POST** /users/{id}/password-reset | Reset a user&#39;s password
[**submit_password_reset**](UsersApi.md#submit_password_reset) | **POST** /users/password-reset | Reset a user&#39;s password without user id
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{id} | Update a user
[**update_user_template**](UsersApi.md#update_user_template) | **PUT** /users/templates/{id} | Update a user template


# **add_user_tag**
> add_user_tag(user_id, tag)

Add a tag to a user

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
api_instance = knetik_cloud.UsersApi(knetik_cloud.ApiClient(configuration))
user_id = 56 # int | The id of the user
tag = knetik_cloud.StringWrapper() # StringWrapper | tag

try: 
    # Add a tag to a user
    api_instance.add_user_tag(user_id, tag)
except ApiException as e:
    print("Exception when calling UsersApi->add_user_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **tag** | [**StringWrapper**](StringWrapper.md)| tag | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_template**
> TemplateResource create_user_template(user_template_resource=user_template_resource)

Create a user template

User Templates define a type of user and the properties they have

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
api_instance = knetik_cloud.UsersApi(knetik_cloud.ApiClient(configuration))
user_template_resource = knetik_cloud.TemplateResource() # TemplateResource | The user template resource object (optional)

try: 
    # Create a user template
    api_response = api_instance.create_user_template(user_template_resource=user_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_template_resource** | [**TemplateResource**](TemplateResource.md)| The user template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_template**
> delete_user_template(id, cascade=cascade)

Delete a user template

If cascade = 'detach', it will force delete the template even if it's attached to other objects

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
api_instance = knetik_cloud.UsersApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a user template
    api_instance.delete_user_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_template: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResource get_user(id)

Get a single user

Additional private info is included as USERS_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersApi()
id = 'id_example' # str | The id of the user or 'me'

try: 
    # Get a single user
    api_response = api_instance.get_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the user or &#39;me&#39; | 

### Return type

[**UserResource**](UserResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_tags**
> list[str] get_user_tags(user_id)

List tags for a user

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
api_instance = knetik_cloud.UsersApi(knetik_cloud.ApiClient(configuration))
user_id = 56 # int | The id of the user

try: 
    # List tags for a user
    api_response = api_instance.get_user_tags(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 

### Return type

**list[str]**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_template**
> TemplateResource get_user_template(id)

Get a single user template

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
api_instance = knetik_cloud.UsersApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template

try: 
    # Get a single user template
    api_response = api_instance.get_user_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_template: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_templates**
> PageResourceTemplateResource get_user_templates(size=size, page=page, order=order)

List and search user templates

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
api_instance = knetik_cloud.UsersApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search user templates
    api_response = api_instance.get_user_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_templates: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> PageResourceUserBaseResource get_users(filter_displayname=filter_displayname, filter_email=filter_email, filter_firstname=filter_firstname, filter_fullname=filter_fullname, filter_lastname=filter_lastname, filter_username=filter_username, filter_tag=filter_tag, filter_group=filter_group, filter_role=filter_role, filter_last_activity=filter_last_activity, filter_id_list=filter_id_list, filter_search=filter_search, size=size, page=page, order=order)

List and search users

Additional private info is included as USERS_ADMIN

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersApi()
filter_displayname = 'filter_displayname_example' # str | Filter for users whose display name starts with provided string. (optional)
filter_email = 'filter_email_example' # str | Filter for users whose email starts with provided string. Requires USERS_ADMIN permission (optional)
filter_firstname = 'filter_firstname_example' # str | Filter for users whose first name starts with provided string. Requires USERS_ADMIN permission (optional)
filter_fullname = 'filter_fullname_example' # str | Filter for users whose full name starts with provided string. Requires USERS_ADMIN permission (optional)
filter_lastname = 'filter_lastname_example' # str | Filter for users whose last name starts with provided string. Requires USERS_ADMIN permission (optional)
filter_username = 'filter_username_example' # str | Filter for users whose username starts with the provided string. Requires USERS_ADMIN permission (optional)
filter_tag = 'filter_tag_example' # str | Filter for users who have a given tag (optional)
filter_group = 'filter_group_example' # str | Filter for users in a given group, by unique name (optional)
filter_role = 'filter_role_example' # str | Filter for users with a given role (optional)
filter_last_activity = 'filter_last_activity_example' # str | A comma separated string without spaces.  First value is the operator to search on, second value is the date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). (optional)
filter_id_list = 'filter_id_list_example' # str | A comma separated list of ids. (optional)
filter_search = 'filter_search_example' # str | Filter for users whose display_name starts with the provided string, or username if display_name is null (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search users
    api_response = api_instance.get_users(filter_displayname=filter_displayname, filter_email=filter_email, filter_firstname=filter_firstname, filter_fullname=filter_fullname, filter_lastname=filter_lastname, filter_username=filter_username, filter_tag=filter_tag, filter_group=filter_group, filter_role=filter_role, filter_last_activity=filter_last_activity, filter_id_list=filter_id_list, filter_search=filter_search, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_displayname** | **str**| Filter for users whose display name starts with provided string. | [optional] 
 **filter_email** | **str**| Filter for users whose email starts with provided string. Requires USERS_ADMIN permission | [optional] 
 **filter_firstname** | **str**| Filter for users whose first name starts with provided string. Requires USERS_ADMIN permission | [optional] 
 **filter_fullname** | **str**| Filter for users whose full name starts with provided string. Requires USERS_ADMIN permission | [optional] 
 **filter_lastname** | **str**| Filter for users whose last name starts with provided string. Requires USERS_ADMIN permission | [optional] 
 **filter_username** | **str**| Filter for users whose username starts with the provided string. Requires USERS_ADMIN permission | [optional] 
 **filter_tag** | **str**| Filter for users who have a given tag | [optional] 
 **filter_group** | **str**| Filter for users in a given group, by unique name | [optional] 
 **filter_role** | **str**| Filter for users with a given role | [optional] 
 **filter_last_activity** | **str**| A comma separated string without spaces.  First value is the operator to search on, second value is the date, a unix timestamp in seconds.  Allowed operators: (GT, LT, EQ, GOE, LOE). | [optional] 
 **filter_id_list** | **str**| A comma separated list of ids. | [optional] 
 **filter_search** | **str**| Filter for users whose display_name starts with the provided string, or username if display_name is null | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceUserBaseResource**](PageResourceUserBaseResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_reset**
> password_reset(id, new_password_request=new_password_request)

Choose a new password after a reset

Finish resetting a user's password using the secret provided from the password-reset endpoint.  Password should be in plain text and will be encrypted on receipt. Use SSL for security.

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersApi()
id = 56 # int | The id of the user
new_password_request = knetik_cloud.NewPasswordRequest() # NewPasswordRequest | The new password request object (optional)

try: 
    # Choose a new password after a reset
    api_instance.password_reset(id, new_password_request=new_password_request)
except ApiException as e:
    print("Exception when calling UsersApi->password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the user | 
 **new_password_request** | [**NewPasswordRequest**](NewPasswordRequest.md)| The new password request object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user**
> UserResource register_user(user_resource=user_resource)

Register a new user

Password should be in plain text and will be encrypted on receipt. Use SSL for security

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersApi()
user_resource = knetik_cloud.UserResource() # UserResource | The user resource object (optional)

try: 
    # Register a new user
    api_response = api_instance.register_user(user_resource=user_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->register_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_resource** | [**UserResource**](UserResource.md)| The user resource object | [optional] 

### Return type

[**UserResource**](UserResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_tag**
> remove_user_tag(user_id, tag)

Remove a tag from a user

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
api_instance = knetik_cloud.UsersApi(knetik_cloud.ApiClient(configuration))
user_id = 56 # int | The id of the user
tag = 'tag_example' # str | The tag to remove

try: 
    # Remove a tag from a user
    api_instance.remove_user_tag(user_id, tag)
except ApiException as e:
    print("Exception when calling UsersApi->remove_user_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **tag** | **str**| The tag to remove | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_password**
> set_password(id, password=password)

Set a user's password

Password should be in plain text and will be encrypted on receipt. Use SSL for security.

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
api_instance = knetik_cloud.UsersApi(knetik_cloud.ApiClient(configuration))
id = 56 # int | The id of the user
password = knetik_cloud.StringWrapper() # StringWrapper | The new plain text password (optional)

try: 
    # Set a user's password
    api_instance.set_password(id, password=password)
except ApiException as e:
    print("Exception when calling UsersApi->set_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the user | 
 **password** | [**StringWrapper**](StringWrapper.md)| The new plain text password | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_password_reset**
> start_password_reset(id)

Reset a user's password

A reset code will be generated and a 'forgot_password' BRE event will be fired with that code.  The default system rule will send an email to the selected user if an email service has been setup. You can modify that rule in BRE to send an SMS instead or any other type of notification as you see fit

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersApi()
id = 56 # int | The id of the user

try: 
    # Reset a user's password
    api_instance.start_password_reset(id)
except ApiException as e:
    print("Exception when calling UsersApi->start_password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_password_reset**
> submit_password_reset(password_reset=password_reset)

Reset a user's password without user id

A reset code will be generated and a 'forgot_password' BRE event will be fired with that code.  The default system rule will send an email to the selected user if an email service has been setup. You can modify that rule in BRE to send an SMS instead or any other type of notification as you see fit.  Must submit their email, username, or mobile phone number

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UsersApi()
password_reset = knetik_cloud.PasswordResetRequest() # PasswordResetRequest | An object containing one of three methods to look up a user (optional)

try: 
    # Reset a user's password without user id
    api_instance.submit_password_reset(password_reset=password_reset)
except ApiException as e:
    print("Exception when calling UsersApi->submit_password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_reset** | [**PasswordResetRequest**](PasswordResetRequest.md)| An object containing one of three methods to look up a user | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(id, user_resource=user_resource)

Update a user

Password will not be edited on this endpoint, use password specific endpoints.

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
api_instance = knetik_cloud.UsersApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the user or 'me'
user_resource = knetik_cloud.UserResource() # UserResource | The user resource object (optional)

try: 
    # Update a user
    api_instance.update_user(id, user_resource=user_resource)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the user or &#39;me&#39; | 
 **user_resource** | [**UserResource**](UserResource.md)| The user resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_template**
> TemplateResource update_user_template(id, user_template_resource=user_template_resource)

Update a user template

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
api_instance = knetik_cloud.UsersApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the template
user_template_resource = knetik_cloud.TemplateResource() # TemplateResource | The user template resource object (optional)

try: 
    # Update a user template
    api_response = api_instance.update_user_template(id, user_template_resource=user_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **user_template_resource** | [**TemplateResource**](TemplateResource.md)| The user template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

