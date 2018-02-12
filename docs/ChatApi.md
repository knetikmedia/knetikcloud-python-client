# knetik_cloud.ChatApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_chat_message**](ChatApi.md#acknowledge_chat_message) | **PUT** /chat/threads/{id}/acknowledge | Acknowledge number of messages in a thread
[**add_chat_message_blacklist**](ChatApi.md#add_chat_message_blacklist) | **POST** /chat/users/{id}/blacklist/{blacklisted_user_id} | Add a user to a chat message blacklist
[**delete_chat_message**](ChatApi.md#delete_chat_message) | **DELETE** /chat/messages/{id} | Delete a message
[**edit_chat_message**](ChatApi.md#edit_chat_message) | **PUT** /chat/messages/{id} | Edit your message
[**get_chat_message**](ChatApi.md#get_chat_message) | **GET** /chat/messages/{id} | Get a message
[**get_chat_message_blacklist**](ChatApi.md#get_chat_message_blacklist) | **GET** /chat/users/{id}/blacklist | Get a list of blocked users for chat messaging
[**get_chat_threads**](ChatApi.md#get_chat_threads) | **GET** /chat/threads | List your threads
[**get_direct_messages**](ChatApi.md#get_direct_messages) | **GET** /chat/users/{id}/messages | List messages with a user
[**get_thread_messages**](ChatApi.md#get_thread_messages) | **GET** /chat/threads/{id}/messages | List messages in a thread
[**get_topic_messages**](ChatApi.md#get_topic_messages) | **GET** /chat/topics/{id}/messages | List messages in a topic
[**remove_chat_blacklist**](ChatApi.md#remove_chat_blacklist) | **DELETE** /chat/users/{id}/blacklist/{blacklisted_user_id} | Remove a user from a blacklist
[**send_message**](ChatApi.md#send_message) | **POST** /chat/messages | Send a message


# **acknowledge_chat_message**
> acknowledge_chat_message(id, read_count=read_count)

Acknowledge number of messages in a thread

<b>Permissions Needed:</b> owner

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
api_instance = knetik_cloud.ChatApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The thread id
read_count = 56 # int | The amount of messages read (optional)

try: 
    # Acknowledge number of messages in a thread
    api_instance.acknowledge_chat_message(id, read_count=read_count)
except ApiException as e:
    print("Exception when calling ChatApi->acknowledge_chat_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The thread id | 
 **read_count** | **int**| The amount of messages read | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_chat_message_blacklist**
> add_chat_message_blacklist(blacklisted_user_id, id)

Add a user to a chat message blacklist

<b>Permissions Needed:</b> CHAT_ADMIN or owner

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
api_instance = knetik_cloud.ChatApi(knetik_cloud.ApiClient(configuration))
blacklisted_user_id = 56 # int | The user id to blacklist
id = 'id_example' # str | The user id or 'me'

try: 
    # Add a user to a chat message blacklist
    api_instance.add_chat_message_blacklist(blacklisted_user_id, id)
except ApiException as e:
    print("Exception when calling ChatApi->add_chat_message_blacklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blacklisted_user_id** | **int**| The user id to blacklist | 
 **id** | **str**| The user id or &#39;me&#39; | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chat_message**
> delete_chat_message(id)

Delete a message

<b>Permissions Needed:</b> CHAT_ADMIN or owner

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
api_instance = knetik_cloud.ChatApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The message id

try: 
    # Delete a message
    api_instance.delete_chat_message(id)
except ApiException as e:
    print("Exception when calling ChatApi->delete_chat_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The message id | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_chat_message**
> edit_chat_message(id, chat_message_resource=chat_message_resource)

Edit your message

<b>Permissions Needed:</b> owner

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
api_instance = knetik_cloud.ChatApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The message id
chat_message_resource = knetik_cloud.ChatMessageResource() # ChatMessageResource | The chat message resource (optional)

try: 
    # Edit your message
    api_instance.edit_chat_message(id, chat_message_resource=chat_message_resource)
except ApiException as e:
    print("Exception when calling ChatApi->edit_chat_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The message id | 
 **chat_message_resource** | [**ChatMessageResource**](ChatMessageResource.md)| The chat message resource | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_message**
> ChatMessageResource get_chat_message(id)

Get a message

<b>Permissions Needed:</b> CHAT_ADMIN or owner

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
api_instance = knetik_cloud.ChatApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The message id

try: 
    # Get a message
    api_response = api_instance.get_chat_message(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chat_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The message id | 

### Return type

[**ChatMessageResource**](ChatMessageResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_message_blacklist**
> list[ChatBlacklistResource] get_chat_message_blacklist(id)

Get a list of blocked users for chat messaging

<b>Permissions Needed:</b> CHAT_ADMIN or owner

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
api_instance = knetik_cloud.ChatApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The user id or 'me'

try: 
    # Get a list of blocked users for chat messaging
    api_response = api_instance.get_chat_message_blacklist(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chat_message_blacklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The user id or &#39;me&#39; | 

### Return type

[**list[ChatBlacklistResource]**](ChatBlacklistResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_threads**
> PageResourceChatUserThreadResource get_chat_threads(size=size, page=page, order=order)

List your threads

<b>Permissions Needed:</b> owner

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
api_instance = knetik_cloud.ChatApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned (optional) (default to 1)
order = 'order_example' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional)

try: 
    # List your threads
    api_response = api_instance.get_chat_threads(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_chat_threads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] 

### Return type

[**PageResourceChatUserThreadResource**](PageResourceChatUserThreadResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_direct_messages**
> PageResourceChatMessageResource get_direct_messages(id, size=size, page=page, order=order)

List messages with a user

<b>Permissions Needed:</b> owner

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
api_instance = knetik_cloud.ChatApi(knetik_cloud.ApiClient(configuration))
id = 56 # int | The user id
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned (optional) (default to 1)
order = 'order_example' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional)

try: 
    # List messages with a user
    api_response = api_instance.get_direct_messages(id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_direct_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The user id | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] 

### Return type

[**PageResourceChatMessageResource**](PageResourceChatMessageResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_thread_messages**
> PageResourceChatMessageResource get_thread_messages(id, size=size, page=page, order=order)

List messages in a thread

<b>Permissions Needed:</b> CHAT_ADMIN or owner

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
api_instance = knetik_cloud.ChatApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The thread id
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned (optional) (default to 1)
order = 'order_example' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional)

try: 
    # List messages in a thread
    api_response = api_instance.get_thread_messages(id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_thread_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The thread id | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] 

### Return type

[**PageResourceChatMessageResource**](PageResourceChatMessageResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_messages**
> PageResourceChatMessageResource get_topic_messages(id, size=size, page=page, order=order)

List messages in a topic

<b>Permissions Needed:</b> CHAT_ADMIN or owner

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
api_instance = knetik_cloud.ChatApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The topic id
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned (optional) (default to 1)
order = 'order_example' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional)

try: 
    # List messages in a topic
    api_response = api_instance.get_topic_messages(id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_topic_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The topic id | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] 

### Return type

[**PageResourceChatMessageResource**](PageResourceChatMessageResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_chat_blacklist**
> remove_chat_blacklist(blacklisted_user_id, id)

Remove a user from a blacklist

<b>Permissions Needed:</b> CHAT_ADMIN or owner

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
api_instance = knetik_cloud.ChatApi(knetik_cloud.ApiClient(configuration))
blacklisted_user_id = 56 # int | The user id to blacklist
id = 'id_example' # str | The user id or 'me'

try: 
    # Remove a user from a blacklist
    api_instance.remove_chat_blacklist(blacklisted_user_id, id)
except ApiException as e:
    print("Exception when calling ChatApi->remove_chat_blacklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blacklisted_user_id** | **int**| The user id to blacklist | 
 **id** | **str**| The user id or &#39;me&#39; | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message**
> ChatMessageResource send_message(chat_message_resource=chat_message_resource)

Send a message

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
api_instance = knetik_cloud.ChatApi(knetik_cloud.ApiClient(configuration))
chat_message_resource = knetik_cloud.ChatMessageResource() # ChatMessageResource | The chat message resource (optional)

try: 
    # Send a message
    api_response = api_instance.send_message(chat_message_resource=chat_message_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->send_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat_message_resource** | [**ChatMessageResource**](ChatMessageResource.md)| The chat message resource | [optional] 

### Return type

[**ChatMessageResource**](ChatMessageResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

