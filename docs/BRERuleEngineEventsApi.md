# swagger_client.BRERuleEngineEventsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fire_event_using_post**](BRERuleEngineEventsApi.md#fire_event_using_post) | **POST** /bre/events | Fire a new event, based on an existing trigger


# **fire_event_using_post**
> fire_event_using_post(bre_event=bre_event)

Fire a new event, based on an existing trigger

Parameters within the event must match names and types from the trigger. Actual rule execution is asynchornous.

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
api_instance = swagger_client.BRERuleEngineEventsApi()
bre_event = swagger_client.BreEvent() # BreEvent | The BRE event object (optional)

try: 
    # Fire a new event, based on an existing trigger
    api_instance.fire_event_using_post(bre_event=bre_event)
except ApiException as e:
    print("Exception when calling BRERuleEngineEventsApi->fire_event_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bre_event** | [**BreEvent**](BreEvent.md)| The BRE event object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

