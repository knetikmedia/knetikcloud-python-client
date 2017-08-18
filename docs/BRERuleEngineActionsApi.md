# knetik_cloud.BRERuleEngineActionsApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bre_actions**](BRERuleEngineActionsApi.md#get_bre_actions) | **GET** /bre/actions | Get a list of available actions


# **get_bre_actions**
> list[ActionResource] get_bre_actions(filter_category=filter_category, filter_name=filter_name, filter_tags=filter_tags, filter_search=filter_search)

Get a list of available actions

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
api_instance = knetik_cloud.BRERuleEngineActionsApi(knetik_cloud.ApiClient(configuration))
filter_category = 'filter_category_example' # str | Filter for actions that are within a specific category (optional)
filter_name = 'filter_name_example' # str | Filter for actions that have names containing the given string (optional)
filter_tags = 'filter_tags_example' # str | Filter for actions that have all of the given tags (comma separated list) (optional)
filter_search = 'filter_search_example' # str | Filter for actions containing the given words somewhere within name, description and tags (optional)

try: 
    # Get a list of available actions
    api_response = api_instance.get_bre_actions(filter_category=filter_category, filter_name=filter_name, filter_tags=filter_tags, filter_search=filter_search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineActionsApi->get_bre_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_category** | **str**| Filter for actions that are within a specific category | [optional] 
 **filter_name** | **str**| Filter for actions that have names containing the given string | [optional] 
 **filter_tags** | **str**| Filter for actions that have all of the given tags (comma separated list) | [optional] 
 **filter_search** | **str**| Filter for actions containing the given words somewhere within name, description and tags | [optional] 

### Return type

[**list[ActionResource]**](ActionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

