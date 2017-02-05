# swagger_client.BRERuleEngineActionsApi

All URIs are relative to *https://integration.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_actions_using_get**](BRERuleEngineActionsApi.md#get_actions_using_get) | **GET** /bre/actions | Get a list of available actions


# **get_actions_using_get**
> list[ActionResource] get_actions_using_get(filter_category=filter_category, filter_name=filter_name)

Get a list of available actions

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
api_instance = swagger_client.BRERuleEngineActionsApi()
filter_category = 'filter_category_example' # str | Filter for actions that are within a specific category (optional)
filter_name = 'filter_name_example' # str | Filter for actions that have names containing the given string (optional)

try: 
    # Get a list of available actions
    api_response = api_instance.get_actions_using_get(filter_category=filter_category, filter_name=filter_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineActionsApi->get_actions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_category** | **str**| Filter for actions that are within a specific category | [optional] 
 **filter_name** | **str**| Filter for actions that have names containing the given string | [optional] 

### Return type

[**list[ActionResource]**](ActionResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

