# knetik_cloud.AuthTokensApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tokens**](AuthTokensApi.md#delete_tokens) | **DELETE** /auth/tokens | Delete tokens by username, client id, or both
[**get_token**](AuthTokensApi.md#get_token) | **GET** /auth/tokens/{username}/{client_id} | Get a single token by username and client id
[**get_tokens**](AuthTokensApi.md#get_tokens) | **GET** /auth/tokens | List usernames and client ids


# **delete_tokens**
> delete_tokens(username=username, client_id=client_id)

Delete tokens by username, client id, or both

<b>Permissions Needed:</b> TOKENS_ADMIN

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
api_instance = knetik_cloud.AuthTokensApi(knetik_cloud.ApiClient(configuration))
username = 'username_example' # str | The username of the user (optional)
client_id = 'client_id_example' # str | The id of the client (optional)

try: 
    # Delete tokens by username, client id, or both
    api_instance.delete_tokens(username=username, client_id=client_id)
except ApiException as e:
    print("Exception when calling AuthTokensApi->delete_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user | [optional] 
 **client_id** | **str**| The id of the client | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> OauthAccessTokenResource get_token(username, client_id)

Get a single token by username and client id

<b>Permissions Needed:</b> TOKENS_ADMIN

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
api_instance = knetik_cloud.AuthTokensApi(knetik_cloud.ApiClient(configuration))
username = 'username_example' # str | The username of the user
client_id = 'client_id_example' # str | The id of the client

try: 
    # Get a single token by username and client id
    api_response = api_instance.get_token(username, client_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthTokensApi->get_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username of the user | 
 **client_id** | **str**| The id of the client | 

### Return type

[**OauthAccessTokenResource**](OauthAccessTokenResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens**
> PageResourceOauthAccessTokenResource get_tokens(filter_client_id=filter_client_id, filter_username=filter_username, size=size, page=page, order=order)

List usernames and client ids

Token value not shown. <br><br><b>Permissions Needed:</b> TOKENS_ADMIN

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
api_instance = knetik_cloud.AuthTokensApi(knetik_cloud.ApiClient(configuration))
filter_client_id = 'filter_client_id_example' # str | Filters for token whose client id matches provided string (optional)
filter_username = 'filter_username_example' # str | Filters for token whose username matches provided string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'order_example' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional)

try: 
    # List usernames and client ids
    api_response = api_instance.get_tokens(filter_client_id=filter_client_id, filter_username=filter_username, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthTokensApi->get_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_client_id** | **str**| Filters for token whose client id matches provided string | [optional] 
 **filter_username** | **str**| Filters for token whose username matches provided string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] 

### Return type

[**PageResourceOauthAccessTokenResource**](PageResourceOauthAccessTokenResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

