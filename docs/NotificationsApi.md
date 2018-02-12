# knetik_cloud.NotificationsApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_type**](NotificationsApi.md#create_notification_type) | **POST** /notifications/types | Create a notification type
[**delete_notification_type**](NotificationsApi.md#delete_notification_type) | **DELETE** /notifications/types/{id} | Delete a notification type
[**get_notification_type**](NotificationsApi.md#get_notification_type) | **GET** /notifications/types/{id} | Get a single notification type
[**get_notification_types**](NotificationsApi.md#get_notification_types) | **GET** /notifications/types | List and search notification types
[**get_user_notification_info**](NotificationsApi.md#get_user_notification_info) | **GET** /users/{user_id}/notifications/types/{type_id} | View a user&#39;s notification settings for a type
[**get_user_notification_info_list**](NotificationsApi.md#get_user_notification_info_list) | **GET** /users/{user_id}/notifications/types | View a user&#39;s notification settings
[**get_user_notifications**](NotificationsApi.md#get_user_notifications) | **GET** /users/{id}/notifications | Get notifications
[**send_notification**](NotificationsApi.md#send_notification) | **POST** /notifications | Send a notification
[**set_user_notification_status**](NotificationsApi.md#set_user_notification_status) | **PUT** /users/{user_id}/notifications/{notification_id}/status | Set notification status
[**silence_direct_notifications**](NotificationsApi.md#silence_direct_notifications) | **PUT** /users/{user_id}/notifications/types/{type_id}/silenced | Enable or disable direct notifications for a user
[**update_notification_type**](NotificationsApi.md#update_notification_type) | **PUT** /notifications/types/{id} | Update a notificationType


# **create_notification_type**
> NotificationTypeResource create_notification_type(notification_type=notification_type)

Create a notification type

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
api_instance = knetik_cloud.NotificationsApi(knetik_cloud.ApiClient(configuration))
notification_type = knetik_cloud.NotificationTypeResource() # NotificationTypeResource | notificationType (optional)

try: 
    # Create a notification type
    api_response = api_instance.create_notification_type(notification_type=notification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->create_notification_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_type** | [**NotificationTypeResource**](NotificationTypeResource.md)| notificationType | [optional] 

### Return type

[**NotificationTypeResource**](NotificationTypeResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_type**
> delete_notification_type(id)

Delete a notification type

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
api_instance = knetik_cloud.NotificationsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | id

try: 
    # Delete a notification type
    api_instance.delete_notification_type(id)
except ApiException as e:
    print("Exception when calling NotificationsApi->delete_notification_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_type**
> NotificationTypeResource get_notification_type(id)

Get a single notification type

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
api_instance = knetik_cloud.NotificationsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | id

try: 
    # Get a single notification type
    api_response = api_instance.get_notification_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_notification_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 

### Return type

[**NotificationTypeResource**](NotificationTypeResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_types**
> PageResourceNotificationTypeResource get_notification_types(size=size, page=page, order=order)

List and search notification types

Get a list of notification type with optional filtering

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
api_instance = knetik_cloud.NotificationsApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search notification types
    api_response = api_instance.get_notification_types(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_notification_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceNotificationTypeResource**](PageResourceNotificationTypeResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_notification_info**
> NotificationUserTypeResource get_user_notification_info(type_id, user_id)

View a user's notification settings for a type

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
api_instance = knetik_cloud.NotificationsApi(knetik_cloud.ApiClient(configuration))
type_id = 'type_id_example' # str | The id of the topic
user_id = 'user_id_example' # str | The id of the subscriber or 'me'

try: 
    # View a user's notification settings for a type
    api_response = api_instance.get_user_notification_info(type_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_user_notification_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**| The id of the topic | 
 **user_id** | **str**| The id of the subscriber or &#39;me&#39; | 

### Return type

[**NotificationUserTypeResource**](NotificationUserTypeResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_notification_info_list**
> PageResourceNotificationUserTypeResource get_user_notification_info_list(user_id, size=size, page=page, order=order)

View a user's notification settings

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
api_instance = knetik_cloud.NotificationsApi(knetik_cloud.ApiClient(configuration))
user_id = 'user_id_example' # str | The id of the subscriber or 'me'
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # View a user's notification settings
    api_response = api_instance.get_user_notification_info_list(user_id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_user_notification_info_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the subscriber or &#39;me&#39; | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceNotificationUserTypeResource**](PageResourceNotificationUserTypeResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_notifications**
> PageResourceUserNotificationResource get_user_notifications(id, filter_status=filter_status, size=size, page=page, order=order)

Get notifications

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
api_instance = knetik_cloud.NotificationsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the user or 'me'
filter_status = 'filter_status_example' # str | filter for notifications with a given status (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Get notifications
    api_response = api_instance.get_user_notifications(id, filter_status=filter_status, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_user_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the user or &#39;me&#39; | 
 **filter_status** | **str**| filter for notifications with a given status | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceUserNotificationResource**](PageResourceUserNotificationResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_notification**
> NotificationResource send_notification(notification=notification)

Send a notification

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
api_instance = knetik_cloud.NotificationsApi(knetik_cloud.ApiClient(configuration))
notification = knetik_cloud.NotificationResource() # NotificationResource | notification (optional)

try: 
    # Send a notification
    api_response = api_instance.send_notification(notification=notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->send_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification** | [**NotificationResource**](NotificationResource.md)| notification | [optional] 

### Return type

[**NotificationResource**](NotificationResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_notification_status**
> set_user_notification_status(user_id, notification_id, notification=notification)

Set notification status

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
api_instance = knetik_cloud.NotificationsApi(knetik_cloud.ApiClient(configuration))
user_id = 'user_id_example' # str | The id of the user or 'me'
notification_id = 'notification_id_example' # str | The id of the notification
notification = knetik_cloud.ValueWrapperstring() # ValueWrapperstring | status (optional)

try: 
    # Set notification status
    api_instance.set_user_notification_status(user_id, notification_id, notification=notification)
except ApiException as e:
    print("Exception when calling NotificationsApi->set_user_notification_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user or &#39;me&#39; | 
 **notification_id** | **str**| The id of the notification | 
 **notification** | [**ValueWrapperstring**](ValueWrapperstring.md)| status | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **silence_direct_notifications**
> silence_direct_notifications(type_id, user_id, silenced)

Enable or disable direct notifications for a user

Allows enabling or disabling messages for a given notification type when sent direct to the user. Notifications can still be retrieved by endpoint. For notifications broadcased to a topic, see the topic service to disable messages for the user there.

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
api_instance = knetik_cloud.NotificationsApi(knetik_cloud.ApiClient(configuration))
type_id = 'type_id_example' # str | The id of the topic
user_id = 'user_id_example' # str | The id of the subscriber or 'me'
silenced = knetik_cloud.ValueWrapperboolean() # ValueWrapperboolean | silenced

try: 
    # Enable or disable direct notifications for a user
    api_instance.silence_direct_notifications(type_id, user_id, silenced)
except ApiException as e:
    print("Exception when calling NotificationsApi->silence_direct_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**| The id of the topic | 
 **user_id** | **str**| The id of the subscriber or &#39;me&#39; | 
 **silenced** | [**ValueWrapperboolean**](ValueWrapperboolean.md)| silenced | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_type**
> NotificationTypeResource update_notification_type(id, notification_type=notification_type)

Update a notificationType

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
api_instance = knetik_cloud.NotificationsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | id
notification_type = knetik_cloud.NotificationTypeResource() # NotificationTypeResource | notificationType (optional)

try: 
    # Update a notificationType
    api_response = api_instance.update_notification_type(id, notification_type=notification_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->update_notification_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id | 
 **notification_type** | [**NotificationTypeResource**](NotificationTypeResource.md)| notificationType | [optional] 

### Return type

[**NotificationTypeResource**](NotificationTypeResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

