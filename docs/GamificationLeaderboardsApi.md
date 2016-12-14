# swagger_client.GamificationLeaderboardsApi

All URIs are relative to *https://devsandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_leaderboard_using_get**](GamificationLeaderboardsApi.md#get_leaderboard_using_get) | **GET** /leaderboards/{context_type}/{context_id} | Retrieves leaderboard details and paginated entries
[**get_strategies_using_get**](GamificationLeaderboardsApi.md#get_strategies_using_get) | **GET** /leaderboards/strategies | Get a list of available leaderboard strategy names
[**get_user_rank_using_get**](GamificationLeaderboardsApi.md#get_user_rank_using_get) | **GET** /leaderboards/{context_type}/{context_id}/users/{id}/rank | Retrieves a specific user entry with rank


# **get_leaderboard_using_get**
> LeaderboardResource get_leaderboard_using_get(context_type, context_id, size=size, page=page)

Retrieves leaderboard details and paginated entries

The context type identifies the type of entity (i.e., 'activity') being tracked on the leaderboard. The context ID is the unique ID of the actual entity tracked by the leaderboard.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GamificationLeaderboardsApi()
context_type = 'context_type_example' # str | The context type for the leaderboard
context_id = 'context_id_example' # str | The context id for the leaderboard
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Retrieves leaderboard details and paginated entries
    api_response = api_instance.get_leaderboard_using_get(context_type, context_id, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLeaderboardsApi->get_leaderboard_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_type** | **str**| The context type for the leaderboard | 
 **context_id** | **str**| The context id for the leaderboard | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**LeaderboardResource**](LeaderboardResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_strategies_using_get**
> list[str] get_strategies_using_get()

Get a list of available leaderboard strategy names

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GamificationLeaderboardsApi()

try: 
    # Get a list of available leaderboard strategy names
    api_response = api_instance.get_strategies_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLeaderboardsApi->get_strategies_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_rank_using_get**
> LeaderboardEntryResource get_user_rank_using_get(context_type, context_id, id)

Retrieves a specific user entry with rank

The context type identifies the type of entity (i.e., 'activity') being tracked on the leaderboard. The context ID is the unique ID of the actual entity tracked by the leaderboard.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GamificationLeaderboardsApi()
context_type = 'context_type_example' # str | The context type for the leaderboard
context_id = 'context_id_example' # str | The context id for the leaderboard
id = 'id_example' # str | The id of a user

try: 
    # Retrieves a specific user entry with rank
    api_response = api_instance.get_user_rank_using_get(context_type, context_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLeaderboardsApi->get_user_rank_using_get: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

