# swagger_client.UsersApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tag_using_post1**](UsersApi.md#add_tag_using_post1) | **POST** /users/{user_id}/tags | Add a tag to a user
[**create_user_template_using_post**](UsersApi.md#create_user_template_using_post) | **POST** /users/templates | Create a user template
[**delete_user_template_using_delete**](UsersApi.md#delete_user_template_using_delete) | **DELETE** /users/templates/{id} | Delete a user template
[**do_password_reset_using_put**](UsersApi.md#do_password_reset_using_put) | **PUT** /users/{id}/password-reset | Choose a new password after a reset
[**get_tags_using_get3**](UsersApi.md#get_tags_using_get3) | **GET** /users/{user_id}/tags | List tags for a user
[**get_user_template_using_get**](UsersApi.md#get_user_template_using_get) | **GET** /users/templates/{id} | Get a single user template
[**get_user_templates_using_get**](UsersApi.md#get_user_templates_using_get) | **GET** /users/templates | List and search user templates
[**get_user_using_get**](UsersApi.md#get_user_using_get) | **GET** /users/{id} | Get a single user
[**get_users_using_get**](UsersApi.md#get_users_using_get) | **GET** /users | List and search users
[**initiate_password_reset_using_post**](UsersApi.md#initiate_password_reset_using_post) | **POST** /users/{id}/password-reset | Reset a user&#39;s password
[**register_user_using_post**](UsersApi.md#register_user_using_post) | **POST** /users | Register a new user
[**remove_tag_using_delete1**](UsersApi.md#remove_tag_using_delete1) | **DELETE** /users/{user_id}/tags/{tag} | Remove a tag from a user
[**set_password_using_put**](UsersApi.md#set_password_using_put) | **PUT** /users/{id}/password | Set a user&#39;s password
[**update_user_template_using_put**](UsersApi.md#update_user_template_using_put) | **PUT** /users/templates/{id} | Update a user template
[**update_user_using_put**](UsersApi.md#update_user_using_put) | **PUT** /users/{id} | Update a user&#39;s info


# **add_tag_using_post1**
> add_tag_using_post1(user_id, tag)

Add a tag to a user

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 56 # int | The id of the user
tag = 'tag_example' # str | tag

try: 
    # Add a tag to a user
    api_instance.add_tag_using_post1(user_id, tag)
except ApiException as e:
    print("Exception when calling UsersApi->add_tag_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **tag** | **str**| tag | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_template_using_post**
> TemplateResource create_user_template_using_post(user_template_resource=user_template_resource)

Create a user template

User Templates define a type of user and the properties they have

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_template_resource = swagger_client.TemplateResource() # TemplateResource | The user template resource object (optional)

try: 
    # Create a user template
    api_response = api_instance.create_user_template_using_post(user_template_resource=user_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user_template_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_template_resource** | [**TemplateResource**](TemplateResource.md)| The user template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_template_using_delete**
> delete_user_template_using_delete(id, cascade=cascade)

Delete a user template

If cascade = 'detach', it will force delete the template even if it's attached to other objects

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a user template
    api_instance.delete_user_template_using_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_template_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| The value needed to delete used templates | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_password_reset_using_put**
> do_password_reset_using_put(id, new_password_request=new_password_request)

Choose a new password after a reset

Finish resetting a user's password using the secret provided from the password-reset endpoint.  Password should be in plain text and will be encrypted on receipt. Use SSL for security.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 56 # int | The id of the user
new_password_request = swagger_client.NewPasswordRequest() # NewPasswordRequest | The new password request object (optional)

try: 
    # Choose a new password after a reset
    api_instance.do_password_reset_using_put(id, new_password_request=new_password_request)
except ApiException as e:
    print("Exception when calling UsersApi->do_password_reset_using_put: %s\n" % e)
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

# **get_tags_using_get3**
> list[str] get_tags_using_get3(user_id)

List tags for a user

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 56 # int | The id of the user

try: 
    # List tags for a user
    api_response = api_instance.get_tags_using_get3(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_tags_using_get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 

### Return type

**list[str]**

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_template_using_get**
> TemplateResource get_user_template_using_get(id)

Get a single user template

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single user template
    api_response = api_instance.get_user_template_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_template_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_templates_using_get**
> PageResourceTemplateResource get_user_templates_using_get(size=size, page=page, order=order)

List and search user templates

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search user templates
    api_response = api_instance.get_user_templates_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_templates_using_get: %s\n" % e)
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

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_using_get**
> UserResource get_user_using_get(id)

Get a single user

Additional private info is included as USERS_ADMIN

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | The id of the user or 'me'

try: 
    # Get a single user
    api_response = api_instance.get_user_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the user or &#39;me&#39; | 

### Return type

[**UserResource**](UserResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_using_get**
> PageResourceUserBaseResource get_users_using_get(filter_displayname=filter_displayname, filter_email=filter_email, filter_firstname=filter_firstname, filter_fullname=filter_fullname, filter_lastname=filter_lastname, filter_username=filter_username, filter_tag=filter_tag, filter_group=filter_group, size=size, page=page, order=order)

List and search users

Additional private info is included as USERS_ADMIN

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
filter_displayname = 'filter_displayname_example' # str | Filter for users whose display name starts with provided string. (optional)
filter_email = 'filter_email_example' # str | Filter for users whose email starts with provided string. Requires USERS_ADMIN permission (optional)
filter_firstname = 'filter_firstname_example' # str | Filter for users whose first name starts with provided string. Requires USERS_ADMIN permission (optional)
filter_fullname = 'filter_fullname_example' # str | Filter for users whose full name starts with provided string. Requires USERS_ADMIN permission (optional)
filter_lastname = 'filter_lastname_example' # str | Filter for users whose last name starts with provided string. Requires USERS_ADMIN permission (optional)
filter_username = 'filter_username_example' # str | Filter for users whose username starts with the provided string. Requires USERS_ADMIN permission (optional)
filter_tag = 'filter_tag_example' # str | Filter for users who have a given tag (optional)
filter_group = 'filter_group_example' # str | Filter for users in a given group, by unique name (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search users
    api_response = api_instance.get_users_using_get(filter_displayname=filter_displayname, filter_email=filter_email, filter_firstname=filter_firstname, filter_fullname=filter_fullname, filter_lastname=filter_lastname, filter_username=filter_username, filter_tag=filter_tag, filter_group=filter_group, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users_using_get: %s\n" % e)
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
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceUserBaseResource**](PageResourceUserBaseResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiate_password_reset_using_post**
> initiate_password_reset_using_post(id)

Reset a user's password

A reset code will be generated and a 'forgot_password' BRE event will be fired with that code; this can be routed to the user as needed and submitted to the 'choose a new password' endpoint.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 56 # int | The id of the user

try: 
    # Reset a user's password
    api_instance.initiate_password_reset_using_post(id)
except ApiException as e:
    print("Exception when calling UsersApi->initiate_password_reset_using_post: %s\n" % e)
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

# **register_user_using_post**
> UserResource register_user_using_post(user_resource=user_resource)

Register a new user

Password should be in plain text and will be encrypted on receipt. Use SSL for security

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_resource = swagger_client.UserResource() # UserResource | The user resource object (optional)

try: 
    # Register a new user
    api_response = api_instance.register_user_using_post(user_resource=user_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->register_user_using_post: %s\n" % e)
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

# **remove_tag_using_delete1**
> remove_tag_using_delete1(user_id, tag)

Remove a tag from a user

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 56 # int | The id of the user
tag = 'tag_example' # str | The tag to remove

try: 
    # Remove a tag from a user
    api_instance.remove_tag_using_delete1(user_id, tag)
except ApiException as e:
    print("Exception when calling UsersApi->remove_tag_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **tag** | **str**| The tag to remove | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_password_using_put**
> set_password_using_put(id, password=password)

Set a user's password

Password should be in plain text and will be encrypted on receipt. Use SSL for security.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 56 # int | The id of the user
password = 'password_example' # str | The new plain text password (optional)

try: 
    # Set a user's password
    api_instance.set_password_using_put(id, password=password)
except ApiException as e:
    print("Exception when calling UsersApi->set_password_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the user | 
 **password** | **str**| The new plain text password | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_template_using_put**
> update_user_template_using_put(id, user_template_resource=user_template_resource)

Update a user template

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | The id of the template
user_template_resource = swagger_client.TemplateResource() # TemplateResource | The user template resource object (optional)

try: 
    # Update a user template
    api_instance.update_user_template_using_put(id, user_template_resource=user_template_resource)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_template_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **user_template_resource** | [**TemplateResource**](TemplateResource.md)| The user template resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_using_put**
> update_user_using_put(id, user_resource=user_resource)

Update a user's info

Password will not be edited on this endpoint, use password specific endpoints.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
id = 'id_example' # str | The id of the user or 'me'
user_resource = swagger_client.UserResource() # UserResource | The user resource object (optional)

try: 
    # Update a user's info
    api_instance.update_user_using_put(id, user_resource=user_resource)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the user or &#39;me&#39; | 
 **user_resource** | [**UserResource**](UserResource.md)| The user resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
