# swagger_client.BRERuleEngineEventsApi

All URIs are relative to *https://devsandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fire_event_using_post**](BRERuleEngineEventsApi.md#fire_event_using_post) | **POST** /bre/events | Fire a new event, based on an existing trigger


# **fire_event_using_post**
> fire_event_using_post(bre_event=bre_event, authentication=authentication)

Fire a new event, based on an existing trigger

Parameters within the event must match names and types from the trigger. Actual rule execution is asynchornous.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BRERuleEngineEventsApi()
bre_event = swagger_client.BreEvent() # BreEvent | The BRE event object (optional)
authentication = swagger_client.OAuth2Authentication() # OAuth2Authentication | The authentication object (optional)

try: 
    # Fire a new event, based on an existing trigger
    api_instance.fire_event_using_post(bre_event=bre_event, authentication=authentication)
except ApiException as e:
    print("Exception when calling BRERuleEngineEventsApi->fire_event_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bre_event** | [**BreEvent**](BreEvent.md)| The BRE event object | [optional] 
 **authentication** | [**OAuth2Authentication**](OAuth2Authentication.md)| The authentication object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

