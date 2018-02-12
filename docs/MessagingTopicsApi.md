# knetik_cloud.MessagingTopicsApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_topic_subscriber**](MessagingTopicsApi.md#disable_topic_subscriber) | **PUT** /messaging/topics/{id}/subscribers/{user_id}/disabled | Enable or disable messages for a user
[**get_topic_subscriber**](MessagingTopicsApi.md#get_topic_subscriber) | **GET** /messaging/topics/{id}/subscribers/{user_id} | Get a subscriber to a topic
[**get_topic_subscribers**](MessagingTopicsApi.md#get_topic_subscribers) | **GET** /messaging/topics/{id}/subscribers | Get all subscribers to a topic
[**get_user_topics**](MessagingTopicsApi.md#get_user_topics) | **GET** /users/{id}/topics | Get all messaging topics for a given user


# **disable_topic_subscriber**
> disable_topic_subscriber(id, user_id, disabled)

Enable or disable messages for a user

Useful for opt-out options on a single topic. Consider multiple topics for multiple opt-out options.

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
api_instance = knetik_cloud.MessagingTopicsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the topic
user_id = 'user_id_example' # str | The id of the subscriber or 'me'
disabled = knetik_cloud.ValueWrapperboolean() # ValueWrapperboolean | disabled

try: 
    # Enable or disable messages for a user
    api_instance.disable_topic_subscriber(id, user_id, disabled)
except ApiException as e:
    print("Exception when calling MessagingTopicsApi->disable_topic_subscriber: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the topic | 
 **user_id** | **str**| The id of the subscriber or &#39;me&#39; | 
 **disabled** | [**ValueWrapperboolean**](ValueWrapperboolean.md)| disabled | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_subscriber**
> TopicSubscriberResource get_topic_subscriber(id, user_id)

Get a subscriber to a topic

<b>Permissions Needed:</b> TOPICS_ADMIN

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
api_instance = knetik_cloud.MessagingTopicsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the topic
user_id = 'user_id_example' # str | The id of the subscriber or 'me'

try: 
    # Get a subscriber to a topic
    api_response = api_instance.get_topic_subscriber(id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingTopicsApi->get_topic_subscriber: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the topic | 
 **user_id** | **str**| The id of the subscriber or &#39;me&#39; | 

### Return type

[**TopicSubscriberResource**](TopicSubscriberResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topic_subscribers**
> PageResourceTopicSubscriberResource get_topic_subscribers(id)

Get all subscribers to a topic

<b>Permissions Needed:</b> TOPICS_ADMIN

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
api_instance = knetik_cloud.MessagingTopicsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the topic

try: 
    # Get all subscribers to a topic
    api_response = api_instance.get_topic_subscribers(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingTopicsApi->get_topic_subscribers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the topic | 

### Return type

[**PageResourceTopicSubscriberResource**](PageResourceTopicSubscriberResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_topics**
> PageResourceTopicResource get_user_topics(id)

Get all messaging topics for a given user

<b>Permissions Needed:</b> TOPICS_ADMIN

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
api_instance = knetik_cloud.MessagingTopicsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the user or 'me'

try: 
    # Get all messaging topics for a given user
    api_response = api_instance.get_user_topics(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagingTopicsApi->get_user_topics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the user or &#39;me&#39; | 

### Return type

[**PageResourceTopicResource**](PageResourceTopicResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

