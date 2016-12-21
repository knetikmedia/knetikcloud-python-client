# swagger_client.AuthTokensApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_token_using_delete**](AuthTokensApi.md#delete_token_using_delete) | **DELETE** /auth/tokens/{username} | Delete all tokens by username
[**delete_token_with_client_id_using_delete**](AuthTokensApi.md#delete_token_with_client_id_using_delete) | **DELETE** /auth/tokens/{username}/{client_id} | Delete a token by username and client id
[**get_token_by_user_using_get**](AuthTokensApi.md#get_token_by_user_using_get) | **GET** /auth/tokens/{username}/{client_id} | Get a single token by username and client id
[**get_tokens_using_get**](AuthTokensApi.md#get_tokens_using_get) | **GET** /auth/tokens | List usernames and client ids


# **delete_token_using_delete**
> delete_token_using_delete(username)

Delete all tokens by username

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
api_instance = swagger_client.AuthTokensApi()
username = 'username_example' # str | The username of the user

try: 
    # Delete all tokens by username
    api_instance.delete_token_using_delete(username)
except ApiException as e:
    print("Exception when calling AuthTokensApi->delete_token_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token_with_client_id_using_delete**
> delete_token_with_client_id_using_delete(username, client_id)

Delete a token by username and client id

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
api_instance = swagger_client.AuthTokensApi()
username = 'username_example' # str | The username of the user
client_id = 'client_id_example' # str | The id of the client

try: 
    # Delete a token by username and client id
    api_instance.delete_token_with_client_id_using_delete(username, client_id)
except ApiException as e:
    print("Exception when calling AuthTokensApi->delete_token_with_client_id_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user | 
 **client_id** | **str**| The id of the client | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_by_user_using_get**
> OauthAccessTokenResource get_token_by_user_using_get(username, client_id)

Get a single token by username and client id

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
api_instance = swagger_client.AuthTokensApi()
username = 'username_example' # str | The username of the user
client_id = 'client_id_example' # str | The id of the client

try: 
    # Get a single token by username and client id
    api_response = api_instance.get_token_by_user_using_get(username, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthTokensApi->get_token_by_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user | 
 **client_id** | **str**| The id of the client | 

### Return type

[**OauthAccessTokenResource**](OauthAccessTokenResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_using_get**
> PageResourceOauthAccessTokenResource get_tokens_using_get(filter_client_id=filter_client_id, filter_username=filter_username, size=size, page=page, order=order)

List usernames and client ids

Token value not shown

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
api_instance = swagger_client.AuthTokensApi()
filter_client_id = 'filter_client_id_example' # str | Filters for token whose client id matches provided string (optional)
filter_username = 'filter_username_example' # str | Filters for token whose username matches provided string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'username:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to username:ASC)

try: 
    # List usernames and client ids
    api_response = api_instance.get_tokens_using_get(filter_client_id=filter_client_id, filter_username=filter_username, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthTokensApi->get_tokens_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_client_id** | **str**| Filters for token whose client id matches provided string | [optional] 
 **filter_username** | **str**| Filters for token whose username matches provided string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to username:ASC]

### Return type

[**PageResourceOauthAccessTokenResource**](PageResourceOauthAccessTokenResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

