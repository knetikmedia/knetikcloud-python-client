# swagger_client.UsersFriendshipsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_friend_using_post**](UsersFriendshipsApi.md#add_friend_using_post) | **POST** /users/{user_id}/friends/{id} | Add a friend
[**connect_using_token_using_post**](UsersFriendshipsApi.md#connect_using_token_using_post) | **POST** /users/{user_id}/friends/tokens | Redeem friendship token
[**get_friends_using_get**](UsersFriendshipsApi.md#get_friends_using_get) | **GET** /users/{user_id}/friends | Get friends list
[**get_invite_token_using_get**](UsersFriendshipsApi.md#get_invite_token_using_get) | **GET** /users/{user_id}/invite-token | Returns the invite token
[**get_invites_using_get**](UsersFriendshipsApi.md#get_invites_using_get) | **GET** /users/{user_id}/invites | Get pending invites
[**remove_friend_using_delete**](UsersFriendshipsApi.md#remove_friend_using_delete) | **DELETE** /users/{user_id}/friends/{id} | Remove or decline a friend


# **add_friend_using_post**
> add_friend_using_post(user_id, id)

Add a friend

As a user, either creates or confirm a pending request. As an admin, call this endpoint twice while inverting the IDs to create a confirmed friendship.

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
api_instance = swagger_client.UsersFriendshipsApi()
user_id = 'user_id_example' # str | The id of the user or 'me' if logged in
id = 56 # int | The id of the user to befriend

try: 
    # Add a friend
    api_instance.add_friend_using_post(user_id, id)
except ApiException as e:
    print("Exception when calling UsersFriendshipsApi->add_friend_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user or &#39;me&#39; if logged in | 
 **id** | **int**| The id of the user to befriend | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_using_token_using_post**
> connect_using_token_using_post(user_id, token=token)

Redeem friendship token

Immediately connects the requested user with the user mapped by the provided invite token

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
api_instance = swagger_client.UsersFriendshipsApi()
user_id = 'user_id_example' # str | The id of the user or 'me' if logged in
token = 'token_example' # str | The invite token (optional)

try: 
    # Redeem friendship token
    api_instance.connect_using_token_using_post(user_id, token=token)
except ApiException as e:
    print("Exception when calling UsersFriendshipsApi->connect_using_token_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user or &#39;me&#39; if logged in | 
 **token** | **str**| The invite token | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_friends_using_get**
> PageSimpleUserResource get_friends_using_get(user_id, size=size, page=page, order=order)

Get friends list

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
api_instance = swagger_client.UsersFriendshipsApi()
user_id = 'user_id_example' # str | The id of the user or 'me'
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Get friends list
    api_response = api_instance.get_friends_using_get(user_id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersFriendshipsApi->get_friends_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user or &#39;me&#39; | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageSimpleUserResource**](PageSimpleUserResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invite_token_using_get**
> str get_invite_token_using_get(user_id)

Returns the invite token

This is a unique invite token that allows direct connection to the request user.  Exposing that token presents privacy issues if the token is leaked. Use friend request flow instead if confirmation is required

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
api_instance = swagger_client.UsersFriendshipsApi()
user_id = 'user_id_example' # str | The id of the user or 'me' if logged in

try: 
    # Returns the invite token
    api_response = api_instance.get_invite_token_using_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersFriendshipsApi->get_invite_token_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user or &#39;me&#39; if logged in | 

### Return type

**str**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invites_using_get**
> PageSimpleUserResource get_invites_using_get(user_id, size=size, page=page, order=order)

Get pending invites

Invites that the specified user received

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
api_instance = swagger_client.UsersFriendshipsApi()
user_id = 'user_id_example' # str | The id of the user or 'me'
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Get pending invites
    api_response = api_instance.get_invites_using_get(user_id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersFriendshipsApi->get_invites_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user or &#39;me&#39; | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageSimpleUserResource**](PageSimpleUserResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_friend_using_delete**
> remove_friend_using_delete(user_id, id)

Remove or decline a friend

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
api_instance = swagger_client.UsersFriendshipsApi()
user_id = 'user_id_example' # str | The id of the user or 'me' if logged in
id = 56 # int | The id of the user to befriend

try: 
    # Remove or decline a friend
    api_instance.remove_friend_using_delete(user_id, id)
except ApiException as e:
    print("Exception when calling UsersFriendshipsApi->remove_friend_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user or &#39;me&#39; if logged in | 
 **id** | **int**| The id of the user to befriend | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

