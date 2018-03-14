# knetik_cloud.GamificationLeaderboardsApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_leaderboard**](GamificationLeaderboardsApi.md#get_leaderboard) | **GET** /leaderboards/{context_type}/{context_id} | Retrieves leaderboard details and paginated entries
[**get_leaderboard_rank**](GamificationLeaderboardsApi.md#get_leaderboard_rank) | **GET** /leaderboards/{context_type}/{context_id}/users/{id}/rank | Retrieves a specific user entry with rank
[**get_leaderboard_strategies**](GamificationLeaderboardsApi.md#get_leaderboard_strategies) | **GET** /leaderboards/strategies | Get a list of available leaderboard strategy names


# **get_leaderboard**
> LeaderboardResource get_leaderboard(context_type, context_id, size=size, page=page, order=order)

Retrieves leaderboard details and paginated entries

The context type identifies the type of entity (i.e., 'activity') being tracked on the leaderboard. The context ID is the unique ID of the actual entity tracked by the leaderboard. Sorting is based on the fields of LeaderboardEntryResource rather than the returned LeaderboardResource. <br><br><b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.GamificationLeaderboardsApi(knetik_cloud.ApiClient(configuration))
context_type = 'context_type_example' # str | The context type for the leaderboard
context_id = 'context_id_example' # str | The context id for the leaderboard
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'score:DESC,updated:ASC,user_id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to score:DESC,updated:ASC,user_id:ASC)

try: 
    # Retrieves leaderboard details and paginated entries
    api_response = api_instance.get_leaderboard(context_type, context_id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLeaderboardsApi->get_leaderboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_type** | **str**| The context type for the leaderboard | 
 **context_id** | **str**| The context id for the leaderboard | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to score:DESC,updated:ASC,user_id:ASC]

### Return type

[**LeaderboardResource**](LeaderboardResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaderboard_rank**
> LeaderboardEntryResource get_leaderboard_rank(context_type, context_id, id)

Retrieves a specific user entry with rank

The context type identifies the type of entity (i.e., 'activity') being tracked on the leaderboard. The context ID is the unique ID of the actual entity tracked by the leaderboard. <br><br><b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.GamificationLeaderboardsApi(knetik_cloud.ApiClient(configuration))
context_type = 'context_type_example' # str | The context type for the leaderboard
context_id = 'context_id_example' # str | The context id for the leaderboard
id = 'id_example' # str | The id of a user

try: 
    # Retrieves a specific user entry with rank
    api_response = api_instance.get_leaderboard_rank(context_type, context_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLeaderboardsApi->get_leaderboard_rank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_type** | **str**| The context type for the leaderboard | 
 **context_id** | **str**| The context id for the leaderboard | 
 **id** | **str**| The id of a user | 

### Return type

[**LeaderboardEntryResource**](LeaderboardEntryResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaderboard_strategies**
> list[str] get_leaderboard_strategies()

Get a list of available leaderboard strategy names

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
api_instance = knetik_cloud.GamificationLeaderboardsApi(knetik_cloud.ApiClient(configuration))

try: 
    # Get a list of available leaderboard strategy names
    api_response = api_instance.get_leaderboard_strategies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLeaderboardsApi->get_leaderboard_strategies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

