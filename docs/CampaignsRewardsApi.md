# swagger_client.CampaignsRewardsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reward_set**](CampaignsRewardsApi.md#create_reward_set) | **POST** /rewards | Create a reward set
[**delete_reward_set**](CampaignsRewardsApi.md#delete_reward_set) | **DELETE** /rewards/{id} | Delete a reward set
[**get_reward_set**](CampaignsRewardsApi.md#get_reward_set) | **GET** /rewards/{id} | Get a single reward set
[**get_reward_sets**](CampaignsRewardsApi.md#get_reward_sets) | **GET** /rewards | List and search reward sets
[**update_reward_set**](CampaignsRewardsApi.md#update_reward_set) | **PUT** /rewards/{id} | Update a reward set


# **create_reward_set**
> RewardSetResource create_reward_set(reward_set_resource=reward_set_resource)

Create a reward set

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
api_instance = swagger_client.CampaignsRewardsApi()
reward_set_resource = swagger_client.RewardSetResource() # RewardSetResource | The reward set resource object (optional)

try: 
    # Create a reward set
    api_response = api_instance.create_reward_set(reward_set_resource=reward_set_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsRewardsApi->create_reward_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_set_resource** | [**RewardSetResource**](RewardSetResource.md)| The reward set resource object | [optional] 

### Return type

[**RewardSetResource**](RewardSetResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reward_set**
> delete_reward_set(id)

Delete a reward set

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
api_instance = swagger_client.CampaignsRewardsApi()
id = 56 # int | The reward id

try: 
    # Delete a reward set
    api_instance.delete_reward_set(id)
except ApiException as e:
    print("Exception when calling CampaignsRewardsApi->delete_reward_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The reward id | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reward_set**
> RewardSetResource get_reward_set(id)

Get a single reward set

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignsRewardsApi()
id = 56 # int | The reward id

try: 
    # Get a single reward set
    api_response = api_instance.get_reward_set(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsRewardsApi->get_reward_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The reward id | 

### Return type

[**RewardSetResource**](RewardSetResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reward_sets**
> PageResourceRewardSetResource get_reward_sets(size=size, page=page, order=order)

List and search reward sets

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignsRewardsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search reward sets
    api_response = api_instance.get_reward_sets(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsRewardsApi->get_reward_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceRewardSetResource**](PageResourceRewardSetResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reward_set**
> update_reward_set(id, reward_set_resource=reward_set_resource)

Update a reward set

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
api_instance = swagger_client.CampaignsRewardsApi()
id = 56 # int | The reward id
reward_set_resource = swagger_client.RewardSetResource() # RewardSetResource | The reward set resource object (optional)

try: 
    # Update a reward set
    api_instance.update_reward_set(id, reward_set_resource=reward_set_resource)
except ApiException as e:
    print("Exception when calling CampaignsRewardsApi->update_reward_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The reward id | 
 **reward_set_resource** | [**RewardSetResource**](RewardSetResource.md)| The reward set resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

