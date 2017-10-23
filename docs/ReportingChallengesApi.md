# knetik_cloud.ReportingChallengesApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_challenge_event_leaderboard**](ReportingChallengesApi.md#get_challenge_event_leaderboard) | **GET** /reporting/events/leaderboard | Retrieve a challenge event leaderboard details
[**get_challenge_event_participants**](ReportingChallengesApi.md#get_challenge_event_participants) | **GET** /reporting/events/participants | Retrieve a challenge event participant details


# **get_challenge_event_leaderboard**
> PageResourceChallengeEventParticipantResource get_challenge_event_leaderboard(filter_event=filter_event, size=size, page=page, order=order)

Retrieve a challenge event leaderboard details

Lists all leaderboard entries with additional user details

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
api_instance = knetik_cloud.ReportingChallengesApi(knetik_cloud.ApiClient(configuration))
filter_event = 789 # int | A sepecific challenge event id (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned (optional) (default to 1)
order = 'order_example' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional)

try: 
    # Retrieve a challenge event leaderboard details
    api_response = api_instance.get_challenge_event_leaderboard(filter_event=filter_event, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingChallengesApi->get_challenge_event_leaderboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_event** | **int**| A sepecific challenge event id | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] 

### Return type

[**PageResourceChallengeEventParticipantResource**](PageResourceChallengeEventParticipantResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_challenge_event_participants**
> PageResourceChallengeEventParticipantResource get_challenge_event_participants(filter_event=filter_event, size=size, page=page, order=order)

Retrieve a challenge event participant details

Lists all user submitted scores sorted by value, including those that do not apear in the leaderboard due to value or aggregation

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
api_instance = knetik_cloud.ReportingChallengesApi(knetik_cloud.ApiClient(configuration))
filter_event = 789 # int | A sepecific challenge event id (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned (optional) (default to 1)
order = 'order_example' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional)

try: 
    # Retrieve a challenge event participant details
    api_response = api_instance.get_challenge_event_participants(filter_event=filter_event, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingChallengesApi->get_challenge_event_participants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_event** | **int**| A sepecific challenge event id | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] 

### Return type

[**PageResourceChallengeEventParticipantResource**](PageResourceChallengeEventParticipantResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

